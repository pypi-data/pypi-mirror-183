from jinja2 import Environment,PackageLoader,FileSystemLoader,PrefixLoader
import jinja2
from jinja2 import ext
import  sys
import re
import ctypes
import textwrap
import io
import os
from .utils import load_json,EasyDict


class PythonExtension(ext.Extension):
    # a set of names that trigger the extension.
    tags = {'py'}

    def __init__(self, environment: Environment):
        super().__init__(environment)

    def parse(self, parser):
        lineno = next(parser.stream).lineno
        body = parser.parse_statements(['name:endpy'], drop_needle=True)
        return jinja2.nodes.CallBlock(self.call_method('_exec_python',
                                                       [jinja2.nodes.ContextReference(),
                                                        jinja2.nodes.DerivedContextReference(),
                                                        jinja2.nodes.Const(lineno),
                                                        jinja2.nodes.Const(parser.filename)]),
                                      [], [], body).set_lineno(lineno)

    def _exec_python(self, ctx, derived_ctx, lineno, filename, caller):
        # Remove access indentation
        # ctx=derived_ctx
        code = textwrap.dedent(caller())
        # Compile the code.
        compiled_code = compile("\n" * (lineno - 1) + code, filename or "string template", "exec")

        # Create string io to capture stdio and replace it.
        # Sometimes one may need to stream stdout to the file
        sout = io.StringIO()
        stdout = sys.stdout
        # sys.stdout = sout
        # print(ctx.parent.keys(), ctx.vars.keys())
        try:
            # print(filename)
            derived_ctx.parent["__name__"]=os.path.basename(filename).split(".")[0]
            derived_ctx.parent["__package__"] = os.path.dirname(filename.replace('\\','/').strip('./').strip('/')).replace('/','.')
            # Execute the code with the derived context parents as global and context vars as locals.
            # print("derived:",derived_ctx.parent.keys(),derived_ctx.vars.keys(),derived_ctx.get_exported().keys())
            # print("ctx:",ctx.parent.keys(),ctx.vars.keys(),ctx.get_exported().keys())
            exec(compiled_code, derived_ctx.parent, ctx.vars) #

            ## Set all variable names as exported vars,
            ctx.exported_vars=set(ctx.vars.keys())
            # print("ctx:", ctx.parent.keys(), ctx.vars.keys(), ctx.get_exported().keys())
        except Exception:
            raise
        finally:
            # Restore stdout whether the code crashed or not.
            sys.stdout = stdout

        # Get a set of all names in the code.
        code_names = set(compiled_code.co_names)

        # The the frame in the jinja generated python code.
        caller_frame = sys._getframe(2)
        var_name_regex = re.compile(r"l_(\d+)_(.+)")
        # Loop through all the locals.
        for local_var_name in caller_frame.f_locals:
            # Look for variables matching the template variable regex.
            match = re.match(var_name_regex, local_var_name)
            if match:
                # Get the variable name.
                var_name = match.group(2)

                # If the variable's name appears in the code and is in the locals.
                if (var_name in code_names) and (var_name in ctx.vars):
                    # Copy the value to the frame's locals.
                    caller_frame.f_locals[local_var_name] = ctx.vars[var_name]
                    # Do some ctypes vodo to make sure the frame locals are actually updated.
                    ctx.exported_vars.add(var_name)
                    ctypes.pythonapi.PyFrame_LocalsToFast(
                        ctypes.py_object(caller_frame),
                        ctypes.c_int(1))

        # Return the captured text.
        return sout.getvalue()


class MyEnvironment(Environment):
    def join_path(self, template, parent):
        template=template.replace('\\','/').replace('//','/')
        if './' in template or '../' in template:
            template=os.path.normpath(os.path.dirname(parent)+"/"+template).replace('\\','/')
            return template
        else:
            return template

def load_config_yaml(f, **kwargs):
    import yaml
    from importlib import import_module
    g = dict()
    g.update(
        import_module=import_module,
    )
    for func in ['abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr',
                 'classmethod', 'compile', 'complex', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec',
                 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id',
                 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'list', 'locals', 'map', 'max',
                 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'range',
                 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum',
                 'super', 'tuple', 'type', 'vars', 'zip']:
        if isinstance(__builtins__,dict):
            g[func]=__builtins__.get(func)
        else:
            g[func] = getattr(__builtins__, func)

    class MyUndefined(jinja2.Undefined):
        @classmethod
        def __repr__(self):
            return ""

    Undefined = MyUndefined

    def required(v, name):
        if isinstance(v, Undefined):
            raise jinja2.UndefinedError(name)
        return ""

    g["required"] = required

    singleton_mode=False
    if singleton_mode:
        with open(f, 'r', encoding='utf-8') as f:
            text = f.read()
            text = Environment(extensions=[PythonExtension,
                                           ext.do,
                                           ], undefined=Undefined).from_string(text, globals=g).render(**kwargs)
            return yaml.safe_load(text)
    else:
        # loader = PackageLoader("tasks",".")
        loader = FileSystemLoader(".")
        # print(loader.list_templates())
        f=f.replace('\\','/')
        text = MyEnvironment(loader=loader,extensions=[PythonExtension,
                                ext.do,
                                ], undefined=Undefined).get_template(f,globals=g).render(**kwargs)
        return yaml.safe_load(text)

def load_config(arg_file):
    if arg_file.endswith('.yaml') or arg_file.endswith('.yml'):
        cfg = load_config_yaml(arg_file)
    elif arg_file.endswith('.json'):
        cfg = load_json(arg_file)
    else:
        cfg = load_json(arg_file)

    return EasyDict(**cfg)

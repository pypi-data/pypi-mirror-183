
builder_factory = {}
def register(name):
    def decorator(func):
        builder_factory[name]=func
        return func


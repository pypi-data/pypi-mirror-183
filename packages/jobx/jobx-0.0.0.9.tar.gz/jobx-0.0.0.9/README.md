# jobx
---
run batch scripts in a managed way

1. 安装 jobx : pip install -U -i https:pypi.org/simple jobx
2. 创建任务配置文件，如tasks.yaml
3. 启动任务 
   1. 运行所有任务 jobx tasks.yaml
   2. 运行指定任务 jobx tasks.yaml demo1
   3. 运行多个指定任务 jobx tasks.yaml demo1,demo3
   4. 运行通配符匹配的所有任务 jobx tasks.yaml demo*,*2


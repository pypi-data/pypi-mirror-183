from libs.commands.Command import Command

class Demo(Command):
    # 命令名
    name = "demo"
    # 命令介绍
    desc = "介绍"
    # 必填参数
    arguments = [
        {"name": "arg1", "desc": ""},
    ]
    # 选填参数
    options = [
        {"name": "kwarg1", "require": True, "default": None, "desc": ""},
        {"name": "kwarg2", "require": False, "default": None, "desc": ""},
        {"name": "kwarg3", "require": False, "default": "test", "desc": ""}
    ]

    def handler(self,*args,**kwargs):
        print("demo 命令参数",self.args,self.kwargs)
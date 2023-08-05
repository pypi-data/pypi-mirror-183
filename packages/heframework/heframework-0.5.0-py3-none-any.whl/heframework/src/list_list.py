# heStudio Framework List by tuple


class list:
    def __init__(self, name, command, info):
        self.code = None
        if not name:
            self.code = 25000
            self.error = 25001
        else:
            self.name = name
            pass
        if not command:
            self.code = 25000
            self.error = 25001
        else:
            self.command = command
            pass
        if not info:
            self.code = 25000
            self.error = 25001
        else:
            self.info = info
            pass

    def list(self):
        if self.code == 25000:
            # # 该代码仅供测试使用
            # print(self.error)
            return self.error
        else:
            num = 0
            for name in self.name:
                num += 1
                print(str(num), ":", name)
            choose = input(str(self.info))
            commands = self.command
            exec(commands[int(int(choose)-1)])
            return 20000

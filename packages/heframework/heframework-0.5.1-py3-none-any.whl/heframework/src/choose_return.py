import json


class list:
    def __init__(self, name, return_text, info):
        self.code = None
        if not name:
            self.code = 25000
            self.error = 25001
        else:
            self.name = name
            pass
        if not return_text:
            self.code = 25000
            self.error = 25001
        else:
            self.return_text = return_text
            pass
        if not info:
            self.code = 25000
            self.error = 25001
        else:
            self.info = info
            pass
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
            choice = input(str(self.info))
            returns = self.return_text
            # # 该代码仅供测试使用
            # print(returns[int(int(choice)-1)])
            re = returns[int(int(choice)-1)]
            return re


class json_mode:
    def __init__(self, json_file, info):
        self.code = None
        if not json_file:
            self.code = 25000
            self.error = 25002
        else:
            self.file = json_file
            if not info:
                self.code = 25000
                self.error = 25001
            else:
                self.info = info

    def list(self):
        if self.code == 25000:
            # # 该代码仅供测试使用
            # print(self.error)
            return self.error
        else:
            db = json.load(open(self.file, encoding="utf-8"))
            return list(name=db["name"],
                        return_text=db["return_text"], info=self.info).list()

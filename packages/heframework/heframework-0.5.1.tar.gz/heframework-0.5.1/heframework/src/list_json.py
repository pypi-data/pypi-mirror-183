# heStudio Framework List

import json
import heframework


class list:
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
            heframework.list_command(mode="list",name=db["name"],
                           command=db["command"], info=self.info)

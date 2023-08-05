# heStudio Framework

# show框架

def show(message: str = "", title: str = ""):
    import heframework.src.show
    return heframework.src.show.show(message, title).show()



# list_command框架

def list_command(mode: str = "list", json_file: str = "", info: str = "", name: list = [], command: list = []):
    import heframework.src.list_json
    import heframework.src.list_list
    if mode == "list":
        return heframework.src.list_list.list(name, command, info).list()
    elif mode == "json":
        return heframework.src.list_json.list(json_file, info).list()
    else:
        return 25003


# choose框架
def choose(mode: str = "list", json_file: str = "", info: str = "", name: list = [], return_text: list = []):
    import heframework.src.choose_return
    if mode == "list":
        return heframework.src.choose_return.list(name, return_text, info).list()
    elif mode == "json":
        return heframework.src.choose_return.json_mode(json_file, info).list()
    else:
        return 25003


# refresh_show框架
class refresh_show:
    def __init__(self, title:str="", geometry:str=""):
        import heframework.src.refresh
        show = heframework.src.refresh.show(title, geometry)
        self.show=show
    
    def refresh(self, message:str=""):
        return self.show.update(message)

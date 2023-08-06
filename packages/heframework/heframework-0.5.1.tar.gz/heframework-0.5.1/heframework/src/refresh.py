import tkinter
import threading
import time

def ui():
    global main
    main = tkinter.Tk()
    global message_show
    message_show = tkinter.Text(main)
    message_show.pack(side="top")
    air = tkinter.Label(main, text=" ")
    air.pack(side="top")
    ok = tkinter.Button(main, text="确定", command=main.destroy)
    ok.pack(side="bottom")
    main.mainloop()

class show:
    def __init__(self, title, geometry:str=""):
        global window
        window = threading.Thread(target=ui)
        window.start()
        time.sleep(1)
        if title:
            main.title(title)
        else:
            pass
        if geometry:
            main.geometry(geometry)
        else:
            pass
        message_show.insert(tkinter.END, "Loading...")
    
    def update(self, message:str):
        if not message:
            return 25001
        else:
            if not window.is_alive():
                return 21099
            else:
                message_show.delete(0.0, tkinter.END)
                message_show.insert(tkinter.END, message)
                return 20000
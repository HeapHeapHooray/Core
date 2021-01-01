import tkinter as tk
from threading import Thread

tcl = None
tcl_thread = None
def loop_tcl():
    global tcl
    tcl = tk.Tk()
    tcl.withdraw()
    tcl.mainloop()
def run_tcl() -> bool :
    global tcl
    global tcl_thread
    tcl_thread = Thread(target=loop_tcl,daemon=True)
    tcl_thread.start()
    while tcl == None:
        pass
    return True
def set_running():
    if not is_running():
        run_tcl()
def is_running() -> bool :
    global tcl
    return not (tcl == None)
def update():
    global tcl
    if not (tcl == None):
        tcl.update()

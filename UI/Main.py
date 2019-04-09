try:
    import tkinter as tk  # for python 3
except:
    import Tkinter as tk  # for python 2
import sys
import os
import pygubu
import Logic


class Application:
    def __init__(self, master):

        #1: Create a builder
        self.builder = builder = pygubu.Builder()

        #2: Load an ui file
        builder.add_from_file('resources\\Main_Test.ui')

        #3: Create the widget using a master as parent
        self.mainwindow = builder.get_object('Main_Frame', master)

        # Configure callbacks
        callbacks = {
            'launchnextgame': Logic.launchnextgame,
            'timerstart': Logic.timerstart,
            'stop_music': Logic.stop_music
        }

        builder.connect_callbacks(callbacks)

        # entry = self.builder.get_object('Entry_1')


def exitfun():
    print("User exited ...")
    os._exit(0)


def start():
    root = tk.Tk()
    root.title("SteamGL")
    app = Application(root)
    root.protocol("WM_DELETE_WINDOW", exitfun)
    icon = tk.PhotoImage(file="resources\\Icon.png")
    root.tk.call('wm', 'iconphoto', root._w, icon)
    root.mainloop()

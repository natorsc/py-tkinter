# -*- coding: utf-8 -*-
"""Python - Tkinter."""

import pathlib
import tkinter as tk
from tkinter import ttk

APP_NAME = 'br.com.justcode.Tk'

BASE_DIR = pathlib.Path(__file__).resolve().parent
ICON = BASE_DIR.parent / 'data' / 'icons' / f'{APP_NAME}.png'


class App(tk.Frame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.master = kwargs['master']

        self.pack(expand=tk.TRUE, fill=tk.BOTH, padx=6, pady=6)

        label1 = tk.Label(master=self, text='Lorem Ipsum')
        label1.pack(expand=tk.TRUE, fill=tk.BOTH)

        separator = ttk.Separator(master=self, orient='horizontal')
        separator.pack(fill=tk.X)

        label2 = tk.Label(master=self, text='Lorem Ipsum Dolor')
        label2.pack(expand=tk.TRUE, fill=tk.BOTH)


if __name__ == '__main__':
    import sys

    if sys.platform == 'win32':
        from ctypes import windll

        windll.shell32.SetCurrentProcessExplicitAppUserModelID(APP_NAME)

    master = tk.Tk(className=APP_NAME)
    master.title('Python - Tkinter')
    master.geometry('683x384')
    master.minsize(683, 384)
    master.iconphoto(True, tk.PhotoImage(file=ICON))

    app = App(master=master)
    app.mainloop()

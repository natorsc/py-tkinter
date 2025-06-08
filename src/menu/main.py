# -*- coding: utf-8 -*-
"""Python - Tkinter."""

import pathlib
import tkinter as tk

APP_NAME = 'br.com.justcode.Tk'

BASE_DIR = pathlib.Path(__file__).resolve().parent
ICON = BASE_DIR.parent / 'data' / 'icons' / f'{APP_NAME}.png'


class App(tk.Frame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.master = kwargs['master']
        self.master.bind_all('<Control-n>', self.on_new_menu_activated)
        self.master.bind_all('<Control-q>', self.on_quit_menu_activated)

        self.pack(expand=tk.TRUE, fill=tk.BOTH, padx=6, pady=6)

        menubar = tk.Menu(master=self)
        self.master.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='File', menu=file_menu)

        file_menu.add_command(
            label='New',
            command=self.on_new_menu_activated,
            accelerator='Ctrl + n',
        )

        file_menu.add_separator()
        file_menu.add_command(
            label='Exit',
            command=self.on_quit_menu_activated,
            accelerator='Ctrl + q',
        )

        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Help', menu=help_menu)

        help_menu.add_command(
            label='About',
            command=self.on_about_menu_activated,
        )

    def on_new_menu_activated(self, event=None):
        print('on_new_menu_activated')

    def on_quit_menu_activated(self, event=None):
        print('on_quit_menu_activated')
        self.master.quit()

    def on_about_menu_activated(self):
        print('on_about_menu_activated')


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

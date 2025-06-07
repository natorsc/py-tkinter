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

        self.pack(expand=tk.TRUE, fill=tk.BOTH, padx=6, pady=6)

        self.radio_selection = tk.StringVar()
        self.radio_selection.set('a')

        for value in ['a', 'b', 'c']:
            radio_button = tk.Radiobutton(
                master=self,
                text=f'Item {value}.',
                variable=self.radio_selection,
                value=value,
                command=self.on_radiobutton_select,
            )
            radio_button.pack(anchor=tk.W)

    def on_radiobutton_select(self):
        print(self.radio_selection.get())


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

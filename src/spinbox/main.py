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

        self.spinbox_value = tk.IntVar(value=5)

        self.current_value_label = tk.Label(
            master=self,
            text=f'...',
        )
        self.current_value_label.pack(expand=tk.TRUE, fill=tk.X)

        spinbox = tk.Spinbox(
            master=self,
            from_=0,
            to=10,
            increment=1,
            textvariable=self.spinbox_value,
            command=self.on_spinbox_change,
            wrap=True,
        )
        spinbox.pack(expand=tk.TRUE, fill=tk.X, pady=6)

        self.get_value_button = tk.Button(
            master=self,
            text='Get spinbox value',
            command=self.on_button_clicked,
        )
        self.get_value_button.pack()

    def on_spinbox_change(self):
        self.current_value_label.config(text=self.spinbox_value.get())

    def on_button_clicked(self):
        print(self.spinbox_value.get())


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

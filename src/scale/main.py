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

        self.current_value_label = tk.Label(master=self, text='...')
        self.current_value_label.pack(expand=tk.TRUE, fill=tk.X)

        self.scale_value = tk.IntVar()
        scale = tk.Scale(
            master=self,
            orient=tk.HORIZONTAL,
            from_=0,
            to=100,
            resolution=1,
            tickinterval=10,
            label='Level',
            variable=self.scale_value,
            command=self.on_update_label,
        )

        scale.set(50)
        scale.pack(expand=tk.TRUE, fill=tk.X, pady=6)

        button = tk.Button(
            master=self,
            text='Get scale value',
            command=self.on_button_clicked,
        )
        button.pack()

    def on_update_label(self, value):
        self.current_value_label.config(text=f'Current: {value}')

    def on_button_clicked(self):
        print(self.scale_value.get())


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

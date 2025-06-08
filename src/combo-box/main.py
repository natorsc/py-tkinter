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

        self.selected_color = tk.StringVar()
        self.selected_color.set('Select')

        self.label = tk.Label(
            master=self,
            text=self.selected_color.get(),
        )
        self.label.pack(expand=tk.TRUE, fill=tk.BOTH)

        self.color_options = [
            'Red',
            'Green',
            'Blue',
            'Yellow',
            'Orange',
            'Purple',
            'Black',
            'White',
            'Gray',
        ]

        combo_box = ttk.Combobox(
            master=self,
            textvariable=self.selected_color,
            values=self.color_options,
            state='normal',
        )
        combo_box.set('Select')
        combo_box.bind('<<ComboboxSelected>>', self.on_combobox_select)
        combo_box.pack(expand=tk.TRUE, fill=tk.X, pady=6)

        self.get_value_button = tk.Button(
            master=self,
            text='Get combobox value',
            command=self.on_button_clicked,
        )
        self.get_value_button.pack()

    def on_combobox_select(self, event):
        self.label.config(text=self.selected_color.get())

    def on_button_clicked(self):
        print(self.selected_color.get())


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

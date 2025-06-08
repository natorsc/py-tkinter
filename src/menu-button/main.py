# -*- coding: utf-8 -*-
"""Python - Tkinter."""

import pathlib
import random
import tkinter as tk

APP_NAME = 'br.com.justcode.Tk'

BASE_DIR = pathlib.Path(__file__).resolve().parent
ICON = BASE_DIR.parent / 'data' / 'icons' / f'{APP_NAME}.png'


class App(tk.Frame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.master = kwargs['master']

        self.pack(expand=tk.TRUE, fill=tk.BOTH, padx=6, pady=6)

        menu_button = tk.Menubutton(
            master=self,
            text='Select',
            relief=tk.RAISED,
            indicatoron=True,
        )
        menu_button.pack(pady=6)

        self.label = tk.Label(
            master=self,
            text='Lorem ipsum.',
        )
        self.label.pack(expand=tk.TRUE, fill=tk.BOTH)

        self.color_menu = tk.Menu(menu_button, tearoff=0)
        self.color_menu.add_command(
            label='Red',
            command=lambda: self.on_color_select('Red', 'red'),
        )
        self.color_menu.add_command(
            label='Blue',
            command=lambda: self.on_color_select('Blue', 'blue'),
        )
        self.color_menu.add_separator()
        self.color_menu.add_command(
            label='Random',
            command=lambda: self.on_color_select('Random', 'random'),
        )
        menu_button['menu'] = self.color_menu

    def on_color_select(self, color_name, color_hex_or_name):
        self.label.config(text=f'Selected: {color_name}')
        if color_hex_or_name == 'random':
            value = random.randint(0, 0xFFFFFF)
            self.label.config(bg=f'#{value:06x}')
        else:
            try:
                self.label.config(bg=color_hex_or_name)
            except tk.TclError:
                self.label.config(bg='white')
                self.label.config(text=f"Invalid color '{color_hex_or_name}'.")


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

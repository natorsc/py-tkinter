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

        scrollbar = tk.Scrollbar(master=self, orient=tk.VERTICAL)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox = tk.Listbox(
            master=self,
            selectmode=tk.SINGLE,
            yscrollcommand=scrollbar.set,
        )
        self.listbox.bind('<<ListboxSelect>>', self.on_listbox_select)
        self.listbox.pack(expand=tk.TRUE, fill=tk.BOTH)

        for i in range(1, 100):
            self.listbox.insert(tk.END, f'Item {i}')

    def on_listbox_select(self, event):
        if self.listbox.curselection():
            selected_index = self.listbox.curselection()[0]
            selected_item = self.listbox.get(selected_index)
            print(selected_index)
            print(selected_item)


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

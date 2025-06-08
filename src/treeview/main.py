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

        treeview = ttk.Treeview(
            master=self,
            columns=('ID', 'column 01', 'column 02'),
            show='headings',
        )
        treeview.heading(column='ID', text='ID', anchor=tk.CENTER)
        treeview.heading(column='column 01', text='column 01', anchor=tk.W)
        treeview.heading(
            column='column 02',
            text='column 02',
            anchor=tk.CENTER,
        )
        treeview.column(
            column='ID',
            width=50,
            stretch=tk.NO,
            anchor=tk.CENTER,
        )
        treeview.column(
            column='column 01',
            width=100,
            stretch=tk.NO,
            anchor=tk.W,
        )
        treeview.column(
            column='column 02',
            width=100,
            stretch=tk.YES,
            anchor=tk.CENTER,
        )
        treeview.pack(expand=tk.TRUE, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(
            master=treeview,
            orient=tk.VERTICAL,
            command=treeview.yview,
        )
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        treeview.config(yscrollcommand=self.scrollbar.set)

        for i in range(1, 101):
            treeview.insert(
                parent='',
                index=tk.END,
                values=(i, f'Item {i}', f'Item {i}.'),
            )


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

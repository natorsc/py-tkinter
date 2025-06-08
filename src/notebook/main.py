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

        self.notebook = ttk.Notebook(master=self)
        self.notebook.bind('<<NotebookTabChanged>>', self.on_tab_changed)
        self.notebook.pack(expand=tk.TRUE, fill=tk.BOTH)

        tab_01 = tk.Frame(master=self.notebook)
        tab_01.pack(fill=tk.BOTH, expand=tk.TRUE)
        self.notebook.add(child=tab_01, text='Tab 01', compound=tk.TOP)

        label_tab_01 = tk.Label(master=tab_01, text='Lorem ipsum.')
        label_tab_01.pack(expand=tk.TRUE, fill=tk.BOTH)

        tab_02 = tk.Frame(master=self.notebook)
        tab_02.pack(fill=tk.BOTH, expand=tk.TRUE)
        self.notebook.add(child=tab_02, text='Tab 02')

        label_tab_02 = tk.Label(
            master=tab_02,
            text='Lorem ipsum dolor.',
        )
        label_tab_02.pack(expand=tk.TRUE, fill=tk.BOTH)

        tab_03 = tk.Frame(master=self.notebook)
        tab_03.pack(fill=tk.BOTH, expand=tk.TRUE)
        self.notebook.add(child=tab_03, text='Tab 03')

        label_tab_03 = tk.Label(
            master=tab_03,
            text='Lorem ipsum dolor sit.',
        )
        label_tab_03.pack(expand=tk.TRUE, fill=tk.BOTH)

        self.notebook.select(tab_02)

    def on_tab_changed(self, event):
        selected_tab_id = self.notebook.select()
        selected_tab_text = self.notebook.tab(selected_tab_id, 'text')
        print(selected_tab_id)
        print(selected_tab_text)


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

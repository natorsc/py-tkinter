# -*- coding: utf-8 -*-
"""Python - Tkinter."""

import pathlib
import tkinter as tk
from tkinter import ttk

APP_NAME = 'br.com.justcode.Tk'

BASE_DIR = pathlib.Path(__file__).resolve().parent
ICON = BASE_DIR.parent / 'data' / 'icons' / f'{APP_NAME}.png'


class App(tk.Frame):
    is_task_running = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.master = kwargs['master']

        self.pack(expand=tk.TRUE, fill=tk.BOTH, padx=6, pady=6)

        self.progress_value = tk.DoubleVar()
        self.progress_value.set(0)

        self.percentage_label = tk.Label(
            master=self,
            text='0%',
        )
        self.percentage_label.pack(expand=tk.TRUE, fill=tk.X)

        # 1. Criar o tk.Progressbar()
        self.progressbar = ttk.Progressbar(
            master=self,
            orient=tk.HORIZONTAL,
            # length=400,
            mode='determinate',
            variable=self.progress_value,
            maximum=100,
        )
        self.progressbar.pack(expand=tk.TRUE, fill=tk.X, pady=12)

        self.start_button = tk.Button(
            master=self,
            text='Start',
            command=self.start_task_simulation,
        )
        self.start_button.pack(expand=tk.TRUE, fill=tk.X)

        reset_button = tk.Button(
            master=self,
            text='Reset',
            command=self.reset_progressbar,
        )
        reset_button.pack(expand=tk.TRUE, fill=tk.X)

    def start_task_simulation(self):
        if self.is_task_running:
            return False
        self.is_task_running = True
        self.start_button.config(state=tk.DISABLED)
        self.simulate_progress(0)

    def simulate_progress(self, current_progress):
        if current_progress <= 100 and self.is_task_running:
            self.progress_value.set(current_progress)
            self.percentage_label.config(text=f'{int(current_progress)}%')
            self.master.after(50, self.simulate_progress, current_progress + 1)
        else:
            self.is_task_running = False
            self.start_button.config(state=tk.NORMAL)
            if current_progress > 100:
                print('do something!')

    def reset_progressbar(self):
        self.is_task_running = False
        self.progress_value.set(0)
        self.percentage_label.config(text='0%')
        self.start_button.config(state=tk.NORMAL)


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

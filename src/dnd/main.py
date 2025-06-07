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

        self._drag_data = {'x': 0, 'y': 0, 'item': None}

        draggable_label = tk.Label(
            self,
            text='Lorem Ipsum',
            bg='lightblue',
            relief='solid',
            borderwidth=1,
            padx=10,
            pady=5,
        )
        draggable_label.place(x=50, y=50)
        draggable_label.bind('<Button-1>', self.on_drag_start)
        draggable_label.bind('<B1-Motion>', self.on_drag_motion)
        draggable_label.bind('<ButtonRelease-1>', self.on_drag_release)

    def on_drag_start(self, event):
        self._drag_data['item'] = event.widget
        self._drag_data['x'] = event.x
        self._drag_data['y'] = event.y
        print(f'Drag start: Widget {event.widget} ({event.x}, {event.y})')

    def on_drag_motion(self, event):
        if self._drag_data['item']:
            widget = self._drag_data['item']
            new_x = widget.winfo_x() + (event.x - self._drag_data['x'])
            new_y = widget.winfo_y() + (event.y - self._drag_data['y'])
            widget.place(x=new_x, y=new_y)

    def on_drag_release(self, event):
        if self._drag_data['item']:
            widget = self._drag_data['item']
            self._drag_data['item'] = None
            self._drag_data['x'] = 0
            self._drag_data['y'] = 0
            print(f'Drag release: Widget {widget}.')


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

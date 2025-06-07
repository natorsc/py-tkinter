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

        self.canvas = tk.Canvas(
            master=self,
            width=500,
            height=300,
            bg='lightgray',
            highlightbackground='blue',
            highlightthickness=2,
        )
        self.canvas.pack(expand=tk.TRUE, fill=tk.BOTH)

        rect = self.canvas.create_rectangle(
            50,
            50,
            150,
            100,
            fill='lightblue',
            outline='blue',
            width=2,
            tags='tag-name',
        )
        self.canvas.create_text(
            100,
            75,
            text='Retângulo',
            fill='darkblue',
            font=('Arial', 10, 'bold'),
        )
        circle_id = self.canvas.create_oval(
            200,
            50,
            300,
            150,
            fill='lightgreen',
            outline='green',
            width=2,
            tags='tag-name',
        )
        self.canvas.create_text(
            250,
            100,
            text='Círculo',
            fill='darkgreen',
            font=('Arial', 10, 'bold'),
        )
        self.canvas.create_line(
            50, 200, 450, 200, fill='red', width=3, arrow=tk.LAST
        )
        self.canvas.create_text(
            250,
            215,
            text='Lorem Ipsum',
            fill='red',
            font=('Arial', 10, 'italic'),
        )
        self.canvas.tag_bind('tag-name', '<Button-1>', self.on_shape_clicked)

    def on_shape_clicked(self, event):
        clicked_item_id = self.canvas.find_closest(event.x, event.y)[0]
        item_tags = self.canvas.gettags(clicked_item_id)

        if 'tag-name' in item_tags:
            current_fill_color = self.canvas.itemcget(clicked_item_id, 'fill')
            new_fill_color = (
                'orchid' if current_fill_color != 'orchid' else 'lightblue'
            )
            self.canvas.itemconfig(clicked_item_id, fill=new_fill_color)
            print(f'ID={clicked_item_id}')
            print(f'Tags={item_tags}')
            print(f'Color: {new_fill_color}')


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

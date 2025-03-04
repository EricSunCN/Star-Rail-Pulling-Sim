import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Tkinter PhotoImage Demo')
        self.geometry('320x150')

        self.python_image = tk.PhotoImage(file='backgroundImage/starrail.png')
        ttk.Label(self, image=self.python_image).pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()
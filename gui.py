#imports
import tkinter as tk
from tkinter import ttk

#gui window
root = tk.Tk()
root.title("Honkai Star Rail")
root.geometry("500x400+50+50")

#Background images
image = tk.PhotoImage(file='backgroundImage/starrail.png')
tk.Label(root, image=image).pack()

#side buttons for switching banners
#characterBannerA = ttk.Button(root, text='Character Banner A', command= )




root.mainloop()


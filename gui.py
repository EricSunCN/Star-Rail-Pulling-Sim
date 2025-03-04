#imports
import tkinter as tk
from tkinter import ttk
from tkinter import *

def hi():
    label_pic.config(image=bannerABackground)

#gui window
root = tk.Tk()
root.title("Honkai Star Rail")
root.geometry("500x400+50+50")

#Background images
background = tk.PhotoImage(file='backgroundImage/starrail.png')
bannerABackground = tk.PhotoImage(file='backgroundImage/standard banner.png')
label_pic = tk.Label(root, image=background)
label_pic.pack(pady=15)

#side buttons for switching banners
characterBannerA = ttk.Button(root, text='Character Banner A', command=hi)
characterBannerA.pack(side=tk.LEFT)





root.mainloop()


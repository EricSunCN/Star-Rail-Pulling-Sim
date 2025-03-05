#imports
import tkinter as tk
from idlelib.debugger_r import restart_subprocess_debugger
from tkinter import ttk
from pull import *
from tkinter import *

#Updates the background image
def change_bg():
    bg_pic.config(image=bannerABackground)

#gui window
root = tk.Tk()
root.title("Honkai Star Rail")
root.geometry("750x600+50+50")

#Background images
default = tk.PhotoImage(file='backgroundImage/starrail.png')
bannerABackground = tk.PhotoImage(file='backgroundImage/standard banner.png')

#Background_Label
bg_pic = tk.Label(root, image=default)
bg_pic.pack(pady=15)

#side buttons for switching banners
standardBanner = ttk.Button(root, text='Standard Banner', command=change_bg)
standardBanner.pack(side=tk.LEFT)


pull = ttk.Button(root, text='10 Pull', command=tenPull)
pull.pack(side=tk.LEFT)

item = ttk.Label(root, text=tenPullResults)
item.pack(side=tk.BOTTOM)



root.mainloop()


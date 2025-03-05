#imports
import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk

from pull import *

#Updates the background image
def changeBgStandard():
    bg_pic.config(image=standardBannerBgFinal)

def changeBgLimitedOne():
    bg_pic.config(image=limitedBannerBgFinal)
    pull.pack()

#gui window
root = tk.Tk()
root.title("Honkai Star Rail")
root.geometry("700x700+50+50")

#Background images
default = Image.open('backgroundImage/defaultBackground.jpg')
standardBannerBg = Image.open('backgroundImage/standardBannerBackground.jpeg')
limitedBannerBg = Image.open('backgroundImage/limitedBannerBackground.jpg')

#Resize
defaultResized = default.resize((700,400))
defaultFinal = ImageTk.PhotoImage(defaultResized)
standardBannerBgResized = standardBannerBg.resize((700,400))
standardBannerBgFinal = ImageTk.PhotoImage(standardBannerBgResized)
limitedBannerBgResized = limitedBannerBg.resize((700,400))
limitedBannerBgFinal = ImageTk.PhotoImage(limitedBannerBgResized)

#Background_Label
bg_pic = Label(root, image=defaultFinal)
bg_pic.image = default
bg_pic.pack(pady=15)

#side buttons for switching banners
standardBanner = ttk.Button(root, text='Standard Banner', command=changeBgStandard)
standardBanner.pack(side=tk.LEFT)

#
limitedBannerOne = ttk.Button(root, text='Limited Banner', command=changeBgLimitedOne)
limitedBannerOne.pack(side=tk.LEFT)

pull = ttk.Button(root, text='10 Pull', command=tenPull)
pull.pack(side=tk.LEFT)

item = Label(root, text=tenPullResults)
item.pack(side=tk.BOTTOM)

pull.pack_forget()


root.mainloop()


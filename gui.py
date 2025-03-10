#imports
import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
from pull import *

allowPullDisplay = False

#Updates the background image to standard banner
def changeBgStandard():
    bg_pic.config(image=standardBannerBgFinal)
#Changes the background image to the limited banner
def changeBgLimitedOne():
    global allowPullDisplay
    bg_pic.config(image=limitedBannerOneBgFinal)
    limitedFiveStarOne()
    if allowPullDisplay == False:
        tenPullButton.pack()
        singlePullButton.pack()
        singlePullButton.place(x=395, y=475)
        tenPullButton.place(x=550, y=475)
        allowPullDisplay = True
    print(allowPullDisplay)
def changeBgLimitedTwo():
    global allowPullDisplay
    bg_pic.config(image=limitedBannerTwoBgFinal)
    limitedFiveStarTwo()
    if allowPullDisplay == False:
        tenPullButton.pack()
        singlePullButton.pack()
        singlePullButton.place(x=395, y=475)
        tenPullButton.place(x=550, y=475)
        allowPullDisplay = True
    print(allowPullDisplay)
    #inglePullButton.place(x=395, y=475)
    #tenPullButton.place(x=550, y=475)
def tenPullFunction():
    tenPull()
    item.config(text=tenPullResults)


#gui window
root = tk.Tk()
root.title("Honkai Star Rail")
root.geometry("700x700+50+50")

#results
item = Label(root, text='')
item.pack(side=tk.BOTTOM)


#Background images
default = Image.open('backgroundImage/defaultBackground.jpg')
standardBannerBg = Image.open('backgroundImage/standardBannerBackground.jpeg')
standardBannerIc = Image.open('backgroundImage/standardBannerIcon.jpg')
limitedBannerOneBg = Image.open('backgroundImage/limitedBannerOneBackground.jpg')
limitedBannerOneIc = Image.open('backgroundImage/limitedBannerOneIcon.jpg')
limitedBannerTwoBg = Image.open('backgroundImage/limitedBannerTwoBackground.jpg')
limitedBannerTwoIc = Image.open('backgroundImage/limitedBannerTwoIcon.jpg')
singlePullIc = Image.open('backgroundImage/singlePull.jpg')
tenPullIc = Image.open('backgroundImage/tenPull.jpg')
#Add all of this to json file

#Resize
defaultResized = default.resize((700,400))
defaultFinal = ImageTk.PhotoImage(defaultResized)
standardBannerBgResized = standardBannerBg.resize((700,450))
standardBannerBgFinal = ImageTk.PhotoImage(standardBannerBgResized)
limitedBannerOneBgResized = limitedBannerOneBg.resize((700,450))
limitedBannerOneBgFinal = ImageTk.PhotoImage(limitedBannerOneBgResized)
limitedBannerTwoBgResized = limitedBannerTwoBg.resize((700,450))
limitedBannerTwoBgFinal = ImageTk.PhotoImage(limitedBannerTwoBgResized)

standardBannerIcResized = standardBannerIc.resize((100,50))
standardBannerIcFinal = ImageTk.PhotoImage(standardBannerIcResized)
limitedBannerOneIcResized = limitedBannerOneIc.resize((100,50))
limitedBannerOneIcFinal = ImageTk.PhotoImage(limitedBannerOneIcResized)
limitedBannerTwoIcResized = limitedBannerTwoIc.resize((100,50))
limitedBannerTwoIcFinal = ImageTk.PhotoImage(limitedBannerTwoIcResized)
singlePullIcResized = singlePullIc.resize((125,30))
singlePullIcFinal = ImageTk.PhotoImage(singlePullIcResized)
tenPullIcResized = tenPullIc.resize((125,30))
tenPullIcFinal = ImageTk.PhotoImage(tenPullIcResized)
#Background_Label
bg_pic = Label(root, image=defaultFinal)
bg_pic.image = default
bg_pic.pack(pady=15)

#side buttons for switching banners
standardBanner = tk.Button(root, text='Standard Banner', width=100, height=50, command=changeBgStandard, image=standardBannerIcFinal)
standardBanner.pack(side=tk.LEFT)
limitedBannerOne = tk.Button(root, text='Limited Banner A', width=100, height=50, command=changeBgLimitedOne, image=limitedBannerOneIcFinal)
limitedBannerOne.pack(side=tk.LEFT)
limitedBannerTwo = tk.Button(root, text='Limited Banner B', width=100, height=50, command=changeBgLimitedTwo, image=limitedBannerTwoIcFinal)
limitedBannerTwo.pack()
#Places the banner buttons in the correct space
limitedBannerOne.place(x=0,y=475)
limitedBannerTwo.place(x=0,y=530)
standardBanner.place(x=0,y=585)
#Pulling buttons
singlePullButton = tk.Button(root, text='1 Pull', width=140, height=30, command=singlePull, image=singlePullIcFinal)
singlePullButton.pack(side=tk.LEFT)
tenPullButton = tk.Button(root, text='10 Pull', width=140, height=30, command=tenPullFunction, image=tenPullIcFinal)
tenPullButton.pack(side=tk.BOTTOM)

#Exist button
exitButton = ttk.Button(root, text='Exit', command=exit)
exitButton.pack(side=tk.RIGHT)

#Results


#Hides the pull buttons on the home screen
tenPullButton.pack_forget()
singlePullButton.pack_forget()



root.mainloop()


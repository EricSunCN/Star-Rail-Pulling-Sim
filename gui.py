import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from pull import singlePull, tenPull, limitedFiveStarOne, limitedFiveStarTwo

# Global Variables
allowPullDisplay = False
root = None
bg_pic = None
singlePullButton = None
tenPullButton = None
item = None

def changeBgStandard():
    bg_pic.config(image=standardBannerBgFinal)

def changeBgLimitedOne():
    global allowPullDisplay
    bg_pic.config(image=limitedBannerOneBgFinal)
    limitedFiveStarOne()
    showPullButtons()

def changeBgLimitedTwo():
    global allowPullDisplay
    bg_pic.config(image=limitedBannerTwoBgFinal)
    limitedFiveStarTwo()
    showPullButtons()

def showPullButtons():
    global allowPullDisplay
    if not allowPullDisplay:
        singlePullButton.place(x=395, y=475)
        tenPullButton.place(x=550, y=475)
        allowPullDisplay = True

def tenPullFunction():
    results = tenPull()

def start_gui():
    global root, bg_pic, singlePullButton, tenPullButton, item
    global standardBannerBgFinal, limitedBannerOneBgFinal, limitedBannerTwoBgFinal
    global standardBannerIcFinal, limitedBannerOneIcFinal, limitedBannerTwoIcFinal
    global singlePullIcFinal, tenPullIcFinal

    root = tk.Tk()
    root.title("Honkai Star Rail")
    root.geometry("700x700+50+50")

    # Results Label
    item = tk.Label(root, text='', font=("Arial", 12))
    item.pack(side=tk.BOTTOM)

    # Get the absolute path of the assets directory
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    ASSETS_PATH = os.path.join(BASE_DIR, "assets", "backgroundImage")

    # Load and Resize Images
    def load_image(filename, size):
        return ImageTk.PhotoImage(Image.open(os.path.join(ASSETS_PATH, filename)).resize(size))

    defaultFinal = load_image('defaultBackground.jpg', (700, 400))
    standardBannerBgFinal = load_image('standardBannerBackground.jpeg', (700, 450))
    limitedBannerOneBgFinal = load_image('limitedBannerOneBackground.jpg', (700, 450))
    limitedBannerTwoBgFinal = load_image('limitedBannerTwoBackground.jpg', (700, 450))

    standardBannerIcFinal = load_image('standardBannerIcon.jpg', (100, 50))
    limitedBannerOneIcFinal = load_image('limitedBannerOneIcon.jpg', (100, 50))
    limitedBannerTwoIcFinal = load_image('limitedBannerTwoIcon.jpg', (100, 50))
    singlePullIcFinal = load_image('singlePull.jpg', (125, 30))
    tenPullIcFinal = load_image('tenPull.jpg', (125, 30))

    # Background Label
    bg_pic = tk.Label(root, image=defaultFinal)
    bg_pic.image = defaultFinal
    bg_pic.pack(pady=15)

    # Banner Buttons
    standardBanner = tk.Button(root, image=standardBannerIcFinal, command=changeBgStandard, borderwidth=0)
    limitedBannerOne = tk.Button(root, image=limitedBannerOneIcFinal, command=changeBgLimitedOne, borderwidth=0)
    limitedBannerTwo = tk.Button(root, image=limitedBannerTwoIcFinal, command=changeBgLimitedTwo, borderwidth=0)

    # Positioning
    standardBanner.place(x=0, y=585)
    limitedBannerOne.place(x=0, y=475)
    limitedBannerTwo.place(x=0, y=530)

    # Pulling Buttons
    singlePullButton = tk.Button(root, image=singlePullIcFinal, command=singlePull, borderwidth=0)
    tenPullButton = tk.Button(root, image=tenPullIcFinal, command=tenPullFunction, borderwidth=0)

    # Exit Button
    exitButton = ttk.Button(root, text='Exit', command=root.quit)
    exitButton.pack(side=tk.RIGHT)

    # Hide pull buttons on the home screen
    singlePullButton.place_forget()
    tenPullButton.place_forget()

    root.mainloop()
"""
Program: Cryptid Hunter (CourtsBrookesM06_1.py)
Author: Brookes Courts
Last Date Modified: 01 December 2023
Cryptid Hunter is a text based Choose Your Own Adventure game that uses TKinter.
"""

# TKinter/Pillow Import
from tkinter import *
from PIL import ImageTk, Image

# startAdventure Button Command Function
def startAdventure():
   adventureLabel.config(text="Adventure started!")

# GUI setup
root = Tk()
root.title("Cryptid Hunter")

myImage = ImageTk.PhotoImage(Image.open("Start.png"))
imageLabel = Label(image=myImage)
imageLabel.pack()

startButton = Button(root, text="Click here to start your adventure!", command=startAdventure)
startButton.pack()

adventureLabel = Label(root, text="")
adventureLabel.pack()

root.mainloop()

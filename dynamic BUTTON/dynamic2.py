#import required libraries
import os
from tkinter import *
from tkinter import ttk

#Create an instance of Tkinter frame
win= Tk()

#Set the geometry of the window
win.geometry("800x800")

#Create a LabelFrame
labelframe= LabelFrame(win)

#Define a canvas in the window
canvas= Canvas(labelframe)
canvas.pack(side=RIGHT, fill=BOTH, expand=1)

labelframe.pack(fill= BOTH, expand= 1, padx= 10, pady=10)
img_folder_path = 'D:/NEW PROJECT/sacndat_studio/BotBees/xml files/'
dirListing = os.listdir(img_folder_path)

#Create Button widget in Canvas
for i in dirListing:
   ttk.Button(canvas, text= "" +str(i)).pack()

win.mainloop()
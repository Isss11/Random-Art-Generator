import math
from random import choice, randint, random, sample
from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk

from ArtGenerator import Picture

class ArtGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Art Generator")

        self.frame = ttk.Frame(self.root, padding="20")
        self.frame.grid(column=0, row=0, sticky=(N, W, E, S))
        self.root.columnconfigure(0, weight=1)
        # All of these previous lines of code are essentially setting up the frame and window, and how they dynamically resize
        self.root.rowconfigure(0, weight=1)

        self.createLabels()
        self.createInputWidgets()

    # Creates GUI Labels
    def createLabels(self):
        self.artLabel = ttk.Label(self.frame, text="Random Art Generator", font="helvetica 14 bold")
        self.artLabel.grid(column=0, row=0, sticky=N)
        
        self.squareSidesLabel = ttk.Label(self.frame, text="Number of Squares on Each Side", font="helvetica 10 bold")
        self.squareSidesLabel.grid(column=0, row=1, sticky= N)
        
        self.spacingTitle = ttk.Label(self.frame, text="Enter Factor of Spacing", font="helvetica 10 bold")
        self.spacingTitle.grid(column=0, row=4, sticky= N)

    # Creates Input Widgets and Canvas
    def createInputWidgets(self):
        
        # Degree of art squares
        # 1 means 1x1 grid, 3 means 3x3 grid, etc. 
        self.squareDegree = StringVar()

        self.squareDegreeScale = ttk.Scale(self.frame, orient=HORIZONTAL, length=200, from_=1, to=20, value=10, command=lambda s: self.squareDegree.set(math.floor(float(s))))
        self.squareDegreeScale.set(10)
        self.squareDegreeScale.grid(column=0, row=2, padx=20, sticky=N)

        self.squareSidesLabel = ttk.Label(self.frame, textvariable=self.squareDegree)
        self.squareSidesLabel.grid(column=0, row=3, sticky=N)

        self.squareSpacing = StringVar()
        
        self.spacingScale = ttk.Scale(self.frame, orient= HORIZONTAL, length = 200, from_=0.1, to=15, value=10, command=lambda t: self.squareSpacing.set(round(float(t), 2)))
        self.spacingScale.set(10)
        self.spacingScale.grid(column = 0, row=5, padx=20, sticky=N)

        # Creating a label to write out the value of the scale variable (self.degree)
        self.spacingValueText = ttk.Label(self.frame, textvariable=self.squareSpacing)
        self.spacingValueText.grid(column = 0, row= 6)

        self.generateArtButton = ttk.Button(self.frame, text="Create Artwork", command=lambda: self.create_art())
        self.generateArtButton.grid(row=13, column=0, ipady=10, ipadx=20, sticky=S)

        # Canvas
        self.cv = Canvas(self.frame, width=720, height=720, highlightbackground="gray21")
        self.cv.grid(row=0, column=1, rowspan=16)

    def create_art(self):
        self.generateArtButton.state(['disabled'])
        Picture(int(self.squareDegree.get()), float(self.squareSpacing.get()))
        
        photoimage = ImageTk.PhotoImage(file="funny.png")
        self.root.photoimage = photoimage
        self.cv.create_image((2, 2), image=photoimage, anchor=NW)
        self.generateArtButton.state(['!disabled'])

        

if __name__ == '__main__':
    root = Tk()
    ArtGenerator(root)

    root.mainloop()

from tkinter import *
from tkinter import ttk

class ArtGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Art Generator")

        self.frame = ttk.Frame(self.root, padding="5")
        self.frame.grid(column=0, row=0, sticky=(N, W, E, S))
        self.root.columnconfigure(0, weight = 1)
        self.root.rowconfigure(0, weight=1) #All of these previous lines of code are essentially setting up the frame and window, and how they dynamically resize

        self.drawInputWidgets() #this basically draws all the labels and input widgets needed to get user input to draw the random painting 

    def drawInputWidgets(self): #this was created to simplify __init__ by making it so that the input widgets would be put in another function for readability
        self.artLabel = ttk.Label(self.frame, text = "Random Art Generator", font= "helvetica 14 bold")
        self.artLabel.grid(column= 0, row = 0, columnspan= 4, ipadx=5, sticky=W)

        self.squareSidesLabel = ttk.Label(self.frame, text="Number of Squares on Each Side", font = "helvetica 10 bold")
        self.squareSidesLabel.grid(column = 0, row = 1, columnspan= 3) #setting up info labels

        #Now creating a scale to get user input on the amount of squares on each side
        self.squareSides = IntVar(value= 1)
        self.squareSidesScale = ttk.Scale(self.frame, orient=HORIZONTAL, length=100, from_=1.0, to= 5.0, variable= self.squareSides, command=self.intSquareSides)
        self.squareSidesScale.grid(column = 0, row = 2, ipady = 40)

        #Creating a label that posts the number of squares on each side
        self.squareSidesLabel = ttk.Label(self.frame, textvariable=self.squareSides)
        self.squareSidesLabel.grid(column = 0, row = 3, ipady = 10)

    def intSquareSides(self):
        self.squareSides = int(self.intSquareSides)
from tkinter import *
from tkinter import ttk
import math
from PIL import ImageGrab

class ArtGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Art Generator")

        self.frame = ttk.Frame(self.root, padding="20")
        self.frame.grid(column=0, row=0, sticky=(N, W, E, S))
        self.root.columnconfigure(0, weight = 1)
        self.root.rowconfigure(0, weight=1) #All of these previous lines of code are essentially setting up the frame and window, and how they dynamically resize

        self.drawInputWidgets() #this basically draws all the labels and input widgets needed to get user input to draw the random painting 

        self.artworkDimensions = [720, 720]
        self.artwork = Canvas(self.frame, width=self.artworkDimensions[0], height = self.artworkDimensions[1], background='gray75')
        self.artwork.grid(column=4, row = 0, sticky=(N, W, E, S), rowspan=24, padx= (40, 0))

        self.saveCanvasImage()

    def drawInputWidgets(self): #this was created to simplify __init__ by making it so that the input widgets would be put in another function for readability
        self.artLabel = ttk.Label(self.frame, text = "Random Art Generator", font= "helvetica 14 bold")
        self.artLabel.grid(column= 0, row = 0, columnspan= 4, padx=5)

        self.squareSidesLabel = ttk.Label(self.frame, text="Number of Squares on Each Side", font = "helvetica 10 bold")
        self.squareSidesLabel.grid(column = 0, row = 1, columnspan= 3, pady=15) #setting up info labels

        #Now creating a scale to get user input on the amount of squares on each side -- might need a lambda function to fix decimal issue
        self.squareSidesFloat = StringVar() #holding floats of numeric values
        self.squareSidesFloat.set('1')

        self.squareSidesScale = ttk.Scale(self.frame, orient=HORIZONTAL, length=200, from_=1, to= 20, value=1, command=lambda s: self.squareSidesFloat.set(math.floor(float(s)))) #learned a lot of that command from stackOverFlow (adjusted it a bit)
        self.squareSidesScale.grid(column = 0, row = 2, pady = 25, padx = 20, rowspan= 4)

        self.squareSidesLabel = ttk.Label(self.frame, textvariable= self.squareSidesFloat)
        self.squareSidesLabel.grid(column=0, row=6, pady=10, rowspan = 10) #added these rows at the end to space out the button a lot

        self.generateArtButton = ttk.Button(self.frame, text="Create Artwork")
        self.generateArtButton.grid(row = 16, column=0, pady = (200, 0), ipady = 10, ipadx = 20, rowspan=8) #trying to pad this a lot so  that we have a nice big space between the scale and button


"""
    def saveCanvasImage(self): #This function will be used to save the Tkinter canvas as an image
        x = self.root.winfo_rootx() + self.artwork.winfo_x()
        y = self.root.winfo_rooty() + self.artwork.winfo_y()
        x1 = x + self.artwork.winfo_width()
        y1 = y + self.artwork.winfo_height() #Getting the dimensions of the top left corner, then the bottom right corner of the canvas
        
        try:
            print(self.root.winfo_rootx(), self.artwork.winfo_x(), self.root.winfo_rooty(), self.artwork.winfo_y()) #FIXME screenshot actualy window
            print(x, y, x1, y1)
            artworkImage = ImageGrab.grab().save("test.jpg")
            
            #.crop((x, y, x1, y1)).save("test.jpg") #screenshots canvas
        except:
            print("Wrong file path input. Read the README for details.")
"""
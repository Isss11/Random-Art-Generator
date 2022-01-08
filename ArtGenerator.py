from tkinter import *
from tkinter import ttk
import math
from random import randint, random, sample, choice
from PIL import Image, ImageDraw, ImageTk, ImageColor, ImageGrab


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

        self.generateArtButton = ttk.Button(self.frame, text="Create Artwork", command=lambda: self.create_squares())
        self.generateArtButton.grid(row=15, column=0, ipady=10, ipadx=20, sticky=S)

        # Canvas
        self.cv = Canvas(self.frame, width=720, height=720, highlightbackground="gray49")
        self.cv.grid(row=0, column=1, rowspan=16)

        # Contains all images used in the artwork
        self.images = []

    # Creates the main squares of the artwork and calls create square art on them
    def create_squares(self):
        self.cv.delete('all')

        degree = int(self.squareDegree.get())
        spacing = float(self.squareSpacing.get())
        
        square_points = self.divide_square([[0, 0], [720, 720]], degree, spacing)

        for square in square_points:
            self.create_square_art(square)

    # Creates randomized art on any inputted square
    def create_square_art(self, square):

        self.add_triangle(square)
        self.add_semicircle(square)
        
        miniSquares = self.divide_square(square, 2)
        
        for miniSquare in miniSquares:
            if randint(1, 10) > 7:
                self.add_triangle(miniSquare)

    # Divides a given square into 'degree' pieces
    # Increase spacing to add space between squares, Decrease to add overlap
    def divide_square(self, square, degree, spacing=1):
        new_square_width = int(math.ceil(abs(square[0][0] - square[1][0])/(degree)))
        square_points = []
        for x in range(square[0][0], square[1][0], new_square_width):
            for y in range(square[0][1], square[1][1], new_square_width):
                square_points.append([[int(x+new_square_width/spacing), int(y+new_square_width/spacing)], [
                    int(x+new_square_width-new_square_width/spacing), int(y+new_square_width-new_square_width/spacing)]])

        return square_points

    # Creates an image of a polygon and places it on the canvas to allow alpha channels
    # https://stackoverflow.com/questions/62117203/how-to-make-a-tkinter-canvas-polygon-transparent
    def create_polygon(self, *args, **kwargs):
        if "alpha" in kwargs:
            if "fill" in kwargs:
                # Get and process the input data
                fill = self.root.winfo_rgb(kwargs.pop("fill"))\
                    + (int(kwargs.pop("alpha") * 255),)
                outline = kwargs.pop(
                    "outline") if "outline" in kwargs else None

                # We need to find a rectangle the polygon is inscribed in
                # (max(args[::2]), max(args[1::2])) are x and y of the bottom right point of this rectangle
                # and they also are the width and height of it respectively (the image will be inserted into
                # (0, 0) coords for simplicity)
                image = Image.new("RGBA", (max(args[::2]), max(args[1::2])))
                ImageDraw.Draw(image).polygon(args, fill=choice(
                    list(ImageColor.colormap.items()))[0], outline=outline)

                # prevent the Image from being garbage-collected
                self.images.append(ImageTk.PhotoImage(image))
                # insert the Image to the 0, 0 coords
                return self.cv.create_image(0, 0, image=self.images[-1], anchor="nw")
            raise ValueError("fill color must be specified!")
        return self.cv.create_polygon(*args, **kwargs)
    
    def create_arc(self, *args, **kwargs):
        if "alpha" in kwargs:
            if "fill" in kwargs:
                # Get and process the input data
                fill = self.root.winfo_rgb(kwargs.pop("fill")) + (int(kwargs.pop("alpha") * 255),)
                outline = kwargs.pop("outline") if "outline" in kwargs else None

                # We need to find a rectangle the polygon is inscribed in
                # (max(args[::2]), max(args[1::2])) are x and y of the bottom right point of this rectangle
                # and they also are the width and height of it respectively (the image will be inserted into
                # (0, 0) coords for simplicity)
                image = Image.new("RGBA", (max(args[::2]), max(args[1::2])))
                ImageDraw.Draw(image).arc(args, fill=choice(list(ImageColor.colormap.items()))[0], outline=outline)

                # prevent the Image from being garbage-collected
                self.images.append(ImageTk.PhotoImage(image))
                # insert the Image to the 0, 0 coords
                return self.cv.create_image(0, 0, image=self.images[-1], anchor="nw")
            raise ValueError("fill color must be specified!")
        return self.cv.create_arc(*args, **kwargs)

    # Adds a triangle on a random side or corner of a square 
    def add_triangle(self, square):
        # draw triangle randomly in the N, NE, E, ..., NW of a given square
        p1 = [square[0][0], square[0][1]]
        p2 = [square[1][0], square[0][1]]
        p3 = [square[0][0], square[1][1]]
        p4 = [square[1][0], square[1][1]]
        center = [int((square[0][0] + square[1][0]) / 2),
                  int((square[0][1] + square[1][1]) / 2)]

        points = [p1, p2, p4, p3, p1, p2]  # extra p1 and p2 allows easy looping

        p_start = randint(0, 3)

        if randint(0, 1):  # Corner triangle
            self.create_polygon(points[p_start][0],
                                points[p_start][1],
                                points[p_start + 2][0],
                                points[p_start + 2][1],
                                points[p_start + 1][0],
                                points[p_start + 1][1],
                                fill='#40E0D0',
                                alpha=random()
                                )
        else:  # Side Triangle
            self.create_polygon(points[p_start][0],
                                points[p_start][1],
                                center[0],
                                center[1],
                                points[p_start + 1][0],
                                points[p_start + 1][1],
                                fill='#40E0D0',
                                alpha=random()
                                )

    # Adds a semicircle/quartercircle to a random side or corner of a square
    def add_semicircle(self, square):
        p1 = [square[0][0], square[0][1]]
        p2 = [square[1][0], square[0][1]]
        p3 = [square[0][0], square[1][1]]
        p4 = [square[1][0], square[1][1]]
        
        points = [p1, p2, p4, p3, p1, p2]  # extra p1 and p2 allows easy looping
        p_start = randint(0, 3)

        if randint(0, 1): # Corner quarter circle
            self.create_arc(points[p_start][0],
                            points[p_start][1],
                            points[p_start + 2][0],
                            points[p_start + 2][1],
                            10, 70)
            
        else: # Side semi-circle
            pass

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

if __name__ == '__main__':
    root = Tk()
    ArtGenerator(root)

    root.mainloop()
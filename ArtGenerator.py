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
        self.artLabel.grid(column=0, row=0, columnspan=4, padx=5)
        
        self.squareSidesLabel = ttk.Label(self.frame, text="Number of Squares on Each Side", font="helvetica 10 bold")
        self.squareSidesLabel.grid(column=0, row=1, columnspan=3, pady=15)
        
        self.spacingTitle = ttk.Label(self.frame, text="Enter Factor of Spacing", font="helvetica 10 bold")
        self.spacingTitle.grid(column=0, row=8, columnspan=3, pady=15)

    # Creates Input Widgets and Canvas
    def createInputWidgets(self):
        
        # Degree of art squares
        # 1 means 1x1 grid, 3 means 3x3 grid, etc. 
        self.squareDegree = StringVar()

        self.squareDegreeScale = ttk.Scale(self.frame, orient=HORIZONTAL, length=200, from_=1, to=20, value=10, command=lambda s: self.squareDegree.set(math.floor(float(s))))
        self.squareDegreeScale.set(1)
        self.squareDegreeScale.grid(column=0, row=2, pady=(20, 0), padx=20)

        self.squareSidesLabel = ttk.Label(self.frame, textvariable=self.squareDegree)
        self.squareSidesLabel.grid(column=0, row=3, pady=10, rowspan=5)

        self.squareSpacing = StringVar()
        
        self.spacingScale = ttk.Scale(self.frame, orient= HORIZONTAL, length = 200, from_=0.1, to=15, value=10, command=lambda t: self.squareSpacing.set(round(float(t), 2)))
        self.spacingScale.set(10)
        self.spacingScale.grid(column = 0, row=9, pady= 10, rowspan=2)

        # Creating a label to write out the value of the scale variable (self.degree)
        self.spacingValueText = ttk.Label(self.frame, textvariable=self.squareSpacing)
        self.spacingValueText.grid(column = 0, row= 11, pady= 10)

        self.generateArtButton = ttk.Button(self.frame, text="Create Artwork", command=lambda: self.create_squares())
        self.generateArtButton.grid(row=16, column=0, pady=(200, 0), ipady=10, ipadx=20, rowspan=8)

        # Canvas
        self.cv = Canvas(self.frame, width=720, height=720, highlightbackground="gray49")
        self.cv.grid(row=0, column=4, rowspan=24)

        # Contains all images used in the artwork
        self.images = []

    def create_squares(self):
        self.cv.delete('all')

        degree = int(self.squareDegree.get())
        spacing = float(self.squareSpacing.get())
        
        square_points = self.divide_square([[0, 0], [720, 720]], degree, spacing)

        for square in square_points:
            # self.cv.create_rectangle(square[0][0], square[0][1], square[1][0], square[1][1], fill="blue")  # FOR TESTING ONLY

            self.create_square_art(square)

    def create_square_art(self, square):

        self.add_triangle(square)
        
        miniSquares = self.divide_square(square, 2)
        
        for miniSquare in miniSquares:
            self.add_triangle(miniSquare)

        #self.create_polygon(10, 10, 10, 20, 200, 300, 250, 150, 10, 10, fill="blue", alpha=0.5)

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

    def add_triangle(self, square):
        # draw triangle randomly in the N, NE, E, ..., NW of a given square
        p1 = [square[0][0], square[0][1]]
        p2 = [square[1][0], square[0][1]]
        p3 = [square[0][0], square[1][1]]
        p4 = [square[1][0], square[1][1]]
        center = [int((square[0][0] + square[1][0]) / 2),
                  int((square[0][1] + square[1][1]) / 2)]

        points = [p1, p2, p4, p3, p1, p2]  # extra p1 allows easy looping

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
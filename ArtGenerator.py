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

        # this basically draws all the labels and input widgets needed to get user input to draw the random painting
        self.drawInputWidgets()

    # this was created to simplify __init__ by making it so that the input widgets would be put in another function for readability

    def drawInputWidgets(self):
        self.artLabel = ttk.Label(
            self.frame, text="Random Art Generator", font="helvetica 14 bold")
        self.artLabel.grid(column=0, row=0, columnspan=4, padx=5)

        self.squareSidesLabel = ttk.Label(
            self.frame, text="Number of Squares on Each Side", font="helvetica 10 bold")
        # setting up info labels
        self.squareSidesLabel.grid(column=0, row=1, columnspan=3, pady=15)

        # Now creating a scale to get user input on the amount of squares on each side -- might need a lambda function to fix decimal issue
        self.squareSidesFloat = StringVar()  # holding floats of numeric values
        self.squareSidesFloat.set('1')

        self.squareSidesScale = ttk.Scale(self.frame, orient=HORIZONTAL, length=200, from_=1, to=20, value=1, command=lambda s: self.squareSidesFloat.set(
            math.floor(float(s))))  # learned a lot of that command from stackOverFlow (adjusted it a bit)
        self.squareSidesScale.grid(
            column=0, row=2, pady=25, padx=20, rowspan=4)

        self.squareSidesLabel = ttk.Label(
            self.frame, textvariable=self.squareSidesFloat)
        # added these rows at the end to space out the button a lot
        self.squareSidesLabel.grid(column=0, row=6, pady=10, rowspan=10)

        self.generateArtButton = ttk.Button(
            self.frame, text="Create Artwork", command=lambda: self.create_squares())
        # trying to pad this a lot so  that we have a nice big space between the scale and button
        self.generateArtButton.grid(row=16, column=0, pady=(
            200, 0), ipady=10, ipadx=20, rowspan=8)

        # Canvas
        self.cv = Canvas(self.frame, width=720, height=720)
        self.cv.grid(row=0, column=4, rowspan=24)

        self.images = []

    def create_squares(self):
        self.cv.delete('all')

        degree = int(self.squareSidesFloat.get())
        square_points = self.divide_square([[0, 0], [720, 720]], degree, 10)

        for square in square_points:
            # self.cv.create_rectangle(square[0][0], square[0][1], square[1][0], square[1][1], fill="blue")  # FOR TESTING ONLY

            self.create_square_art(square)

    def create_square_art(self, square):

        self.add_triangle(square)

        #self.create_polygon(10, 10, 10, 20, 200, 300, 250, 150, 10, 10, fill="blue", alpha=0.5)

    # Divides a given square into 'degree' pieces
    # Increase spacing to add space between squares, Decrease to add overlap
    def divide_square(self, square, degree, spacing=1):
        new_square_width = int(abs(square[0][0] - square[1][0])/(degree))
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

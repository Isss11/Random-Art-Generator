import math
import cairo
from random import *

class Picture:
    def __init__(self, degree, spacing):
        self.degree = degree
        self.spacing = spacing
        
        WIDTH, HEIGHT = 720, 720

        self.surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
        self.ctx = cairo.Context(self.surface)
        
        self.ctx.set_source_rgba(1, 1, 1, 0)
        self.ctx.paint()

        
        self.create_squares()
        
        self.surface.write_to_png("funny.png")  # Output to PNG
        
    def create_squares(self):
        square_points = self.divide_square([[0, 0], [720, 720]], self.degree, self.spacing)

        for square in square_points:
            self.create_square_art(square)

    # Creates randomized art on any inputted square
    def create_square_art(self, square):
        self.add_triangle(square)
        
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
        
        if randint(0, 1):
            self.ctx.set_source_rgba(random(), random(), random(), random())  # Solid color
            self.ctx.move_to(points[p_start][0],points[p_start][1])
            self.ctx.line_to(points[p_start + 2][0], points[p_start + 2][1])
            self.ctx.line_to(points[p_start + 1][0], points[p_start + 1][1])
            self.ctx.fill()
        else:  # Side Triangle
            self.ctx.set_source_rgba(random(), random(), random(), random())  # Solid color
            self.ctx.move_to(points[p_start][0], points[p_start][1])
            self.ctx.line_to(center[0], center[1])
            self.ctx.line_to(points[p_start + 1][0], points[p_start + 1][1])
            self.ctx.fill()

if __name__ == '__main__':
    Picture(3, 10)

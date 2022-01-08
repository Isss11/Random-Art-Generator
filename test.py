from tkinter import Tk, Frame, Canvas
from PIL import ImageTk

t = Tk()
t.title("Transparency")

frame = Frame(t)
frame.pack()

canvas = Canvas(frame, bg="black", width=500, height=500)
canvas.pack()

photoimage = ImageTk.PhotoImage(file="4b070e9.png")
canvas.create_image(0, 0, image=photoimage)

t.mainloop()
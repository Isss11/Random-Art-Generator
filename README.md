# GrandRiverRenegadesHackTheJob2022
This is the repository of team "Grand River Renegades" project at "Hack the Job" 2022.
## Random Art Generator
A random art generator created with python, tkinter, and pycario

### General Info

**Purpose**: The purpose was of this project is to make a random art generator with squares, filled with different shapes algorithmically and in the end connecting the pieces to create art. Each square has random shapes drawn within the constraints of itself, and they would all be drawn out with borders.

**Challenges**: One of the challenges that we encountered during the creation of the project was to algorithmically add the semi-circles or arc in the project. We were trying to add semi-circles at the borders of each individual square. However, Tkinter way of deploying shapes made it immensely challenging to create semi-circles along the edges and as a result, midway through the project one of our group members Micheal Janeway realized that instead of using Tkinter to draw shapes, we should use pycairo, which is another graphics library in python. From there he translated all of the code of Tkinter canvas code to pycairo and the problem was resolved. Furthermore, with using pycario, there was another problem resolved which was taking a screenshot of the art, which is another feature of this project as well. As there was not an efficient method with Tkinter to take a screenshot and another library was needed to be installed to take the screenshot of the random art. 

**Installation**:

```pip install pycairo```

```pip install --upgrade Pillow```

```pip install tk```

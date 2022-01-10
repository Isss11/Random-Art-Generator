![Banner](https://github.com/Isss11/GrandRiverRenegadesHackTheJob2022/blob/main/readme_files/readmeimage.png?raw=true)


# GrandRiverRenegadesHackTheJob2022
This is the repository of team "Grand River Renegades" project at "Hack the Job" 2022.
## Random Art Generator
A random art generator created with python, tkinter, pycario and Tcl themes.

### General Info

**Purpose**: This is a random art generator that develops mini-squares and fills them with different shapes (algorithmically). It then connects them all together in a visual array placed on a single image to create the final artpiece. 

![Banner](https://github.com/Isss11/GrandRiverRenegadesHackTheJob2022/blob/main/readme_files/readmeimage2.png?raw=true)
![randomArtGenerator_fullGUIImage](https://user-images.githubusercontent.com/89956249/148689583-83d0326a-15f6-4d81-a805-a2f6d1b12397.png)

**Challenges**: One of the challenges that we encountered during the creation of the project was to algorithmically add the semi-circles or arc in the project. We were trying to add semi-circles at the borders of each individual square. However, Tkinter's way of deploying shapes made it immensely challenging to create semi-circles along the edges of the mini-squares with Tkinter, so Michael changed the graphics library he was using (to create artwork) to pycairo. From there he translated all of the Tkinter canvas code to pycairo and the problem was resolved. Furthermore, pycairo resolved another problem having to do with getting an image of the art generated. Tkinter did not have a good method to take a screenshot and another library was needed to be installed to take the screenshot of the random art. On the GUI input side, there were many challenges with properly spacing out widgets and creating them (particularly the integer scale) with the constraints of ttk Tkinter.

**Installation**:

```pip install pycairo```

```pip install --upgrade Pillow```

**Having an Error With Installation?**: When installing the program by downloading the files as zip and extracting the folder you may encounter an error when running. If you do, it is probably because of an issue with Tcl themes that were used in the project. To solve this, go to https://github.com/rdbende/Sun-Valley-ttk-theme. Then download the contents of this repository as a zip, and paste the contents of the unzipped folder into the folder for this project. It should work after that.

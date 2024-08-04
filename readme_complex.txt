These are two small tools for visualizing complex functions, f:C->C. I made them to understand stuff like branch cuts and branch points better.

DomainColoring.py (Command line): 
The output of a complex function at any point in the complex plane is represented by a colour.
The darkness of a point/pixel represents magnitude - black for 0 and white for infinity.
The hue of the color represents the argument - red for 0 degrees.
'lumdropoff' should be >1. Default is 1.07. If it is increased, complex numbers of large magnitude turn white faster.
The function to plot, w=f(z), can be specified in line 43.
Running the code results in a png file output, which includes a picture of the domain coloring of both the domain and the image space, for reference.


ComplexPlotter.py (Graphical interface):
This visualizes complex functions in a different way.
Two canvases are shown on screen, for the domain and image space.
The function to plot can be specified in the window itself (from a textbox). You can choose between a f:C->C or a f:R^2->R^2 definition for the function.
You can click and drag your cursor in the domain space canvas. Let the position of your cursor be z. Then a dot will appear in the image space canvas at f(z), and will move appropriately as your cursor moves.
The scale/zoom can also be adjusted for either canvas.

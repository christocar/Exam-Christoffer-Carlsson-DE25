import matplotlib.pyplot as plt
from circle import Circle
from rectangle import Rectangle

class Shape2DPlotter:
    """A class to plot 2D shapes like circles and rectangles using matplotlib."""

    def __init__(self):
        """Initialize the plotter with a matplotlib figure and axis."""
        self.fig, self.ax = plt.subplots()
        self.ax.set_aspect('equal', 'box')
        self.ax.grid(True)

    def plot_circle(self, circle: Circle, color: str = 'blue'):
        """
        Plot a circle on the axis.

        Args:
            circle (Circle): The circle to plot.
            color (str): The color of the circle.
        """
        circle_patch = plt.Circle((circle.x, circle.y), circle.radius, color=color, fill=False)
        self.ax.add_patch(circle_patch)
        self.ax.set_xlim(circle.x - circle.radius - 1, circle.x + circle.radius + 1)
        self.ax.set_ylim(circle.y - circle.radius - 1, circle.y + circle.radius + 1)

    def plot_rectangle(self, rectangle: Rectangle, color: str = 'red'):
        """
        Plot a rectangle on the axis.

        Args:
            rectangle (Rectangle): The rectangle to plot.
            color (str): The color of the rectangle.
        """
        rect_patch = plt.Rectangle((rectangle.x, rectangle.y), rectangle.width, rectangle.height, 
                                   edgecolor=color, fill=False)
        self.ax.add_patch(rect_patch)
        self.ax.set_xlim(rectangle.x - 1, rectangle.x + rectangle.width + 1)
        self.ax.set_ylim(rectangle.y - 1, rectangle.y + rectangle.height + 1)

    def show(self):
        """Display the plot."""
        plt.show()
import matplotlib.pyplot as plt
from circle import Circle
from rectangle import Rectangle
from shape2d import Shape2D

class Shape2DPlotter:
    """A class to plot 2D shapes like circles and rectangles using matplotlib."""

    def __init__(self):
        """Initialize the plotter with a matplotlib figure and axis."""
        self.fig, self.ax = plt.subplots()
        self.ax.set_aspect('equal', 'box')
        self.ax.grid(True)
        self.shapes = []  # collection of shapes

    def add_shape(self, shape):
        """Add a 2D shape to internal storage for later plotting."""
        if not isinstance(shape, Shape2D):
            raise TypeError("Only 2D shapes can be added to Shape2DPlotter.")
        self.shapes.append(shape)

    def plot_circle(self, circle: Circle, color: str = 'blue'):
        """
        Plot a circle on the axis.

        Args:
            circle (Circle): The circle to plot.
            color (str): The color of the circle.
        """
        circle_patch = plt.Circle((circle.x, circle.y), circle.radius, color=color, fill=False, linewidth=3)
        self.ax.add_patch(circle_patch)

    def plot_rectangle(self, rectangle: Rectangle, color: str = 'red'):
        """
        Plot a rectangle on the axis.

        Args:
            rectangle (Rectangle): The rectangle to plot.
            color (str): The color of the rectangle.
        """
        rect_patch = plt.Rectangle((rectangle.x, rectangle.y), rectangle.width, rectangle.height,
                                   edgecolor=color, fill=False, linewidth=3)
        self.ax.add_patch(rect_patch)

    def plot_all(self):
        """Plot all stored shapes in one figure using default colors, then set unified limits."""
        if not self.shapes:
            print("No 2D shapes to plot.")
            return

        # 1) draw all shapes
        for shape in self.shapes:
            if isinstance(shape, Circle):
                self.plot_circle(shape)
            elif isinstance(shape, Rectangle):
                self.plot_rectangle(shape)

        # 2) compute a unified bounding box covering ALL shapes
        min_x = float('inf')
        max_x = float('-inf')
        min_y = float('inf')
        max_y = float('-inf')

        for shape in self.shapes:
            if isinstance(shape, Circle):
                cx, cy, r = shape.x, shape.y, shape.radius
                min_x = min(min_x, cx - r)
                max_x = max(max_x, cx + r)
                min_y = min(min_y, cy - r)
                max_y = max(max_y, cy + r)
            elif isinstance(shape, Rectangle):
                rx, ry, rw, rh = shape.x, shape.y, shape.width, shape.height
                min_x = min(min_x, rx)
                max_x = max(max_x, rx + rw)
                min_y = min(min_y, ry)
                max_y = max(max_y, ry + rh)

        # 3) add a small padding and apply once
        width = max_x - min_x
        height = max_y - min_y
        if width == 0:
            width = 1.0
        if height == 0:
            height = 1.0
        pad = 0.1 * max(width, height)

        self.ax.set_xlim(min_x - pad, max_x + pad)
        self.ax.set_ylim(min_y - pad, max_y + pad)

    def show(self):
        """Display the plot."""
        plt.show()

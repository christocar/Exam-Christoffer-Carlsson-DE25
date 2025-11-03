"""
Main menu module for creating and working with 2D and 3D shapes.
User can create shapes, view information, move shapes and plot all 2D shapes.
This file connects all classes together and provides the interaction layer.
Some parts of this structure were improved with help from ChatGPT (OpenAI, 2025).
"""

from circle import Circle
from rectangle import Rectangle
from cube import Cube
from sphere import Sphere
from shape2dplotter import Shape2DPlotter


def create_shape():
    print("Choose shape type:")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Cube")
    print("4. Sphere")

    choice = input("Select 1–4: ")

    try:
        if choice == "1":
            x = float(input("x-position: "))
            y = float(input("y-position: "))
            r = float(input("radius: "))
            return Circle(r, x, y)

        elif choice == "2":
            x = float(input("x-position: "))
            y = float(input("y-position: "))
            w = float(input("width: "))
            h = float(input("height: "))
            return Rectangle(w, h, x, y)

        elif choice == "3":
            x = float(input("x-position: "))
            y = float(input("y-position: "))
            z = float(input("z-position: "))
            s = float(input("side length: "))
            return Cube(s, x, y, z)

        elif choice == "4":
            x = float(input("x-position: "))
            y = float(input("y-position: "))
            z = float(input("z-position: "))
            r = float(input("radius: "))
            return Sphere(r, x, y, z)

        else:
            print("Invalid choice.")
            return None

    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
        return None


def show_shape_info(shape):
    print("--- Shape information ---")
    print(shape)

    # 2D shapes
    if hasattr(shape, "perimeter"):
        print(f"Area: {shape.area:.2f}")
        print(f"Perimeter: {shape.perimeter:.2f}")

    # 3D shapes
    else:
        print(f"Surface area: {shape.surface_area:.2f}")
        print(f"Volume: {shape.volume:.2f}")


def move_shape(shape):
    print("Move shape:")

    # 2D shapes
    if hasattr(shape, "perimeter"):
        dx = float(input("dx: "))
        dy = float(input("dy: "))
        shape.translate(dx, dy)

    # 3D shapes
    else:
        dx = float(input("dx: "))
        dy = float(input("dy: "))
        dz = float(input("dz: "))
        shape.translate(dx, dy, dz)

    print("Shape moved:")
    print(shape)


def main():
    shapes = []
    while True:
        print("--- MENU ---")
        print("1. Create new shape")
        print("2. Show all shapes")
        print("3. Move a shape")
        print("4. Plot 2D shapes")
        print("5. Exit")

        val = input("Choose: ")

        if val == "1":
            shape = create_shape()
            if shape:
                shapes.append(shape)
                show_shape_info(shape)

        elif val == "2":
            if not shapes:
                print("No shapes created yet.")
            else:
                for i, s in enumerate(shapes, 1):
                    print(f"{i}. {s}")

        elif val == "3":
            if not shapes:
                print("No shapes to move.")
            else:
                for i, s in enumerate(shapes, 1):
                    print(f"{i}. {s}")
                index = int(input("Which shape number to move: "))
                if 1 <= index <= len(shapes):
                    move_shape(shapes[index - 1])
                else:
                    print("Invalid number.")

        elif val == "4":
            shapes_2d = [s for s in shapes if hasattr(s, "perimeter")]
            if not shapes_2d:
                print("No 2D shapes to plot.")
            else:
                plotter = Shape2DPlotter()
                for s in shapes_2d:
                    plotter.add_shape(s)
                plotter.plot_all()
                plotter.show()

        elif val == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()

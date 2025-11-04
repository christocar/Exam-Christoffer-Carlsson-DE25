# Geometry OOP Project

## Overview
This project is an object-oriented Python application designed to model and visualize 2D and 3D geometric shapes. It allows the user to:
- Create and manage shapes such as **circles**, **rectangles**, **cubes**, and **spheres**
- Calculate **area**, **perimeter**, and **volume**
- **Translate (move)** shapes in space
- **Compare** shapes by area or volume
- **Plot** 2D shapes (circles and rectangles) using `matplotlib`
- Test all functionalities using `pytest`

The program was built as part of a lab in object-oriented programming (OOP), focusing on inheritance, encapsulation, abstraction, and polymorphism.

## Class Structure
Shape2D (abstract)  
├── Circle  
└── Rectangle  

Shape3D (abstract)  
├── Cube  
└── Sphere  

Shape2DPlotter (visualization utility)  
Utils (validation helper)  
main.py (menu and interaction logic)  
tests/ (pytest files)

## UML Planning
Before implementation, the system was carefully planned using a UML class diagram. This helped visualize the relationships between classes, inheritance structure, and method responsibilities.

The diagram includes:
- Abstract base classes for 2D and 3D shapes
- Specific shape implementations like `Circle`, `Rectangle`, `Cube`, and `Sphere`
- Utility classes for validation and plotting
- Associated test classes for each shape

### UML Diagram
![UML Diagram](./uml_diagram/Lab2UML.png)

## File Overview
| File | Description |
|------|--------------|
| `shape2d.py` | Abstract base class for all 2D shapes |
| `circle.py` | Implements Circle (inherits from Shape2D) |
| `rectangle.py` | Implements Rectangle (inherits from Shape2D) |
| `shape3d.py` | Abstract base class for all 3D shapes |
| `cube.py` | Implements Cube (inherits from Shape3D) |
| `sphere.py` | Implements Sphere (inherits from Shape3D) |
| `shape2dplotter.py` | Plots 2D shapes using matplotlib |
| `utils.py` | Contains validation methods for numeric and positive values |
| `main.py` | The main program with an interactive text-based menu |
| `test_circle.py` | Unit tests for Circle |
| `test_rectangle.py` | Unit tests for Rectangle |
| `test_cube.py` | Unit tests for Cube |
| `test_sphere.py` | Unit tests for Sphere |

## How to Run the Program
1. Make sure you have Python **3.10 or later** installed.  
2. Install dependencies (matplotlib and pytest):  
```bash
pip install matplotlib pytest
```  
3. Run the program:  
```bash
python main.py
```  
4. Follow the on-screen menu to create and manipulate shapes:  
```
--- MENU ---
1. Create a new shape
2. Show all shapes
3. Move a shape
4. Plot 2D shapes
5. Exit
```

## How to Run Tests
Run all test files:  
```bash
pytest
```  
Run a single test file:  
```bash
pytest test_circle.py -v
```  

Each test file verifies:
- Initialization and validation
- Area, perimeter, and volume calculations
- Translation and comparison logic
- String representations (`__str__`, `__repr__`)

## Object-Oriented Design Principles
| Concept           | Implementation                                                                             |
| ----------------- | ------------------------------------------------------------------------------------------ |
| **Encapsulation** | Attributes like `_x`, `_y`, `_radius` are protected.                                       |
| **Inheritance**   | 2D shapes inherit from `Shape2D`, 3D shapes from `Shape3D`.                                |
| **Abstraction**   | `Shape2D` and `Shape3D` define abstract methods (`area`, `volume`, `translate`).           |
| **Polymorphism**  | Shared method names (`translate`, `__eq__`, `__lt__`) behave differently in each subclass. |

## Visualization
Shape2DPlotter uses matplotlib to display 2D shapes:
- Circles are drawn in blue.
- Rectangles are drawn in red.
- Labels and gridlines are added automatically.

Example:
```python
from circle import Circle
from rectangle import Rectangle
from shape2dplotter import Shape2DPlotter

shapes = [Circle(0, 0, 2), Rectangle(1, 1, 3, 2)]
plotter = Shape2DPlotter(shapes)
plotter.plot()
```

## Utils Module
The `utils.py` file provides reusable validation methods:
```python
Utils.validate_number(value)
Utils.validate_positive(value)
```
These are used in constructors to ensure all input values are numeric and positive.

## Testing Philosophy
All test files use pytest and follow a clear naming convention:
- Each method name starts with `test_`
- Each method tests one specific behavior
- Descriptive docstrings are included in every test file

This makes it easy to extend or modify the code safely.

## LLM Assistance Statement
Some parts of this code and documentation were created or refined with the help of ChatGPT (OpenAI, 2025).  
All code has been reviewed, understood, and tested manually before submission.  
The purpose of using AI assistance was to improve clarity, documentation, and structure.

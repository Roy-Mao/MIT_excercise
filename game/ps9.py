# 6.00 Problem Set 9
#
# Name:
# Collaborators:
# Time:

from string import *
shapes_file = open('shapes.txt', 'r')

class Shape(object):
    def area(self):
        raise AttributeException("Subclasses should override this method.")

class Square(Shape):
    def __init__(self, h):
        """
        h: length of side of the square
        """
        self.side = float(h)
    def area(self):
        """
        Returns area of the square
        """
        return self.side**2
    def __str__(self):
        return 'Square with side ' + str(self.side)
    def __eq__(self, other):
        """
        Two squares are equal if they have the same dimension.
        other: object to check for equality
        """
        return type(other) == Square and self.side == other.side

# Problem 1: Create the Triangle class
#
## TO DO: Implement the `Triangle` class, which also extends `Shape`.

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = float(base)
        self.height = float(height)
    def area(self):
        return (self.base * self.height) // 2
    def __str__(self):
        return 'Triangle with base ' + str(self.base) + ' and height ' + str(self.height)
    def __eq__(self, other):
        return type(other) == Triangle and self.base == other.base and self.height == other.height

class Circle(Shape):
    def __init__(self, radius):
        """
        radius: radius of the circle
        """
        self.radius = float(radius)
    def area(self):
        """
        Returns approximate area of the circle
        """
        return 3.14159*(self.radius**2)
    def __str__(self):
        return 'Circle with radius ' + str(self.radius)
    def __eq__(self, other):
        """
        Two circles are equal if they have the same radius.
        other: object to check for equality
        """
        return type(other) == Circle and self.radius == other.radius


#
# Problem 2: Create the ShapeSet class
#
## TO DO: Fill in the following code skeleton according to the
##    specifications.

class ShapeSet(Shape):
    def __init__(self):
        """
        Initialize any needed variables
        """
        ## TO DO
        self.shapes = []
    def addShape(self, sh):
        """
        Add shape sh to the set; no two shapes in the set may be
        identical
        sh: shape to be added
        """
        ## TO DO
        if not sh in self.shapes:
            self.shapes.append(sh)


    def __iter__(self):
        """
        Return an iterator that allows you to iterate over the set of
        shapes, one shape at a time
        """
        ## TO DO
        return iter(self.shapes)
    def __str__(self):
        """
        Return the string representation for a set, which consists of
        the string representation of each shape, categorized by type
        (circles, then squares, then triangles)
        """
        ## TO DO
        rep = ''
        for sh in self.shapes:
            rep = rep + sh.__str__() + '\n'
        return rep


my_Triangle = Triangle(5,5)


ss = ShapeSet()
ss.addShape(Triangle(3,8))
ss.addShape(Circle(1))
ss.addShape(Triangle(4,6))
 

        
#
# Problem 3: Find the largest shapes in a ShapeSet
#
def findLargest(shapes):
    """
    Returns a tuple containing the elements of ShapeSet with the
       largest area.
    shapes: ShapeSet
    """
    ## TO DO
    maxVal = 0
    Length = len(shapes.shapes)
    Largest = 0
    alist = []
    for item in shapes.shapes:
        if item.area() >= maxVal:
            maxVal = item.area()
            Largest = maxVal
    for item in shapes.shapes:
        if item.area() == maxVal:
            alist.append(item)
    atuple = tuple(alist)

    return atuple



# Problem 4: Read shapes from a file into a ShapeSet
#
def readShapesFromFile(filename):
    """
    Retrieves shape information from the given file.
    Creates and returns a ShapeSet with the shapes found.
    filename: string
    """
    ## TO DO
    mySet = ShapeSet()
    for line in filename:
        cleanLine = line.strip()
        cleanLine = cleanLine.split(',')
        if cleanLine[0] == 'circle':
            radius = float(cleanLine[1])
            circle = Circle(radius)
            mySet.addShape(circle)
        elif cleanLine[0] == 'square':
            side = float(cleanLine[1])
            square = Square(side)
            mySet.addShape(square)
        else:
            base = float(cleanLine[1])
            height = float(cleanLine[2])
            triangle = Triangle(base, height)
            mySet.addShape(triangle)

    print mySet

 
readShapesFromFile(shapes_file)

#Blessing Gijima R247779H
#Assignment 2

#Question 1

# Base class
class Vehicle:
    def move(self):
        print("This vehicle can move.")

class Car(Vehicle):
    def move(self):
        print("The car drives on the road.")
class Bike(Vehicle):
    def move(self):
        print("The bike rides on two wheels.")

v = Vehicle()
c = Car()
b = Bike()

# Call the methods
v.move()
c.move()
b.move()


#Question 2

import math

# Base class
class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

def total_area(shapes):
    total = 0
    for shape in shapes:
        total += shape.area()
    return total

# Example use
shapes = [
    Circle(5),
    Rectangle(4, 6),
    Circle(3)
]

print("Total area of all shapes:", total_area(shapes))


#question 3

# Base class
class Shape:
    def __init__(self):
        print("Shape constructor called")

    def calculate_area(self):
        pass

# Derived class
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def calculate_area(self):
        super().__init__()
        area = self.length * self.width
        print(f"Rectangle area: {area}")
        return area

rect = Rectangle(5, 3)
rect.calculate_area()

#Question 4

# Function that works with any object having make_sound()
def process_sound(sound_object):
    sound_object.make_sound()

# Dog class
class Dog:
    def make_sound(self):
        print("Woof! Woof!")

# Cat class
class Cat:
    def make_sound(self):
        print("Meow! Meow!")

dog = Dog()
cat = Cat()

process_sound(dog)
process_sound(cat)

#Question 5

from abc import ABC, abstractmethod

# Abstract base class
class FileHandler(ABC):

    @abstractmethod
    def read(self, filename):
        pass

    @abstractmethod
    def write(self, filename, data):
        pass


# Concrete class for handling text files
class TextFileHandler(FileHandler):

    def read(self, filename):
        with open(filename, 'r') as file:
            content = file.read()
        print("Reading from text file:")
        return content

    def write(self, filename, data):
        with open(filename, 'w') as file:
            file.write(data)
        print("Writing to text file complete.")

class BinaryFileHandler(FileHandler):

    def read(self, filename):
        with open(filename, 'rb') as file:
            content = file.read()
        print("Reading from binary file:")
        return content

    def write(self, filename, data):
        with open(filename, 'wb') as file:
            file.write(data)
        print("Writing to binary file complete.")


# Example use case
if __name__ == "__main__":
    # Text file example
    text_handler = TextFileHandler()
    text_handler.write("example.txt", "Hello, this is a text file.")
    print(text_handler.read("example.txt"))

    # Binary file example
    binary_handler = BinaryFileHandler()
    binary_handler.write("example.bin", b"\x48\x65\x6C\x6C\x6F")  # "Hello" in hex
    print(binary_handler.read("example.bin"))

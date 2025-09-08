class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        return f"Starting {self.brand} {self.model}"


class Car(Vehicle):
    def start_engine(self):
        return f"Car {self.brand} {self.model} engine started with a purr"


class Bike(Vehicle):
    def start_engine(self):
        return f"Bike {self.brand} {self.model} engine started with a roar"


# Test Question 1
print("Question 1:")
car = Car("Toyota", "Camry")
bike = Bike("Honda", "CBR")
print(car.start_engine())
print(bike.start_engine())
print()

# Question 2: Polymorphism with Shapes

import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


def calculate_total_area(shapes):
    total = 0
    for shape in shapes:
        total += shape.calculate_area()
    return total


# Test Question 2
print("Question 2:")
shapes = [Circle(5), Rectangle(4, 6), Circle(3)]
total_area = calculate_total_area(shapes)
print(f"Total area: {total_area:.2f}")
print()


# Question 3: Using super() function

class Shape:
    def __init__(self, name):
        self.name = name
        print(f"Shape {name} created")

    def calculate_area(self):
        print("Base calculate_area called")
        return 0


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def calculate_area(self):
        super().calculate_area()  # Call parent method
        area = self.width * self.height
        print(f"Rectangle area: {area}")
        return area


# Test Question 3
print("Question 3:")
rect = Rectangle(5, 8)
rect.calculate_area()
print()


# Question 4: Polymorphism with Dog and Cat

class Dog:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return f"{self.name} says Woof!"


class Cat:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return f"{self.name} says Meow!"


def process_sound(sound_object):
    return sound_object.make_sound()


# Test Question 4
print("Question 4:")
dog = Dog("Buddy")
cat = Cat("Whiskers")
print(process_sound(dog))
print(process_sound(cat))
print()

# Question 5: Abstract Base Classes

from abc import ABC, abstractmethod


class FileHandler(ABC):
    def __init__(self, filename):
        self.filename = filename

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass


class TextFileHandler(FileHandler):
    def read(self):
        return f"Reading text from {self.filename}"

    def write(self, data):
        return f"Writing text '{data}' to {self.filename}"


class BinaryFileHandler(FileHandler):
    def read(self):
        return f"Reading binary data from {self.filename}"

    def write(self, data):
        return f"Writing binary data to {self.filename}"


# Test Question 5
print("Question 5:")
text_handler = TextFileHandler("document.txt")
binary_handler = BinaryFileHandler("image.jpg")

print(text_handler.read())
print(text_handler.write("Hello World"))
print(binary_handler.read())
print(binary_handler.write("binary data"))
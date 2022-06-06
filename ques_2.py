"""
                                    Abstract Classes
An abstract class can be considered as a blueprint for other classes. It allows you to create a set
of methods that must be created within any child classes built from the abstract class.
By defining an abstract base class, you can define a common Application Program Interface(API)
for a set of subclasses.
"""
from abc import ABC, abstractmethod


class Polygon(ABC):

    @abstractmethod
    def noofsides(self):
        pass


class Triangle(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 3 sides")


class Pentagon(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 5 sides")


class Hexagon(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 6 sides")


class Quadrilateral(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 4 sides")


R = Triangle()
R.noofsides()
K = Quadrilateral()
K.noofsides()
R = Pentagon()
R.noofsides()
K = Hexagon()
K.noofsides()

"""
                                    Multiple Inheritance
hen a class is derived from more than one base class it is called multiple Inheritance. 
The derived class inherits all the features of the base case.
"""


class Class1:
    def m(self):
        print("In Class1")


class Class2(Class1):
    def m(self):
        print("In Class2")


class Class3(Class1):
    def m(self):
        print("In Class3")


class Class4(Class2, Class3):
    pass


obj = Class4()
obj.m()

"""
                                    Decorators
Decorators are a very powerful and useful tool in Python since it allows programmers to modify 
the behaviour of function or class. Decorators allow us to wrap another function in order to 
extend the behaviour of the wrapped function, without permanently modifying it.
"""


def hello_decorator(func):
    def inner1(*args, **kwargs):
        print("before Execution")

        # getting the returned value
        returned_value = func(*args, **kwargs)
        print("after Execution")

        # returning the value to the original frame
        return returned_value

    return inner1


# adding decorator to the function
@hello_decorator
def sum_two_numbers(a, b):
    print("Inside the function")
    return a + b


a, b = 1, 2

# getting the value through return of the function
print("Sum =", sum_two_numbers(a, b))
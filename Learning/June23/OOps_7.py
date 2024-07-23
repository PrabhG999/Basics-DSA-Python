"""
7. Method Overloading
Python does not support method overloading by default. However,
you can achieve similar functionality using default arguments or variable-length arguments.

Question: Create a class MathOperations with a method add that can add two or three numbers.


"""


class MathOperations:
    def add(self, a, b, c=0):
        return a + b + c


math = MathOperations()
print(math.add(1, 2))
print(math.add(3, 4, 7))

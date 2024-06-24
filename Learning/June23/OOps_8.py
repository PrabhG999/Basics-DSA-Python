"""
8. Static Methods
Question: Create a class Utility with a static method is_even that checks if a number is even.


"""


class EvenCheck:
    @staticmethod
    def is_even(number):
        return number % 2 == 0


print(EvenCheck.is_even(5))
print(EvenCheck.is_even(10))

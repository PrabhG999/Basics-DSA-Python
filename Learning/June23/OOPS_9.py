"""
9. Class Methods
Question: Create a class Book with a class variable total_books.
Create a class method increment_books to increase the count of total books.
"""


class Book:

    total_books = 0
    def __init__(self):
        Book.total_books+=1

    @classmethod
    def increment_books(cls,count):
        cls.total_books+= count




"""1. Class and Object
Question: Create a class Person with attributes name and age.
Create an object of this class and print the name and age of the person."""


class Person:
    def __init__(self, name, age):  # constructor 
        self.name = name
        self.age = age


person = Person('Kabir', 25)  ##object of person class
print(person.name)
print(person.age)

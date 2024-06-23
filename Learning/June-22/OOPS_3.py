"""3. Inheritance
Question: Create a base class Animal with a method make_sound. Create a derived class Dog that overrides the make_sound method.

Hint: Use the super() function to call the constructor of the base class."""


class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name


class Dog(Animal):
    def make_sound(self):
        print('woof')


animal = Dog('Bob')
animal.make_sound()
print(animal.name)

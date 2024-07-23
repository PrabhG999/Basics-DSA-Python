# Class and objects

class Animal:
    # base class
    # constructor
    def __init__(self, petName, petAge, petGender):
        self.petName = petName
        self.petAge = petAge
        self.petGender = petGender

    # function
    def animalSpeak(self):
        print('the animal speaks')


class Dog(Animal):
    def animalSpeak(self):
        print('woof')


class Cat(Animal):
    def animalSpeak(self):
        print('meow')


dog = Dog('hero', 2, 'male')
dog.animalSpeak()

cat = Cat('cat', 2, 'female')
cat.animalSpeak()

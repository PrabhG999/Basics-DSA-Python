class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return 'Woof!'


class Cat(Animal):
    def speak(self):
        return 'Meow!'


def make_animal_speak(animal):
    print(animal.speak())


my_dog = Dog()
my_cat = Cat()

make_animal_speak(my_dog)
make_animal_speak(my_cat)

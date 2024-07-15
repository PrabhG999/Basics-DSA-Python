from abc import ABC, abstractmethod

class Animal(ABC):  # Inherit from ABC
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return 'Woof'

class Cat(Animal):
    def speak(self):
        return 'Meow'

class Sonali(Animal):
    def speak(self):
        return 'Hello'
dog = Dog()
cat = Cat()
human = Sonali()

print(cat.speak())  # This will print: Meow
print(dog.speak())  # This will print: Woof
print(human.speak())

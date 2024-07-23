"""5. Abstraction
Question: Create an abstract class Vehicle with an abstract method start_engine. Create a derived class Car that implements the start_engine method.

"""
from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass


class Car(Vehicle):
    def start_engine(self):
        print("Vehicle has been started.")


car = Car()
car.start_engine()

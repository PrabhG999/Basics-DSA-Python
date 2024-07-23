class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print('bow bow')

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age


my_dog = Dog('Sonali Rahul Sil',25)
my_dog.speak()
my_dog.set_name('Sonali Makker')
print(my_dog.get_name())
my_dog.set_age(26)
print(my_dog.get_age())

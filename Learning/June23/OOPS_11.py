class Student:
    def __init__(self, name, age):
        self.name = name  # __ makes it private variable
        self.__age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.__age


student1 = Student('John', 23)
print(student1.name)  # 2 examples of printing names
print(student1.get_name())

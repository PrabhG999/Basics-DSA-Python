""""6. Method Overriding
Question: Create a base class Employee with a method get_salary that returns a fixed salary.
 Create a derived class Manager that overrides the get_salary method to include a bonus."""


class Employee:
    def get_salary(self):
        return 5000


class Manager(Employee):

    def get_salary(self):
        bonus = 1000
        base_salary = super().get_salary() + bonus

        return base_salary


manager = Manager()

print(manager.get_salary())

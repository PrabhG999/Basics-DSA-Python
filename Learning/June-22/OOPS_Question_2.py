"""
2. Encapsulation
Question: Create a class BankAccount with a private attribute balance. Provide methods to deposit and withdraw money,
 and to check the balance.

Hint: Use double underscores __ to make the attribute private."""


class BankAccount:
    def __init__(self, initial_balanace):
        self.__balance = initial_balanace

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def get_balance(self):
        return self.__balance


bannkAcc = BankAccount(1000)

bannkAcc.deposit(100)
bannkAcc.withdraw(200)

print(bannkAcc.get_balance())

class Rahul:
    def __init__(self, name):
        self.name = name

    def account_balance(self):
        pass


class Sonali(Rahul):
    def account_balance(self):
        will = 20000
        return (will / 2)


class Ujjuwal(Rahul):
    def account_balance(self):
        will = 20000
        return (will / 2)


sonali = Sonali('sonali')
print(sonali.account_balance())

ujjuwal = Ujjuwal('ujjuwal')
print(ujjuwal.account_balance())

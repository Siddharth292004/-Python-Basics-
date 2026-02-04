class BankAccount:
    def __init__(self):
        self.__balance = 5000   # private variable

    def show_balance(self):
        print("Balance:", self.__balance)

    def deposit(self, amount):
        self.__balance += amount


acc = BankAccount()
acc.show_balance()
acc.deposit(1000)
acc.show_balance()


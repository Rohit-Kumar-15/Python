# 02 - Attributes, Methods, and self

class BankAccount:
    def __init__(self, owner, balance):
        # Instance attributes: each object has its own values
        # simiral as pointer or -> arrow symbol inc++
        self.owner = owner
        self.balance = balance

    # Instance method: works with the current object through self
    #self refers to  teh current object
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit must be positive.")
            return
        self.balance += amount
        print(f"Deposited {amount}")

    def show_balance(self):
        print(f"{self.owner}'s balance: {self.balance}")

account1 = BankAccount("Asha", 1000)
account2 = BankAccount("Ravi", 500)

account1.deposit(250)
account1.show_balance()
account2.show_balance()



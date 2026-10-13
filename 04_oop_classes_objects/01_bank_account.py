class BankAccount:
    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
        else:
            self.balance += amount
            print(f"{amount} deposit successfully!")    

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance")
        elif amount <= 0:
            print("Invalid amount")    
        else:
            self.balance -= amount
            print(f"{amount} Withdrawn successfully")

    def check_balance(self):
        print("Balance = ", self.balance)                


account1 = BankAccount(5644288, "Roger", 48000)

account1.deposit(20000)
account1.withdraw(14000)
account1.check_balance()




    
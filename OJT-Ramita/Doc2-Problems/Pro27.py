'''27. Write a class that represents a bank account, do bank operations.'''

class Bank():
    def __init__(self, customer_name, account_num, funds):
        self.customer_name = customer_name
        self.account_num = account_num
        self.funds = funds

    def show_Balance(self):
        print("Avaialable Funds:",self.funds)
    
    def show_Acccount_Number(self):
        print("Account Number:", self.account_num)

    def withdraw(self, amount):
        if amount < self.funds:
            self.funds -= amount
            print(amount,"debited successfully...")
        else:
            print("Insufficient Funds!")
    
    def deposit(self, amount):
        self.funds += amount
        print(amount, "credited successfully...")

obj = Bank("Mr.Ramesh Gosai", 24424400, 1000)
obj.show_Balance()
obj.withdraw(700)
obj.show_Balance()
obj.deposit(5000)
obj.show_Balance()


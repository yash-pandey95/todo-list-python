class ATM:
    def __init__(self,name,bank_balance):
        self.name = name
        self.bank_balance = bank_balance
    def show_balance(self):
        print(f"Bank Balance: {self.bank_balance}")
    def deposit(self,deposit_amount):
        self.bank_balance +=  deposit_amount
        print("Deposite successful")
    def withdraw(self,withdraw_amount) :
        if withdraw_amount <= self.bank_balance:
            self.bank_balance -= withdraw_amount
            print("Withdraw Successful")
        else:
            print("Insufficeint Balance !")
    
    
p1 = ATM("Tony",1200000)
p1.deposit(500000)
p1.show_balance()  
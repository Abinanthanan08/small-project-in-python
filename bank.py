class account:
    def __init__(self,holder_name,initial_balance=0):
        self.holder_name=holder_name
        self.balance=initial_balance

    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print("Deposit amount is",amount,"\nNew balance is",self.balance)

        else:
            print("Deposit process is faild")


    def withdraw(self,amount):
        if amount>0:
            if amount<=self.balance:
                self.balance-=amount
                print("Withdraw amount is",amount,"\nNew balance is",self.balance)

        else:
             print("Insufficient balance")


    """def check_balance(self):
        return self.balance"""


    def display(self):
        print("Holder_name:",self.holder_name)
        print("balance:",self.balance)


x=account("ram",15000)
x.deposit(500)
x.withdraw(250)
x.display()
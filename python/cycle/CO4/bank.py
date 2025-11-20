class Account:
    def __init__(self,acc_no,name,acc_type,balance):
        self.acc_no=acc_no
        self.name=name
        self.acc_type=acc_type
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print(f"{amount} is successfully deposited!")

    def withdraw(self,amount):
        if(amount>self.balance):
            print(f"Insufficient balance!")
        else:
            self.balance-=amount
            print(f"{amount} is successfully withdrawed!")
    def display(self):
        print(f"account no:{self.acc_no}\t name:{self.name}\t account type:{self.acc_type} \t balance:{self.balance}")
        
account_no = int(input("enter the account number:"))
account_type = input("enter the account type:")
name = input("enter the name:")

member = Account(account_no,name,account_type,0)

while True:
    member.display()
    transaction = int(input("enter 1 to deposit , enter 2 to withdraw , enter 0 to exit"))
    if transaction == 1:
        member.deposit(int(input("enter the amount: ")))
    elif transaction == 2:
        member.withdraw(int(input("enter the amount: ")))
    elif transaction == 0:
        exit()

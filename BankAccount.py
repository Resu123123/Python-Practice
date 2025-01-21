class BankAccount:
    def __init__(self):
        self.balance = 0
        print("Welcome to ATM!!")

    def deposit(self):
        amount = int(input("Enter amount to be Deposit: "))
        self.balance += amount
        print("\nAmount Deposited:",amount)

    def withdraw(self):
        withdraw = int(input("\nEnter amount to be Withdrawn: "))
        if self.balance >= withdraw:
            self.balance -= withdraw
            print("\nAmount withdrawn is:",withdraw)
        else:
            print("\nInsufficient Balance ") 

    def display(self):
        print("\nAvailable Balance" , self.balance)

s = BankAccount()
s.deposit()
s.withdraw()
s.display()       

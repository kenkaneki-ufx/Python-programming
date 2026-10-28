# □ Login using Account Number
# □ File Saving
# □ PIN Protection

# Create Account -> Deposit -> Withdraw -> Check Balance -> Accounts History
import random
import time
import os
# import datetime  

class Bank:
    #choices
    def __init__(self,choice):
        self.name = input("Enter your Account name: ")
        if choice == 1:
            self.create_acc(self.name)
        elif choice == 2:
            self.deposit()
        elif choice == 3:
            self.withdraw()
        elif choice == 4:
            self.get_balance()
        elif choice == 5:
            self.acc_history()
        else:
            print("Please enter valid option")
        

    # 1 [ Creating a new account ]
    def create_acc(self,name):
        self.name = name
        self.acc_no = random.choice(range(1000,100000))
        try:
            with open(f"Bank/{self.name}.txt","r") as f:
                pass
        except FileNotFoundError:
            print("Connecting to the Bank server..")
            time.sleep(0.5)
            print("Creating your Account...")
            time.sleep(1)
            print(f"{'-'*30}\nYour account has been created...!")
            print(f"Account Name: {self.name}\nAccount no.: {self.acc_no}\n{'-'*20}")
            try:
                with open(f"Bank/{self.name}bal.txt","w") as f:
                    f.write('0')  # creates a tem current balance fur further updation
            except:
                os.mkdir("Bank")   # This is when User Run this for first time
                with open(f"Bank/{self.name}bal.txt","w") as f:  
                    f.write('0')
            with open(f"Bank/{self.name}.txt","w") as f:
                f.write(f"{'-'*21}\nAccount Name:\t{self.name}\nAccount no.:\t{self.acc_no}\n{'-'*21}\nTRANSACTION HISTORY\n{'-'*21}")
            with open(f"Bank/01_Bank_accounts.txt","a") as f:   # creates a file of new account
                f.write(f"\nAccount Name:\t{self.name}\nAccount no.:\t{self.acc_no}\n{'-'*21}")
        else:
            print("Account already exits..")
            

    # 2 [ Depositing money to account ]
    def deposit(self):
        try:
            with open(f"Bank/{self.name}bal.txt","r") as f:
                self.balance = float(f.read())
        except FileNotFoundError:
            print("Your account Doesn't exist.\nCreate new account ?")
        else:
            amount = float(input("Enter your deposit amount $: "))
            if amount <= 0:
                print("Invalid Deposit Amount..")
            else:
                self.balance += amount
                time.sleep(1)
                print(f"${amount} deposited Sucessfully..")
            with open(f"Bank/{self.name}bal.txt","w") as f:
                f.write(f"{self.balance}")  # updates the tem balance
            with open(f"Bank/{self.name}.txt","a") as f:   # adds the transaction history of deposit
                f.write(f"\n${amount} amount has been Deposited.\tCurrent balancee: ${self.balance}")


    # 3 [ Withdrawing money from account ]
    def withdraw(self):
        try:
            with open(f"Bank/{self.name}bal.txt","r") as f:
                self.balance = float(f.read())
        except FileNotFoundError:
            print("Your account Doesn't exist.\nCreate new account ?")
        else:
            amount = float(input("Enter your withdrawal amount $: "))
            if amount > self.balance and amount<=0:
                print("Invalid Withdrawal Amount..")
            else:
                self.balance = self.balance - amount
                time.sleep(1)
                print(f"${amount} Withdraw Sucessfully..")
            with open(f"Bank/{self.name}bal.txt","w") as f:
                f.write(f"{self.balance}")  # updates the tem balance
            with open(f"Bank/{self.name}.txt","a") as f:   # adds the transaction history of withdraw
                f.write(f"\n${amount} amount has been Withdrawed.\tCurrent balance: ${self.balance}")
            

    # 4 [ Display current balance ]
    def get_balance(self):
        try:
            with open(f"Bank/{self.name}bal.txt","r") as f:
                time.sleep(0.5)
                print(f"Your current balance is: ${f.read()}")
        except FileNotFoundError:
            print("Your account Doesn't exist.\nCreate new account ?")
        time.sleep(2)


    # 5 [ Display Transaction hisory ]
    def acc_history(self):
        try:
            with open(f"Bank/{self.name}.txt","r") as f:
                time.sleep(0.5)
                print(f.read())
        except FileNotFoundError:
            print("Your account Doesn't exist.\nCreate new account ?")
        time.sleep(2)


while True:
    # [ Main menu ]
    time.sleep(0.5)
    print(f"{'-'*20}\nWelcome to ABC Bank\n{'-'*20}")
    time.sleep(0.5)
    print(f"1.Create Account.\n2.Deposit Money.\n3.Withdraw Money.\n4.Check Balance.\n5.Transaction history.\n{'-'*20}")
    time.sleep(0.5)
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Oops...Inalid choice")
        time.sleep(2)
        continue
    Bank(choice)

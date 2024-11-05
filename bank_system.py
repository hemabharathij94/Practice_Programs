class Bank:
    def __init__(self):
        self.account={}
    
    def create_account(self,account_number,account_holder,initial_balance,password):
        if account_number in self.account:
            return "Account Already Exists."
        if initial_balance < 0:
            return "Initial Balance must be Non-negative"
        self.account[account_number]={
            "Account_Holder":account_holder,
            "Balance":initial_balance,
            "Password":password
        }
        return "Account Created Successfully."
    
    def Deposite(self,account_number,amount,password):
        if account_number not in self.account:
            return "Account does not Exists."
        if amount < 0:
            return "Amount to deposite must be positive"
        if self.account[account_number]["Password"] != password:
            return "Incorrect password"
        self.account[account_number]["Balance"]+=amount
        return "Deposite: " + str(amount) + "Successfully. New Balance: " + str(self.account[account_number]["Balance"])
    
    def Withdraw(self,account_number,amount,password):
        if account_number not in self.account:
            return "Account does not Exists."
        if amount <= 0:
            return "Amount t0 Withdraw must be positive"
        if self.account[account_number]["Password"] != password:
            return "Incorrect Password"
        if self.account[account_number]["Balance"] < amount:
            return "Insufficient Balance"
        self.account[account_number]["Balance"]-=amount
        return "Withdraw: " + str(amount) + "Successfully. New Balance: " + str(self.account[account_number]["Balance"])
    
    def Check(self,account_number,password):
        if account_number not in self.account:
            return "Account does not Exists."
        if self.account[account_number]["Password"] != password:
            return "Incorrect Password"
        return "Account Holder:" + self.account[account_number]["Account_Holder"] + "\nBalance: " + str(self.account[account_number]["Balance"])
bank=Bank()
print("\n*****Bank Management System*****")
print("\n1. Create Account")
print("2. Deposite")
print("3. Withdraw")
print("4. Check Balance")
print("5. Exit")
while True:
    choice=input("\nEnter the choice (1 to 5): ")
    
    if choice == "1":
        account_number=input("Enter the Account Number: ")
        account_holder=str(input("Enter the Account Holder's Name: "))
        initial_balance=float(input("Enter the Initial Balance: "))
        password=input("Enter the Password: ")
        result=bank.create_account(account_number,account_holder,initial_balance,password)
        print(result)
    
    elif choice == "2":
        account_number=input("Enter the Account Number: ")
        amount=float(input("Enter Amount of Deposite: "))
        password=input("Enter the Password: ")
        result=bank.Deposite(account_number,amount,password)
        print(result)

    elif choice == "3":
        account_number=input("Enter the Account Number: ")
        amount=float(input("Enter Amount of Withdraw: "))
        password=input("Enter the Password: ")
        result=bank.Withdraw(account_number,amount,password)
        print(result)

    elif choice == "4":
        account_number=input("Enter the Account Number: ")
        password=input("Enter the Password: ")
        result=bank.Check(account_number,password)
        print(result)

    elif choice == "5":
        print("Existing the Program.")
        break

    else:
        print("Invalid Choice.Please Try Again !!!")
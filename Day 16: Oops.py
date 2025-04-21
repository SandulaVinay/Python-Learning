# Defining a class named BankAccount
class BankAccount:
    
    # Constructor method to initialize the object's data
    def __init__(self, account_number, holder_name, balance):
        # 'self' refers to the current object being created
        # 'account_number', 'holder_name', and 'balance' are passed as arguments during object creation
        self.account_number = account_number  # Assigning account number to the object
        self.holder_name = holder_name        # Assigning account holder name
        self.balance = balance                # Assigning initial balance

    # Method to deposit amount into the bank account
    def deposit(self, amount):
        self.balance += amount  # Increase the current balance by the deposited amount
        print(f"{self.holder_name} Deposited {amount}. New Balance: {self.balance}")  # Show updated balance

    # Method to withdraw amount from the bank account
    def withdraw(self, amount):
        # Check if there is enough balance to withdraw
        if amount <= self.balance:
            self.balance -= amount  # Subtract the amount from balance
            print(f"{self.holder_name} Withdrawn {amount}. Remaining Balance: {self.balance}")  # Show updated balance
        else:
            print(f"{self.holder_name}, Insufficient balance.")  # Show error if balance is not sufficient

    # Method to display current balance
    def display_balance(self):
        print(f"{self.holder_name}'s Account Balance: {self.balance}")  # Print current balance

# ✅ Creating an object for State Bank of India account
State_Bank_of_India = BankAccount(2424, "Sid", 32423)  # Object creation, calling __init__

# Performing transactions on State_Bank_of_India object
State_Bank_of_India.deposit(1000)        # Calling deposit method to add 1000
State_Bank_of_India.withdraw(100)        # Calling withdraw method to remove 100
State_Bank_of_India.display_balance()    # Display the final balance

# ✅ Creating another object for HDFC Bank account
HDFC_Bank = BankAccount(6543, "Anil", 100000)  # Object creation

# Performing transactions on HDFC_Bank object
HDFC_Bank.deposit(25000)               # Add 25000 to balance
HDFC_Bank.withdraw(10000)             # Withdraw 10000 from balance
HDFC_Bank.display_balance()           # Show remaining balance

Sid Deposited 1000. New Balance: 33423
Sid Withdrawn 100. Remaining Balance: 33323
Sid's Account Balance: 33323

Anil Deposited 25000. New Balance: 125000
Anil Withdrawn 10000. Remaining Balance: 115000
Anil's Account Balance: 115000

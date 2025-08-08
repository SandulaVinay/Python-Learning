from logic import Bank #Bank is a single class we can create multiple objects like below banks
from Ac_Holders_Data import Account_Holders

check = False
while check is True:

    Axis_Bank_Customer1 = Bank(1234, 'vinay', 'AXIS0100', 1000)
    Axis_Bank_Customer3 = Bank(6546, 'varma', 'AXIS0100', 0)

    Axis_Bank_Customer1.Account_Details()
    Axis_Bank_Customer1.Money_Withdraw(1200)    

    Axis_Bank_Customer3.Account_Details()
    Axis_Bank_Customer3.Money_Withdraw(100)

    ICICI_Bank_Cust1 = Bank(8440, 'Krish', 'ICICI001', 2500)
    ICICI_Bank_Cust2 = Bank(8441, 'Ganesh', 'ICICI001', 100)

    ICICI_Bank_Cust1.Account_Details()
    ICICI_Bank_Cust1.Money_Withdraw(100)

    ICICI_Bank_Cust2.Account_Details()
    ICICI_Bank_Cust2.Money_Withdraw(100)

    SBI_Bank_Cust1 = Bank(6156, 'Varun', 'SBI', 220)
    SBI_Bank_Cust1.Money_Deposit(1)

while True:
    print("\n1.Add Account \n2.Show Accounts \n3.Exit")
    choice = input("Enter Choice:")

    if choice == '1':
        acc_no = int(input("Please enter account No: "))
        Name = input("Please enter your Name: ")
        IFSCCODE = input("Please enter Bank IFSCCODE: ")
        amount = float(input("Please enter amount: "))

        Bank.Add_NewAccount(acc_no, Name, IFSCCODE, amount) 
        print(f"You account successfully added {Name} ")
        print(f"Account No:{acc_no}, Name:{Name}, IFSCCODE:{IFSCCODE}, Amount: {amount}")
    
    elif choice == '2':
        for acc in Account_Holders.values():
            acc.Account_Details()

    elif choice == '3':
        print("Thank you! ")
        break
    
    else:
        print("Invalid Input")





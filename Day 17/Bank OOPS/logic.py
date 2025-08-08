from Ac_Holders_Data import Account_Holders

class Bank:
    def __init__(self, AccountNo, AccountName, IFSCCODE, Balance):
        self.AccountNo = AccountNo
        self.AccountName = AccountName
        self.IFSCCODE = IFSCCODE
        self.Balance = Balance

    @staticmethod                                           #Using @staticmethod lets you call Add_Account without first creating a dummy Bank object.
    def Add_NewAccount(AccountNo, Name, IFSCCODE,
                        amount):
        if AccountNo in Account_Holders:
            print("Account Number already exists.")
        else:
            new_customer = Bank(AccountNo, Name, IFSCCODE, amount)
            Account_Holders[AccountNo] = new_customer

    def Account_Details(self):
        print(f"Account No: {self.AccountNo}")
        print(f"Account Name: {self.AccountName}")
        print(f"IFSC Code: {self.IFSCCODE}")
        print(f"Balance: {self.Balance}\n")

    def Money_Withdraw(self, amount):
        if amount > self.Balance:
            print("Not Sufficient Balance Available\n")
        else:
            self.Balance -= amount
            print(f"Amount {amount}/- has been withdrawn from account {self.AccountNo}")
            print(f"Available Balance: {self.Balance}\n")

    def Money_Deposit(self, amount):
        self.Balance += amount
        print(f"Amount {amount}/- deposited. Available Balance: {self.Balance}\n")

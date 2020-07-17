#bank=>ac.no,ac-type,person name,balance
#account-create
#deposit
#withdraw
#balance enquiry
##############
#different types of vaariable
#instance variable instance means related to object

#local variables
#class or static variable
class Bank:
    bankname = "SBI"
    def Account_create(self,account_no,account_type,name):
        self.account_no=account_no
        self.accoount_type=account_type
        self.name=name
        self.balance=3000


    def Deposit(self,amount):
        self.balance+=amount
        print("your",self.bankname,"has been credited with amount ",amount)

    def Withdraw(self,wamount):
        if(wamount>self.balance):
            print("insufficient balance and transaction is cancelled")
        else:
            self.balance-=wamount
            print("your",self.bankname,"has been debited with amount ",amount)

    def Balance_Enquiry(self):
        print("current balance is",self.balance)
    def printValues(self):
        print(Bank.bankname)

b=Bank()
b.Account_create(100,"savings","das")
#b.Deposit(10000)
#b.Withdraw(5000)
b.Balance_Enquiry()
b.printValues()
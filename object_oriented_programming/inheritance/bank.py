
class Person:
    def setPerson(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address


class Bank(Person):
    bankname = "SBI"
    def Account_create(self,account_no,account_type):
        self.account_no=account_no
        self.accoount_type=account_type
        self.balance=3000


    def Deposit(self,amount):
        self.balance+=amount
        print("your",self.bankname,"has been credited with amount ",amount)

    def Withdraw(self,wamount):
        if(wamount>self.balance):
            print("insufficient balance and transaction is cancelled")
        else:
            self.balance-=wamount
            print(self.name,"your",Bank.bankname,"has been debited with amount ",wamount)

    def Balance_Enquiry(self):
        print("current balance is",self.balance)
    def printValues(self):
        print(Bank.bankname)

b=Bank()
b.setPerson("jini",28,"address")
b.Account_create(100,"savings")
#b.Deposit(10000)
b.Withdraw(2000)
b.Balance_Enquiry()
b.printValues()
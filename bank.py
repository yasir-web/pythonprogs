"""Banking solution
1.Create an account
2. Deposit the amount
3. Withdraw the amount
4. Balance enquiry"""
class bank:
    def createaccount(self,acno,name,balance):
        self.acno=acno
        self.name=name
        self.balance=balance
    def deposit(self,acno,amt):
        if self.acno==acno:
            self.balance=self.balance+amt
            print("The amount",amt,"is credited in your account")
        else:
            print("The account does not exist")
    def withdraw(self,acno,amt):
        if self.acno==acno:
            if self.balance>=amt:
                self.balance=self.balance-amt
                print("The amount",amt,"is debited from your account")
            else:
                print("Unsufficient balance")
        else:
            ("The account does not exist")
    def enquiry(self,acno):
        if self.acno==acno:
            print("The balance amount=",self.balance)
        else:
            print("The account does not exist")
#Now we test the class
acno=int(input("Enter account number: "))
name=input("Enter account holder name: ")
balance=int(input("Enter opening balance: "))
b=bank()
b.createaccount(acno,name,balance)
print("Your accont is created")
ch=0
while ch!=4:
    print("1 --> Deposit")
    print("2 --> Withdraw")
    print("3 --> Enquiry")
    print("4 --> Exit")
    ch=int(input())
    if ch==1:
        acno=int(input("Enter account no.: "))
        amt=int(input("Enter amount to deposit: "))
        b.deposit(acno,amt)
    elif ch==2:
        acno=int(input("Enter aacount no.: "))
        amt=int(input("Enter amount to withdraw: "))
        b.withdraw(acno,amt)
    elif ch==3:
        acno=int(input("Enter account no.: "))
        b.enquiry(acno)
    elif ch==4:
        pass
    else:
        print("Invalid choice")
            
                
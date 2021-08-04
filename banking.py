
import random
class UserDirectory:
    details={}
    def deposit(self,accNum,addMoney):
        self.details[accNum]['deposit']=self.details[accNum]['deposit']+addMoney
    def withdraw(self,accNum,deductMoney):
        self.details[accNum]['deposit']=self.details[accNum]['deposit']-deductMoney   
class NewUser(UserDirectory): 
    def __init__(self,name,money):
        self.name=name
        self.money=money
    def addUser(self):
        accNum=random.randint(0, 99999)
        print(accNum)
        print(self.details)
        self.details[accNum]={'name':self.name,'deposit':self.money}
        print(self.details)
    @staticmethod
    def welcome():
        print("Welcome") 
    def displayUsers(self):
        print(self.details)
        print("User details")

print("Press 1 if new user")
print("Press 2 if existing user")
print("Press 3 to quit")
ex=UserDirectory()
while True:
    choice=int(input("Enter your choice"))
    if choice==1:
        name=input("Enter the name")
        deposit=float(input("Enter the deposit to open account with"))
        user=NewUser(name,deposit)
        user.addUser()
        user.welcome()
        user.displayUsers()
        print(UserDirectory.details)
    elif choice==2:
        name=input("Enter the name")
        accNum=int(input("Enter the account number"))
        if accNum in UserDirectory.details.keys():
            print("Press 1 to display balance")
            print("Press 2 to deposit")
            print("Press 3 to withdraw")
            ch=int(input("Enter your choice"))
            if ch==1:
                print("Account number is")
                print(ex.details[accNum])
            if ch==2:
                addMoney=float(input("Enter the amount to deposit"))
                ex.deposit(accNum,addMoney)
                print(ex.details[accNum]['deposit'])
            if ch==3:
                deductMoney=float(input("Enter the amount to deposit"))
                ex.deposit(accNum,deductMoney)
                print(ex.details[accNum]['deposit'])
    elif choice==3:
        quit()




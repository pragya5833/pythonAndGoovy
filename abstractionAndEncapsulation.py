class Library:
    # display,lend,add books
    def __init__(self,listOfbooks):
        self.listOfbooks=listOfbooks
    def displayBooks(self):
        for i in range(0,len(self.listOfbooks)):
            print(self.listOfbooks[i])
    def lendbooks(self,requestedbook):
        if requestedbook in self.listOfbooks:
            print("you have now borrowed the book")
            self.listOfbooks.remove(requestedbook)
        else:
            print("book unavailable")

    def addbooks(self,returnedbook):
        self.listOfbooks.append(returnedbook)
        
    

class Customer:
    #request and return books
    def borrow(self):
        self.borrowing=input("Enter the book you want to borrow")
        return self.borrowing
    def returned(self):
        self.returning=input("Name of book returning")
        return self.returning
l1=Library(['art of the day','day to remember','subtle art'])
c1=Customer()
print("1 to display books")
print("2 to request a book")
print("3 to return a book")
print("4 to exit")

while True:
    userChoice=int(input("Enter your choice"))
    if userChoice==1:
        l1.displayBooks()
    elif userChoice==2:
        borr=c1.borrow()
        l1.lendbooks(borr)
    elif userChoice==3:
        ret=c1.returned()
        l1.addbooks(ret)
    elif userChoice==4:
        quit()


# instance methods are methods in class used to get or modify instance attributes
# static methods dont take self param, they do this by making use of decorator staticmethod, it ignores the binding
# decorators are functions that take other functions and extend their functionality
class Employee:
    def Empdetails(self):
        self.name="Joey"
    @staticmethod
    def welcomeMsg():
        print("Welcome to our organization")
e1=Employee()
e1.Empdetails()
print(e1.name)
e1.welcomeMsg()

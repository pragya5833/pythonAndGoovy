class Employee:
    #default work Hours
    numberOfWorkingHours=45
    def __init__(self,name,designation,salesMade):
        self.name=name
        self.designation=designation
        self.salesMade=salesMade
    @staticmethod
    def welcome():
        print("Welcome To Our Organization")
    def printDetails(self):
        print(self.name)
    def totalWorkHours(self):
        print("Total working Hours")
        print(self.numberOfWorkingHours*5)
e1=Employee("Joey","sales",6)
e1.welcome()
e1.printDetails()
e1.totalWorkHours()
e2=Employee("Matt","sales1",4)
e2.welcome()
e2.printDetails()
e2.numberOfWorkingHours=40
e2.totalWorkHours()
e1.age=22
print(e1.age)
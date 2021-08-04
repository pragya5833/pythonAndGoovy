class Employee:
    # class attribute common to all instances or objects defined in class and accessed in class using self. and from outside using classname.
    workingHours=10
    def totalweekHours(self):
        print(self.workingHours*5)
e1=Employee()
print(Employee.workingHours)
e1.totalweekHours()
# instanceAttribute
e1.name="Joey"
print(e1.name)
#checks first instance attribute with name and then the class attribute
e1.workingHours=5
e1.totalweekHours()

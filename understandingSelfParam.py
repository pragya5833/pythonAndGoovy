class Employee:
    def totalWork(self):
        self.name="Matt"
        print("attribute name of object is", self.name)
        # we use self.attribute when we want the attribute to be linked to object
        # throughout it's lifespan
        # lifespan of object: creation to destruction of object
        # or manually delete object
        age=30
        print("Age= ",age)
    def printDetails(self):
        print(self.name)
        # in this case we get name 'age' not defined error bcz life span of age was within the function it was declared
        #print("age= ", age)


e=Employee()
#ways to call method
e.totalWork()
#or
Employee.totalWork(e)
# as we are passing an argument which is the object , parameter must be defined in function hence self
e.printDetails()
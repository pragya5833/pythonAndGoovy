class Employee:
    name="Joey"
    designation="sales"
    salesMade= 6
    def targetAchieved(self):
        if self.salesMade>=5:
            print("Target Acheived")
        else:
            print("Not acheived")
e=Employee()
print(e.name)
e.targetAchieved()
# class name-> noun
# attributes -> adjectives
# actions that can be performed -> verbs
# class is a blue print
# object is instance of class
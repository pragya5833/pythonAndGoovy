class Employee:
    def initializeWorkHours(self):
        self.numberOfWorkHours=45
    def displayWorkHours(self):
        print(self.numberOfWorkHours)
class Trainee(Employee):
    def initializeWorkHours(self):
        self.numberOfWorkHours=40
    def resetWorkHours(self):
        super().initializeWorkHours()
e=Employee()
t=Trainee()
e.initializeWorkHours()
e.displayWorkHours()
t.initializeWorkHours()
t.displayWorkHours()
t.resetWorkHours()
t.displayWorkHours()

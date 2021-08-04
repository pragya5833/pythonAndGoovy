# class Car:
#     def __init__(self,choice):
#         self.choice=choice
#     def costOfCar(self):
#         if self.choice==1:
#             return 30
#         elif self.choice==2:
#             return 50
#         elif self.choice==3:
#             return 100

class Cost:
    def __init__(self,costOfCar):
        self.costOfCar=costOfCar
    def totalCost(self):
        self.days=int(input("Enter of days to borrow the car for"))
        print("Total cost is :") 
        print(self.days*self.costOfCar)

print("Enter 1 for Hetchback")
print("Enter 2 for sedan")
print("Enter 3 for SUV")
print()
while True:
    choice=int(input("Enter the choice of car"))
    if choice==4:
        quit()
    elif choice==1:
        cost=Cost(30)
        cost.totalCost()
    elif choice==2:
        cost=Cost(50)
        cost.totalCost()
    elif choice==3:
        cost=Cost(100)
        cost.totalCost(100)

    



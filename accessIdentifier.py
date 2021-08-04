class Car:
    #public member , accessible to all
    numOfwheels=4
    #protected member, accessible to class and its derived classes
    _color="Black"
    #private member, accessible to only class
    __yearModel=2017
class BMW(Car):
    def __init__(self):
        print("Car has {} and is {} color".format(self.numOfwheels,self._color))
car=BMW()
car1=Car()
# Name mangling 
print(car1._Car__yearModel)
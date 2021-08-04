class A:
    def method(self):
        print("This method is executed from A class")
class B(A):
    def method(self):
        print("This method is executed from B class")
class C(A):
    def method(self):
        print("This method is executed from C class")
#B method will be taken , if C was written before B then from B would be executed
class D(B,C):
    pass
a=A()
a.method()
d=D()
d.method()
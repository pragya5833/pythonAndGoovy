class Square:
    def __init__(self,side):
        self.side=side
    def __add__(sq1,sq2):
        return ((4*sq1.side)+(4*sq2.side))
sq1=Square(5)
sq2=Square(10)
print(sq1+sq2)

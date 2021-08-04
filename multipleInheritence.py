class Opsystem:
    multiTask=True
    name="Mac OS"
class Apple:
    website="www.appleInc.com"
    name="Maccing"
class Macbook(Opsystem,Apple):
    def __init__(self):
        if self.multiTask is True:
            print(self.website)
            print(self.name)
mac=Macbook()

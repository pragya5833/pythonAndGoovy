class Apple:
    manufacturer="Apple Inc"
    contactWebsite="www.apple.com"
    def contactDetails(self):
        print("Please contact us on {}".format(self.contactWebsite))
class Macbook(Apple):
    def __init__(self):
        self.yearOfManufacture=2017
    def manufacturer(self):
        print("Manufactured by {} in {} and contact us {}".format(self.manufacturer,self.yearOfManufacture,self.contactDetails))
mac=Macbook()
mac.manufacturer()
mac.contactDetails()   
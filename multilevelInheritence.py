class Musicalinstruments:
    numberOfkeys=12
class stringInstruments(Musicalinstruments):
    typeOfwood="Teak"
class Guitar(stringInstruments):
    def __init__(self):
        self.numberOfStrings=6
        print("Consists of {} number of keys, made of {} and has {} strings".format(self.numberOfkeys,self.typeOfwood,self.numberOfStrings))
ins=Guitar()
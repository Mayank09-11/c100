class Student(object):
    def __init__(self,cardnumber,pinnumber):
        self.cardnumber = cardnumber
        self.pinnumber=pinnumber
    
    def cardnumber(self, number, cardnumber):
        self.cardnumber[number] = cardnumber

    def pinnumber(self, number):
        return self.pinnumber[number]

    def getGPA(self):
        return sum(self.pinnumber.number())/len(self.pinnumber)

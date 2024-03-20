from Helpers import *

class MotherCollection:
    def __init__(self, filename):
        inFile = Helpers.removeHeader(open(filename, 'r', encoding='utf-8'))
        self._mothers = []
        for line in inFile:
            mothersData = line.rstrip().split(", ")
            if len(mothersData) != 1:                                       
                self._mothers.append(mothersData)
    
    def setMothers(self, mothers):
        self._mothers = mothers

    def getMothers(self):
        return self._mothers

    #string
    def __str__(self):
        
        return f'{self.getMothers()}'
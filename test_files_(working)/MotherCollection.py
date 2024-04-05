from Mother import Mother
from Helper import Helper

class MotherCollection:
    """
    Mother collection class
    """
    def __init__(self, filename):
        self._filename = filename
        self._header, self._mothersData = Helper().readFile(self.getFilename())
        self._mothers = []
        for data in self.getMothersData():
            name, age, tagColour, riskLevel = data
            mother = Mother(name, age, tagColour, riskLevel)
            self._mothers.append(mother)

    # setters
    def setHeader(self, header):
        self._header = header

    def setMothersData(self, mothersData):
        self._mothersData = mothersData

    def setMothers(self, mothers):
        self._mothers = mothers

    # getters
    def getFilename(self):
        return self._filename
    
    def getHeader(self):
        return self._header

    def getMothersData(self):
        return self._mothersData
    
    def getMothers(self):
        return self._mothers

    # sorting mother's list by the keys from the Mother class
    def sortMothers(self):
        self.getMothers().sort(key = Mother.sortMothersKeys)
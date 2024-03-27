from Mother import *

class MotherCollection:
    def __init__(self, filename):
        self._filename = filename
        self._header, self._mothersData = self.readFile()
        self._mothers = []
        for data in self.getMothersData():
            name, age, tagColour, riskLevel = data
            mother = Mother(name, age, tagColour, riskLevel)
            self._mothers.append(mother)

    def getFilename(self):
        return self._filename

    def readFile(self):
        with open(self.getFilename(), 'r', encoding='utf-8') as inFile:
            lines = inFile.readlines()

            header = [line.rstrip() for line in lines[:7] if line.strip()]

            mothersData = [line.strip().split(", ") for line in lines[7:] if line.strip()]

        return header, mothersData
    
    def setHeader(self, header):
        self._header = header

    def setMothersData(self, mothersData):
        self._mothersData = mothersData

    def setMothers(self, mothers):
        self._mothers = mothers

    def getHeader(self):
        return self._header

    def getMothersData(self):
        return self._mothersData
    
    def getMothers(self):
        return self._mothers

    def sortMothers(self):
        self.getMothers().sort(key = Mother.sortMothersKeys)
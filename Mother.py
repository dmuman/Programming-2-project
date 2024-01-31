class Mother:
    def __init__(self, name, age, tagColour, riskLevel):
        self._name = name
        self._age = age
        self._tagColour = tagColour
        self._riskLevel = riskLevel

    #setters
    def setName(self, name):
        self._name = name
    
    def setAge(self, age):
        self._age = age

    def setTagColour(self, tagColour):
        self._tagColour = tagColour
    
    def setRiskLevel(self, riskLevel):
        self._riskLevel = riskLevel

    #getters
    def getName(self):
        return self._name
    
    def getAge(self):
        return self._age

    def getTagColour(self):
        return self._tagColour
    
    def getRiskLevel(self):
        return self._riskLevel

    #string
    def __str__(self):
        return f'Name: {self.getName()}\nAge: {self.getAge()}\nTag colour: {self.getTagColour()}\nRisk level: {self.getRiskLevel()}'
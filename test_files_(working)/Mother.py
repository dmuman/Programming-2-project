class Mother:
    def __init__(self, name, age, tagColour, riskLevel):
        self._name = name
        self._age = age
        self._tagColour = tagColour
        self._riskLevel = riskLevel
        self._mother = [self.getName(), self.getAge(), self.getTagColour(), self.getRiskLevel()]

    def setName(self, name):
        self._name = name
    
    def setAge(self, age):
        self._age = age

    def setTagColour(self, tagColour):
        self._tagColour = tagColour
    
    def setRiskLevel(self, riskLevel):
        self._riskLevel = riskLevel

    def setMother(self, mother):
        self._mother = mother

    def getName(self):
        return self._name
    
    def getAge(self):
        return int(self._age)

    def getTagColour(self):
        return self._tagColour
    
    def getRiskLevel(self):
        return self._riskLevel
    
    def getMother(self):
        return self._mother

    def sortMothersKeys(self):

        risks={"high":1, "low":2}
        tags={"red": 3, "yellow":2, "green":1}

        return (-risks[self.getRiskLevel()], tags[self.getTagColour()], -self.getAge(), self.getName())

    #TODO

    def __lt__(self, other):
        return self.getAge() < other.getAge()

    def __eq__(self, other):
        return (
            self.getName() == other.getName() and
            self.getSkill() == other.getSkill() and
            self.getNextFreeHours() == other.getNextFreeHours() and
            self.getDailyMinutes() == other.getDailyMinutes() and
            self.getWeeklyHours() == other.getWeeklyHours()
        )
    
    def __repr__(self):
        return str(self.getMother())
    
    def __str__(self):
        return str(self.getMother())
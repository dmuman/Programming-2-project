class DoctorTest:
    def __init__(self, name, skill, nextFreeHours, dailyMinutes, weeklyHours):
        self._name = name
        self._skill = skill
        self._nextFreeHours = nextFreeHours
        self._dailyMinutes = dailyMinutes
        self._weeklyHours = weeklyHours

    def setName(self, name):
        self._name = name
    
    def setSkill(self, skill):
        self._skill = skill

    def setNextFreeHours(self, nextFreeHours):
        self._nextFreeHours = nextFreeHours
    
    def setDailyMinutes(self, dailyMinutes):
        self._dailyMinutes = dailyMinutes
    
    def setWeeklyHours(self, weeklyHours):
        self._weeklyHours = weeklyHours

    def getName(self):
        return self._name
    
    def getSkill(self):
        return self._skill

    def getNextFreeHours(self):
        return self._nextFreeHours
    
    def getDailyMinutes(self):
        return self._dailyMinutes
    
    def getWeeklyHours(self):
        return self._weeklyHours
    
    def __str__(self):
        return f"Name: {self.getName()}, Skill: {self.getSkill()}, Next Free Hours: {self.getNextFreeHours()}, Daily Minutes: {self.getDailyMinutes()}, Weekly Hours: {self.getWeeklyHours()}"
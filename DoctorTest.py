class DoctorTest:
    def __init__(self, name, skill, nextFreeHours, dailyMinutes, weeklyHours):
        self._name = name
        self._skill = skill
        self._nextFreeHours = nextFreeHours
        self._dailyMinutes = dailyMinutes
        self._weeklyHours = weeklyHours
        self._doctor = [self.getName(), self.getSkill(), self.getNextFreeHours(), self.getDailyMinutes(), self.getWeeklyHours()]

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

    def setDoctor(self, doctor):
        self._doctor = doctor

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
    
    def getDoctor(self):
        return self._doctor
    
    def __str__(self):
        return str(self.getDoctor())
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
        return int(self._skill)

    def getNextFreeHours(self):
        return self.timeToInt(self._nextFreeHours)
    
    def getDailyMinutes(self):
        return int(self._dailyMinutes)
    
    def getWeeklyHours(self):
        return self.timeToInt(self._weeklyHours)
    
    def getDoctor(self):
        return self._doctor
    
    def timeToInt(self, time):
        t = time.split("h")
        hours = int(t[0])
        minutes = int(t[1])

        return [hours, minutes]
    
    def intToTime(self, hour, minutes):
        h = str(hour)
        m = str(minutes)

        if hour < 10:
            h = "0" + h

        if minutes < 10 or minutes == 0:
            m = "0" + m

        time = f"{h}h{m}"

        return time

    def sortDoctorsKeys(self):
        if self.getDailyMinutes() > 240:
            timeToPause = 240*2 - self.getDailyMinutes()
        else:
            timeToPause = 240 - self.getDailyMinutes()

        totalMinutesWeeklyWorked = (self.getWeeklyHours()[0]*60 + self.getWeeklyHours()[1])

        timeToWeeklyPause = 40 * 60 - totalMinutesWeeklyWorked

        return (-self.getSkill(), -timeToPause, -timeToWeeklyPause, self.getName())

    #TODO

    def isDoctorFree(self):
        pass

    def updateDoctorsTime(self):
        pass

    def updateDoctors(self):
        pass

    def __lt__(self, other):
        return (self.getWeeklyHours()[0]*60 + self.getWeeklyHours()[0]) < (other.getWeeklyHours()[0]*60 + other.getWeeklyHours()[0])

    def __eq__(self, other):
        return (
            self.getName() == other.getName() and
            self.getSkill() == other.getSkill() and
            self.getNextFreeHours() == other.getNextFreeHours() and
            self.getDailyMinutes() == other.getDailyMinutes() and
            self.getWeeklyHours() == other.getWeeklyHours()
        )
    
    def __repr__(self):
        return str(self.getDoctor())
    
    def __str__(self):
        return str(self.getDoctor())
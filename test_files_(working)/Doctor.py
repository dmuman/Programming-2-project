from Helper import Helper

class Doctor:
    HOURS_IDX = 0
    MINUTES_IDX = 1
    WKL_PAUSE = 'weekly leave'
    def __init__(self, name, skill, nextFreeHours, dailyMinutes, weeklyHours):
        self._name = name
        self._skill = skill
        self._nextFreeHours = nextFreeHours
        self._dailyMinutes = dailyMinutes
        self._weeklyHours = weeklyHours
        self._doctor = [self.getName(), self.getSkill(), self.getNextFreeHours(), self.getDailyMinutes(), self.getWeeklyHours()]
        self._isDoctorAssigned = False

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

    def setStatus(self, status):
        self._isDoctorAssigned = status

    def getName(self):
        return self._name
    
    def getSkill(self):
        return int(self._skill)

    def getNextFreeHours(self):
        if self._nextFreeHours == self.WKL_PAUSE:
            return self.WKL_PAUSE
        else:
            return Helper().timeToInt(self._nextFreeHours)
    
    def getDailyMinutes(self):
        return int(self._dailyMinutes)
    
    def getWeeklyHours(self):
        return Helper().timeToInt(self._weeklyHours)
    
    def getDoctor(self):
        return self._doctor
    
    def getStatus(self):
        return self._isDoctorAssigned

    def sortDoctorsKeys(self):
        if self.getDailyMinutes() > 240:
            timeToPause = 240*2 - self.getDailyMinutes()
        else:
            timeToPause = 240 - self.getDailyMinutes()

        totalMinutesWeeklyWorked = (self.getWeeklyHours()[self.HOURS_IDX]*60 + self.getWeeklyHours()[self.MINUTES_IDX])

        timeToWeeklyPause = 40 * 60 - totalMinutesWeeklyWorked

        return (-self.getSkill(), -timeToPause, -timeToWeeklyPause, self.getName())

    def updateDoctorsTime(self, minutesToAdd):
        oldFreeHours = self.getNextFreeHours()
        oldDailyMinutes = self.getDailyMinutes()
        oldWeeklyHours = self.getWeeklyHours()
 
        #declaring variables for new free hours, daily minutes worked and weekly hours worked
        newFreeHours = None
        newWeeklyHours = None
        newDailyMinutes = int(oldDailyMinutes) + minutesToAdd #already adding minutes to it

        #declaring variables for old hours and minutes from old free hours
        hoursFromOldHours, minutesFromOldHours = oldFreeHours

        hoursFromOldWeeklyHours, minutesFromOldWeeklyHours = oldWeeklyHours 

        if minutesFromOldHours < 30:                                            #checks if minutes from old hours are less then 30(time from the new schedule)
            minutesFromOldHours = minutesFromOldHours + (30 - minutesFromOldHours)                               #if so, properly adding new minutes
            oldFreeHours = Helper().intToTime(hoursFromOldHours, minutesFromOldHours)    #updating old free hours, considering the time in new schedule
            newFreeHours = Helper().updateHours(oldFreeHours, minutesToAdd)              #calculating new free hours, using updateHours() function from the dateTime module
        
        if int(oldDailyMinutes) < 240:                                       #checks if old daily minutes worked are less than 240
            if newDailyMinutes >= 240:                                       #if so, checks if new daily minutes worked are greater than 240
                newFreeHours = Helper().intToTime(hoursFromOldHours + 1, minutesFromOldHours + minutesToAdd)    #if so, adding one hour(i.e. one hour pause) to the new free hours
            else:                                                          #checks if new daily minutes worked are less than 240
                newFreeHours = Helper().updateHours(Helper().intToTime(hoursFromOldHours, minutesFromOldHours), minutesToAdd)      #if so, adding minutes to the new free hours, using updateHours() function from th dateTime module
        else:                                                               #checks if old daily minutes worked are already greater than 240
            newFreeHours = Helper().updateHours(Helper().intToTime(hoursFromOldHours, minutesFromOldHours), minutesToAdd)          #if so, adding minutes to the new free hours, using updateHours() function from th dateTime module

        newWeeklyHours = Helper().updateHours(Helper().intToTime(hoursFromOldWeeklyHours, minutesFromOldWeeklyHours), minutesToAdd)      #updating new weekly worked hours using the updateHours() function from the dateTime module

        if Helper().timeToInt(newWeeklyHours)[self.HOURS_IDX] >= 40:           #checks if new weekly worked hours are greater than 40
            newFreeHours = self.WKL_PAUSE                    #if so, doctor receives weekly pause   

        self.setDailyMinutes(newDailyMinutes)
        self.setNextFreeHours(newFreeHours)
        self.setWeeklyHours(newWeeklyHours)
        self.setDoctor([self.getName(), self.getSkill(), self.getNextFreeHours(), self.getDailyMinutes(), self.getWeeklyHours()])
    
    def __repr__(self):
        return str(self.getDoctor())
    
    def __str__(self):
        if self.getNextFreeHours() == self.WKL_PAUSE:
            return f'{str(self.getName())}, {str(self.getSkill())}, {self.getNextFreeHours()}, {str(self.getDailyMinutes())}, {Helper().intToTime(*self.getWeeklyHours())}'
        else:
            return f'{str(self.getName())}, {str(self.getSkill())}, {Helper().intToTime(*self.getNextFreeHours())}, {str(self.getDailyMinutes())}, {Helper().intToTime(*self.getWeeklyHours())}'
            
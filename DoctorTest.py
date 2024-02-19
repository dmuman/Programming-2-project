class DoctorTest:
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

    def setStatus(self, status):
        self._isDoctorAssigned = status

    def getStatus(self):
        return self._isDoctorAssigned

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
        if self._nextFreeHours == self.WKL_PAUSE:
            return self.WKL_PAUSE
        else:
            return self.timeToInt(self._nextFreeHours)
    
    def getDailyMinutes(self):
        return int(self._dailyMinutes)
    
    def getWeeklyHours(self):
        return self.timeToInt(self._weeklyHours)
    
    def getDoctor(self):
        return self._doctor
    
    def timeToInt(self, time):
        t = time.split("h")
        hours = int(t[self.HOURS_IDX])
        minutes = int(t[self.MINUTES_IDX])

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

        totalMinutesWeeklyWorked = (self.getWeeklyHours()[self.HOURS_IDX]*60 + self.getWeeklyHours()[self.MINUTES_IDX])

        timeToWeeklyPause = 40 * 60 - totalMinutesWeeklyWorked

        return (-self.getSkill(), -timeToPause, -timeToWeeklyPause, self.getName())

    def updateDoctorsTime(self, minutesToAdd):
        oldFreeHours = self.getNextFreeHours()
        oldDailyMinutes = self.getDailyMinutes()
        oldWeeklyHours = self.getWeeklyHours()

        #i love you dimka 
        #declaring variables for new free hours, daily minutes worked and weekly hours worked
        newFreeHours = None
        newWeeklyHours = None
        newDailyMinutes = int(oldDailyMinutes) + minutesToAdd #already adding minutes to it

        #declaring variables for old hours and minutes from old free hours
        hoursFromOldHours, minutesFromOldHours = oldFreeHours

        hoursFromOldWeeklyHours, minutesFromOldWeeklyHours = oldWeeklyHours 

        if minutesFromOldHours < 30:                                            #checks if minutes from old hours are less then 30(time from the new schedule)
            minutesFromOldHours = minutesFromOldHours + \
                (30 - minutesFromOldHours)                               #if so, properly adding new minutes
            oldFreeHours = self.intToTime(hoursFromOldHours, minutesFromOldHours)    #updating old free hours, considering the time in new schedule
            newFreeHours = self.updateHours(oldFreeHours, minutesToAdd)              #calculating new free hours, using updateHours() function from the dateTime module
        
        if int(oldDailyMinutes) < 240:                                       #checks if old daily minutes worked are less than 240
            if newDailyMinutes >= 240:                                       #if so, checks if new daily minutes worked are greater than 240
                newFreeHours = self.intToTime(hoursFromOldHours + 1, minutesFromOldHours)    #if so, adding one hour(i.e. one hour pause) to the new free hours
            else:                                                          #checks if new daily minutes worked are less than 240
                newFreeHours = self.updateHours(self.intToTime(hoursFromOldHours, minutesFromOldHours), minutesToAdd)      #if so, adding minutes to the new free hours, using updateHours() function from th dateTime module
        else:                                                               #checks if old daily minutes worked are already greater than 240
            newFreeHours = self.updateHours(self.intToTime(hoursFromOldHours, minutesFromOldHours), minutesToAdd)          #if so, adding minutes to the new free hours, using updateHours() function from th dateTime module

        newWeeklyHours = self.updateHours(self.intToTime(hoursFromOldWeeklyHours, minutesFromOldWeeklyHours), minutesToAdd)      #updating new weekly worked hours using the updateHours() function from the dateTime module

        if self.timeToInt(newWeeklyHours)[0] >= 40:           #checks if new weekly worked hours are greater than 40
            newFreeHours = self.WKL_PAUSE                    #if so, doctor receives weekly pause   

        self.setDailyMinutes(newDailyMinutes)
        self.setNextFreeHours(newFreeHours)
        self.setWeeklyHours(newWeeklyHours)
        self.setDoctor([self.getName(), self.getSkill(), self.getNextFreeHours(), self.getDailyMinutes(), self.getWeeklyHours()])

    def updateHours(self, hoursToUpdate, minutesToAdd):
        #declaring variables for holding the int representatin of hours, minutes and total minutes
        intHours = None 
        intMinutes = None
        totalMinutes = None
        #declaring variable for the new, updated hours
        updatedHours = None
        #in case new minutes are greater than 60
        if self.timeToInt(hoursToUpdate)[self.MINUTES_IDX] + minutesToAdd > 60:
            intHours = self.timeToInt(hoursToUpdate)[self.HOURS_IDX]                                 #assigning hours
            intMinutes = self.timeToInt(hoursToUpdate)[self.MINUTES_IDX]                            #assigning minutes
            totalMinutes = intHours * 60 + intMinutes + minutesToAdd            #new totalMinutes
            updatedHours = self.intToTime((totalMinutes // 60), (totalMinutes % 60)) #new, updated hours, based on totalMinutes
        #in case new minutes are equal 60
        elif self.timeToInt(hoursToUpdate)[self.MINUTES_IDX] + minutesToAdd == 60:
            intHours = self.timeToInt(hoursToUpdate)[self.HOURS_IDX] + 1         #updating hours(adding 1 hour)
            intMinutes = 0                                  #updating minutes(equal 00)
            updatedHours = self.intToTime(intHours, intMinutes)  #new, updated hours
        #in case new minutes are less than 60
        else:
            intHours = self.timeToInt(hoursToUpdate)[self.HOURS_IDX]                     #assigning hours. they remain the same
            intMinutes = self.timeToInt(hoursToUpdate)[self.MINUTES_IDX] + minutesToAdd #updating minutes with minutesToAdd
            updatedHours = self.intToTime(intHours, intMinutes)          #new, updated hours
        return updatedHours

    #TODO

    def isDoctorFree(self):
        pass

    def updateDoctors(self):
        pass

    ######################

    def __lt__(self, other):
        return (self.getWeeklyHours()[self.HOURS_IDX]*60 + self.getWeeklyHours()[self.HOURS_IDX]) < (other.getWeeklyHours()[self.HOURS_IDX]*60 + other.getWeeklyHours()[self.HOURS_IDX])

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
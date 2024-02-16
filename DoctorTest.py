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

    def updateDoctorsTime(self, minutesToAdd):
        oldFreeHours = self.getNextFreeHours()
        oldDailyMinutes = self.getDailyMinutes()
        oldWeeklyHours = self.getWeeklyHours()

        #declaring variables for new free hours, daily minutes worked and weekly hours worked
        newFreeHours = None
        newWeeklyHours = None
        newDailyMinutes = int(oldDailyMinutes) + minutesToAdd #already adding minutes to it

        #declaring variables for old hours and minutes from old free hours
        hoursFromOldHours, minutesFromOldHours = self.timeToInt(oldFreeHours)

        if minutesFromOldHours < 30:                                            #checks if minutes from old hours are less then 30(time from the new schedule)
            minutesFromOldHours = self.timeToInt(oldFreeHours)[1] + \
                (30 - self.timeToInt(oldFreeHours)[1])                               #if so, properly adding new minutes
            oldFreeHours = self.intToTime(hoursFromOldHours, minutesFromOldHours)    #updating old free hours, considering the time in new schedule
            newFreeHours = updateHours(oldFreeHours, minutesToAdd)              #calculating new free hours, using updateHours() function from the dateTime module
        
        if int(oldMinutesDias) < 240:                                       #checks if old daily minutes worked are less than 240
            if newMinutesDias >= 240:                                       #if so, checks if new daily minutes worked are greater than 240
                newFreeHours = intToTime(hourToInt(oldFreeHours) + 1, \
                                        minutesToInt(oldFreeHours)+20)     #if so, adding one hour(i.e. one hour pause) to the new free hours
            else:                                                           #checks if new daily minutes worked are less than 240
                newFreeHours = updateHours(oldFreeHours, minutesToAdd)      #if so, adding minutes to the new free hours, using updateHours() function from th dateTime module
        else:                                                               #checks if old daily minutes worked are already greater than 240
            newFreeHours = updateHours(oldFreeHours, minutesToAdd)          #if so, adding minutes to the new free hours, using updateHours() function from th dateTime module
        
        newHorasSemanais = updateHours(oldHorasSemanais, minutesToAdd)      #updating new weekly worked hours using the updateHours() function from the dateTime module

        if hourToInt(newHorasSemanais) >= 40:           #checks if new weekly worked hours are greater than 40
            newFreeHours = WKL_PAUSE                    #if so, doctor receives weekly pause   

        return [oldDoctor[DOCT_NAME_IDX], str(oldDoctor[DOCT_SKILL_IDX]), \
                newFreeHours, str(newMinutesDias), newHorasSemanais]

    def updateHours(hoursToUpdate, minutesToAdd):
        #declaring variables for holding the int representatin of hours, minutes and total minutes
        intHours = None 
        intMinutes = None
        totalMinutes = None

        #declaring variable for the new, updated hours
        updatedHours = None

        #in case new minutes are greater than 60
        if minutesToInt(hoursToUpdate) + minutesToAdd > 60:
            intHours = hourToInt(hoursToUpdate)                                 #assigning hours
            intMinutes = minutesToInt(hoursToUpdate)                            #assigning minutes
            totalMinutes = intHours * 60 + intMinutes + minutesToAdd            #new totalMinutes
            updatedHours = intToTime((totalMinutes // 60), (totalMinutes % 60)) #new, updated hours, based on totalMinutes

        #in case new minutes are equal 60
        elif minutesToInt(hoursToUpdate) + minutesToAdd == 60:
            intHours = hourToInt(hoursToUpdate) + 1         #updating hours(adding 1 hour)
            intMinutes = 0                                  #updating minutes(equal 00)
            updatedHours = intToTime(intHours, intMinutes)  #new, updated hours

        #in case new minutes are less than 60
        else:
            intHours = hourToInt(hoursToUpdate)                     #assigning hours. they remain the same
            intMinutes = minutesToInt(hoursToUpdate) + minutesToAdd #updating minutes with minutesToAdd
            updatedHours = intToTime(intHours, intMinutes)          #new, updated hours

        return updatedHours

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
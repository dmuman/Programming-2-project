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
                newFreeHours = self.intToTime(hoursFromOldHours + 1, \
                                        minutesFromOldHours)[1]+20     #if so, adding one hour(i.e. one hour pause) to the new free hours
            else:                                                           #checks if new daily minutes worked are less than 240
                newFreeHours = self.updateHours(oldFreeHours, minutesToAdd)      #if so, adding minutes to the new free hours, using updateHours() function from th dateTime module
        else:                                                               #checks if old daily minutes worked are already greater than 240
            newFreeHours = self.updateHours(oldFreeHours, minutesToAdd)          #if so, adding minutes to the new free hours, using updateHours() function from th dateTime module

        newWeeklyHours = self.updateHours(self.intToTime(hoursFromOldHours, minutesFromOldWeeklyHours), minutesToAdd)      #updating new weekly worked hours using the updateHours() function from the dateTime module

        if self.timeToInt(newWeeklyHours)[0] >= 40:           #checks if new weekly worked hours are greater than 40
            newFreeHours = 'weekly pause'                    #if so, doctor receives weekly pause   

        self.setDailyMinutes(newDailyMinutes)
        self.setNextFreeHours(newFreeHours)
        self.setWeeklyHours(newFreeHours)
        self.setDoctor([self.getName(), self.getSkill(), self.getNextFreeHours(), self.getDailyMinutes(), self.getWeeklyHours()])

        return [self.getName(), str(self.getSkill()), \
                self.getNextFreeHours(), self.getDailyMinutes(), self.getWeeklyHours()]

def updateHours(self, hoursToUpdate, minutesToAdd):
    #declaring variables for holding the int representatin of hours, minutes and total minutes
    intHours = None 
    intMinutes = None
    totalMinutes = None
    #declaring variable for the new, updated hours
    updatedHours = None
    #in case new minutes are greater than 60
    if self.timeToInt(hoursToUpdate)[1] + minutesToAdd > 60:
        intHours = self.timeToInt(hoursToUpdate)[0]                                 #assigning hours
        intMinutes = self.timeToInt(hoursToUpdate)[1]                            #assigning minutes
        totalMinutes = intHours * 60 + intMinutes + minutesToAdd            #new totalMinutes
        updatedHours = self.intToTime((totalMinutes // 60), (totalMinutes % 60)) #new, updated hours, based on totalMinutes
    #in case new minutes are equal 60
    elif self.timeToInt(hoursToUpdate)[1] + minutesToAdd == 60:
        intHours = self.timeToInt(hoursToUpdate)[0] + 1         #updating hours(adding 1 hour)
        intMinutes = 0                                  #updating minutes(equal 00)
        updatedHours = self.intToTime(intHours, intMinutes)  #new, updated hours
    #in case new minutes are less than 60
    else:
        intHours = self.timeToInt(hoursToUpdate)[0]                     #assigning hours. they remain the same
        intMinutes = self.timeToInt(hoursToUpdate)[1] + minutesToAdd #updating minutes with minutesToAdd
        updatedHours = self.intToTime(intHours, intMinutes)          #new, updated hours
    return updatedHours
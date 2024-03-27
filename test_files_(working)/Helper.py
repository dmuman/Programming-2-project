class Helper:
    def timeToInt(self, time):
        t = time.split("h")
        hours = int(t[0])
        minutes = int(t[1])

        return [hours, minutes]
    
    def hoursToInt(self, time):
        t = time.split("h")
        hours = int(t[0])

        return hours
    
    def minutesToInt(self, time):
        t = time.split("h")
        minutes = int(t[1])

        return minutes
    
    def intToTime(self, hour, minutes):
        h = str(hour)
        m = str(minutes)

        if hour < 10:
            h = "0" + h

        if minutes < 10 or minutes == 0:
            m = "0" + m

        time = f"{h}h{m}"

        return time

    def updateHours(self, hoursToUpdate, minutesToAdd):
        #declaring variables for holding the int representatin of hours, minutes and total minutes
        intHours = None 
        intMinutes = None
        totalMinutes = None
        #declaring variable for the new, updated hours
        updatedHours = None
        #in case new minutes are greater than 60
        if self.minutesToInt(hoursToUpdate) + minutesToAdd > 60:
            intHours = self.hoursToInt(hoursToUpdate)                                #assigning hours
            intMinutes = self.minutesToInt(hoursToUpdate)                            #assigning minutes
            totalMinutes = intHours * 60 + intMinutes + minutesToAdd            #new totalMinutes
            updatedHours = self.intToTime((totalMinutes // 60), (totalMinutes % 60)) #new, updated hours, based on totalMinutes
        #in case new minutes are equal 60
        elif self.minutesToInt(hoursToUpdate) + minutesToAdd == 60:
            intHours = self.hoursToInt(hoursToUpdate) + 1         #updating hours(adding 1 hour)
            intMinutes = 0                                  #updating minutes(equal 00)
            updatedHours = self.intToTime(intHours, intMinutes)  #new, updated hours
        #in case new minutes are less than 60
        else:
            intHours = self.hoursToInt(hoursToUpdate)                     #assigning hours. they remain the same
            intMinutes = self.minutesToInt(hoursToUpdate) + minutesToAdd #updating minutes with minutesToAdd
            updatedHours = self.intToTime(intHours, intMinutes)          #new, updated hours
        return updatedHours
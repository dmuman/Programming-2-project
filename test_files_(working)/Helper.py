class Helper:
    HOURS_IDX = 0
    MINUTES_IDX = 1
    HEADER_TIME_IDX = 3
    FILENAME_HEADER_IDX = 6

    def __init__(self):
        pass

    def readFile(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8-sig') as inFile:
                timeInName = filename[-9:-4]

                lines = inFile.readlines()

                header = [line.rstrip() for line in lines[:7] if line.strip()]

                timeInHeader = header[self.HEADER_TIME_IDX]

                data = [line.strip().split(", ") for line in lines[7:] if line.strip()]

                if header[self.FILENAME_HEADER_IDX] not in ['Schedule:', 'Doctors:', 'Mothers:']:
                    raise IOError(f"scope inconsistency between name and header in file <{filename}>")
                elif timeInHeader != timeInName:
                    raise IOError("time in the header and in the name are not the same")
                else:
                    return header, data
                
        except IOError as e:
            print(f"File head error: {e}")
    
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

    def updateHours(self, hoursToUpdate, minutesToAdd):
        #declaring variables for holding the int representatin of hours, minutes and total minutes
        intHours = None 
        intMinutes = None
        totalMinutes = None
        #declaring variable for the new, updated hours
        updatedHours = None
        #in case new minutes are greater than 60
        if self.timeToInt(hoursToUpdate)[self.MINUTES_IDX] + minutesToAdd > 60:
            intHours = self.timeToInt(hoursToUpdate)[self.HOURS_IDX]                                #assigning hours
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
    def writeFile():
        pass
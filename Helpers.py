class Helpers:

    def removeHeader(fileName):

        for _ in range(7):
            fileName.readline()

        return fileName
    
    def saveHeader(fileName):
        """
        Saves the header into a list, containing lists, 
        each of one has the line of the header, corresponding to the index.

        Requires: fileName is a str with the ending of a .txt, 
        header is presented inside the file.

        Ensures: that the given number of lines(NUM_HEADER_LINES) 
        are saved into a list when reading the .txt file(i.e. header)
        """
        inFile = open(fileName, "r", encoding = "utf-8-sig") #opening the file

        #declaring variables for the header, temporary header and it's data
        header = []
        headertemp = []
        headerData = []

        for _ in range(7):               #using placeholder do write to the header only given amount of lines
            headerData = inFile.readline()              #headerData is equal to each line in header
            headertemp.append(headerData)               #appending temporary header with headerData
        
        for line in headertemp:                         #searching through the temporary header
            headertemp = line.rstrip().split(", ")      #splitting the info by commas
            header.append(headertemp)                   #appending the header

        return header
    
    #function for transforming string hours to int
    def hourToInt(time):
        """
        Gets the provided time in type string that has the letter 'h' inside of it 
        that separates hours and minutes and then returns the amount of hours in type int.

        Requires: time is a string and has the letter 'h' inside that separates hours and minutes.
        Ensures: the amount of hours in the type of int, that is provided 
        before the letter 'h' inside of the provided time.
        Examples:
        >>> hourToInt("14h00")
        14
        >>> hourToInt("09h30")
        9
        """
        t = time.split("h")     #splitting the time by the letter "h"
        hours = int(t[0])       #getting hours

        return hours


    #function for transforming string minutes to int
    def minutesToInt(time):
        """
        Gets the provided time in type string that has the letter 'h' inside of it 
        that separates hours and minutes and then returns the amount of minutes in type int.

        Requires: time is a string and has the letter 'h' inside that separates hours and minutes.
        Ensures: the amount of minutes in the type of int, that is provided 
        after the letter 'h' inside of the provided time.
        Examples:
        >>> minutesToInt("14h00")
        0
        >>> minutesToInt("09h30")
        30
        """
        t = time.split("h")     #splitting the time by the letter "h"
        minutes = int(t[1])     #getting the minutes

        return minutes


    #function for transforming int hours and minutes to string time
    def intToTime(hour, minutes):
        """
        Gets the provided amount of hours and minutes, separated by commas, in the type of int 
        and returns the time of type string with the look of 'hourshminutes'. 
        Hours and minutes are separated by the letter 'h'.

        Requires: hour and minutes are positive integers, hour is less than 24 and minutes is less than 60.
        Ensures: string representation of the provided amount of hours and minutes, separated by the letter 'h'.
        >>> intToTime(9, 0)
        '09h00'
        >>> intToTime(14, 30)
        '14h30'
        """
        h = str(hour)
        m = str(minutes)

        if hour < 10:
            h = "0" + h         #adding zero at the beginning to the hours, if hours are less then 10. 9 become "09", for example

        if minutes < 10 or minutes == 0:
            m = "0" + m         #adding zero at the beginning to the minutes, if minutes are less then 10. 0 become "00", for example

        time = f"{h}h{m}"       #creating a new string for the time

        return time

    #function for updating string time with int minutes
def updateHours(hoursToUpdate, minutesToAdd):
    """
    Updates the time with the given time to update and minutes to add. 
    Time is in the format of HHhMM, minutesToAdd are integers.
    Using converting time functions to get the hours and minutes and then to update those.
    It has three cases:
    If the added minutes ultrapassed 60(i.e. more than one hour)
    If the added minutes is iqual 60(i.e. iqual one hour)
    If the added minutes are less than 60(i.e. less than one hour)

    Requires: hoursToUpdate is a string in the format of HHhMM, minutesToAdd is integer

    Ensures: new, updated time with the given amount of minutes, in type string in the format of HHhMM

    >>> updateHours("14h25", 40)
    '15h05'
    >>> updateHours("14h25", 35)
    '15h00'
    >>> updateHours("14h25", 30)
    '14h55'
    >>> updateHours("23h30", 40)
    '00h10'
    """
    #declaring variables for holding the int representatin of hours, minutes and total minutes
    intHours = None 
    intMinutes = None
    totalMinutes = None

    #declaring variable for the new, updated hours
    updatedHours = None

    #in case new minutes are greater than 60
    if Helpers.minutesToInt(hoursToUpdate) + minutesToAdd > 60:
        intHours = Helpers.hourToInt(hoursToUpdate)                                 #assigning hours
        intMinutes = Helpers.minutesToInt(hoursToUpdate)                            #assigning minutes
        totalMinutes = intHours * 60 + intMinutes + minutesToAdd            #new totalMinutes
        updatedHours = Helpers.intToTime((totalMinutes // 60), (totalMinutes % 60)) #new, updated hours, based on totalMinutes

    #in case new minutes are equal 60
    elif Helpers.minutesToInt(hoursToUpdate) + minutesToAdd == 60:
        intHours = Helpers.hourToInt(hoursToUpdate) + 1         #updating hours(adding 1 hour)
        intMinutes = 0                                  #updating minutes(equal 00)
        updatedHours = Helpers.intToTime(intHours, intMinutes)  #new, updated hours

    #in case new minutes are less than 60
    else:
        intHours = Helpers.hourToInt(hoursToUpdate)                     #assigning hours. they remain the same
        intMinutes = Helpers.minutesToInt(hoursToUpdate) + minutesToAdd #updating minutes with minutesToAdd
        updatedHours = Helpers.intToTime(intHours, intMinutes)          #new, updated hours

    return updatedHours

    #testing part
    if __name__ == "__main__":
        import doctest
        doctest.testmod()
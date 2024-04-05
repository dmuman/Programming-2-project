class Helper:
    """
    Helper class providing various helper functions.
    """

    ############################################################################
    ############################## INITIALIZATION ##############################
    ############################################################################

    def __init__(self):
        """
        There're no attributes since this class doesn't need any, it's just
        providing helping functions that are used throughout the project.
        Initializes constants.

        Ensures:
        Constants for the next indexes:
        hours
        minutes
        time in header
        header filename
        """
        # instance variables (constants)
        self._HOURS_IDX = 0             # hours index
        self._MINUTES_IDX = 1           # minutes index
        self._HEADER_TIME_IDX = 3       # header time index
        self._FILENAME_HEADER_IDX = 6   # filename header index
        self._HEADER_END_IDX = 7

    ############################################################################
    ################################# GETTERS ##################################
    ############################################################################

    def getHoursIdx(self):
        """
        Gets the hours index.

        Ensures:
        Hours index constant.
        """
        return self._HOURS_IDX
    
    def getMinutesIdx(self):
        """
        Gets the minutes index.

        Ensures:
        Minutes index constant.
        """
        return self._MINUTES_IDX
    
    def getHeaderTimeIdx(self):
        """
        Gets the header time index.

        Ensures:
        Header time index constant.
        """
        return self._HEADER_TIME_IDX
    
    def getFilenameHeaderIdx(self):
        """
        Gets the filename header index.

        Ensures:
        Filename header index constant.
        """
        return self._FILENAME_HEADER_IDX
    
    def getHeaderEndIdx(self):
        """
        Gets the header end index.

        Ensures:
        Header end index constant.
        """
        return self._HEADER_END_IDX

    ############################################################################
    ############################# FILE OPERATIONS ##############################
    ############################################################################

    # reading file
    def readFile(self, filename):
        """
        Reads data from the specified file.

        Requires:
        filename is a string representing the name of the file to be read.
        file with provided filename has to be inside the same directory as
        the program.
        file is .txt format.

        Ensures:
        Tuple containing header and data from the file.
        Header is from the beginning of the file untill the
        header end index.
        Data is from the header end index untill the end of the file. 
        """
        # using try except to catch an exception
        try:
            # opening file using the right encoding
            with open(filename, 'r', encoding='utf-8-sig') as inFile:
                # declaring variable for the time in the name
                timeInName = filename[-9:-4]
                # using readlines()
                lines = inFile.readlines()
                # declaring variable for the header
                header = [line.rstrip() for line in 
                          lines[:self.getHeaderEndIdx()] if line.strip()]
                # declaring a variable for the time in the header
                timeInHeader = header[self.getHeaderTimeIdx()]
                # declaring a variable for the data
                data = [line.strip().split(", ") for line in 
                        lines[self.getHeaderEndIdx():] if line.strip()]

                # checking for the inconsistency in names
                if header[self.getFilenameHeaderIdx()] not in \
                    ['Schedule:', 'Doctors:', 'Mothers:']:
                    # if names are not the same - raising IOError
                    raise IOError(f"Scope inconsistency between name and " \
                                  f"header in file <{filename}>")
                # also checking for the inconsistency in times
                elif timeInHeader != timeInName:
                    # if times are not the same - raising IOError
                    raise IOError("Time in the header and in the name are not the same")
                # if there're no errors
                else:
                    # retirning header and data
                    return header, data
                
        # printing an exceprion
        except IOError as e:
            print(f"File head error: {e}")

    # writing file
    def writeFile(self, filename, header, data):
        """
        Writes data to the new .txt file based on provided name of the original
        file, header and data to write.

        Requires:
        filename is a string that represent the name of the original file.
        header is a list containing header information.
        data is a list containing information from the enter file.

        Ensures:
        new .txt file with the updated hours in name, header
        and with updated data.
        """
        # declaring variable for old time in name
        oldTimeInName = filename[-9:-4]
        # updating it
        newTimeInName = self.updateHours(oldTimeInName, 30)
        # updating time in the filename
        newFileName = f'{filename[0:-9]}{newTimeInName}.txt'

        # opening a file woth the right encoding
        with open(newFileName, 'w', encoding='utf-8-sig') as outFile:
            # writing updated header
            for i in range(len(header)):
                outFile.write(f'{header[i]}\n')

            # writing updated data
            for i in range(len(data)):
                # addind \n if it's not the last element in the list
                if i != len(data)-1:
                    outFile.write(f'{data[i]}\n')
                # not adding otherwise
                else:
                    outFile.write(f'{data[i]}')
    
    ############################################################################
    ########################### TIME CONVERSION FUNCTIONS ######################
    ############################################################################

    def timeToInt(self, time):
        """
        Converts time string to integer representation.
        Returns a list containing int hours and minutes

        Requires:
        time is a string in 'HHhMM' format.

        Ensures:
        List containing hours and minutes as integers.
        """
        t = time.split("h")
        hours = int(t[self.getHoursIdx()])
        minutes = int(t[self.getMinutesIdx()])
        return [hours, minutes]
    
    def intToTime(self, hour, minutes):
        """
        Converts integer hours and minutes to time string
        in 'HHhMM' format.

        Requires:
        hour is an int that represents the hour value.
        minutes is an int that represents the minutes value.

        Ensures:
        Time string in 'HHhMM' format.
        """
        h = str(hour)
        m = str(minutes)

        # adding 0 to the hours if they are less than 10
        if hour < 10:
            h = "0" + h

        # adding 0 to the minutes if they are less or equal 10
        if minutes < 10 or minutes == 0:
            m = "0" + m

        return f"{h}h{m}"

    ############################################################################
    ############################## UPDATE HOURS ################################
    ############################################################################

    def updateHours(self, hoursToUpdate, minutesToAdd):
        """
        Updates the hours by adding minutes.
        Returns string of the 'HHhMM' with the updated by the given amount of 
        minutes time.

        Requires:
        hoursToUpdate is a string representing the time string to be updated
        in the 'HHhMM' format.
        minutesToAdd is an integer representing the number of minutes to add.

        Ensures:
        Updated by the given amount of minutes time string
        in the 'HHhMM' format.
        """
        # declaring variables for hours, minutes, total minutes and updated hours
        intHours = None 
        intMinutes = None
        totalMinutes = None
        updatedHours = None

        if self.timeToInt(hoursToUpdate)[self.getMinutesIdx()] + minutesToAdd > 60:
            intHours = self.timeToInt(hoursToUpdate)[self.getHoursIdx()]
            intMinutes = self.timeToInt(hoursToUpdate)[self.getMinutesIdx()]
            totalMinutes = intHours * 60 + intMinutes + minutesToAdd
            updatedHours = self.intToTime((totalMinutes // 60), (totalMinutes % 60))
        elif self.timeToInt(hoursToUpdate)[self.getMinutesIdx()] + minutesToAdd == 60:
            intHours = self.timeToInt(hoursToUpdate)[self.getHoursIdx()] + 1
            intMinutes = 0
            updatedHours = self.intToTime(intHours, intMinutes)
        else:
            intHours = self.timeToInt(hoursToUpdate)[self.getHoursIdx()]
            intMinutes = self.timeToInt(hoursToUpdate)[self.getMinutesIdx()] + minutesToAdd
            updatedHours = self.intToTime(intHours, intMinutes)
        return updatedHours
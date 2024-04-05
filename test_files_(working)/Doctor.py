from Helper import Helper # importing Helper

class Doctor:
    """
    Doctor class representing a doctor with attributes 
    such as name, skill, next free hours, daily minutes, and weekly hours.
    """
    # class variables (constants)
    HOURS_IDX = 0               # hours index
    MINUTES_IDX = 1             # minutes index
    WKL_PAUSE = 'weekly leave'  # weekly pause

    ############################################################################
    ############################## INITIALIZATION ##############################
    ############################################################################

    def __init__(self, name, skill, nextFreeHours, dailyMinutes, weeklyHours):
        """
        Initializes a Doctor object.

        Requires:
        name is a string that represents the name of the doctor.
        skill is a string that represents the skill level of the doctor.
        nextFreeHours is a string that represents the next free hours of the doctor.
        dailyMinutes is a string that represents the daily minutes of the doctor.
        weeklyHours is a string that represents the weekly hours of the doctor.

        Ensures:
        A Doctor object is initialized with the specified attributes.
        """
        self._name = name
        self._skill = skill
        self._nextFreeHours = nextFreeHours
        self._dailyMinutes = dailyMinutes
        self._weeklyHours = weeklyHours
        self._doctor = [self.getName(), self.getSkill(), self.getNextFreeHours(), 
                        self.getDailyMinutes(), self.getWeeklyHours()]
        self._isDoctorAssigned = False

    ############################################################################
    ################################# SETTERS ##################################
    ############################################################################

    def setName(self, name):
        """
        Sets the name of the doctor.

        Requires:
        name is a string that represents new name of the doctor.

        Ensures:
        The name of the doctor is updated.
        """
        self._name = name
    
    def setSkill(self, skill):
        """
        Sets the skill level of the doctor.

        Requires:
        skill is a string that represents 
        the new skill level of the doctor.

        Ensures:
        The skill level of the doctor is updated.
        """
        self._skill = skill

    def setNextFreeHours(self, nextFreeHours):
        """
        Sets the next free hours of the doctor.

        Requires:
        nextFreeHours is a string that represents 
        the new next free hours of the doctor.

        Ensures:
        The next free hours of the doctor are updated.
        """
        self._nextFreeHours = nextFreeHours
    
    def setDailyMinutes(self, dailyMinutes):
        """
        Sets the daily minutes worked by the doctor.

        Requires:
        dailyMinutes is a string that represents 
        the new daily minutes worked by the doctor.

        Ensures:
        The daily minutes worked by the doctor are updated.
        """
        self._dailyMinutes = dailyMinutes
    
    def setWeeklyHours(self, weeklyHours):
        """
        Sets the weekly hours worked by the doctor.

        Requires:
        weeklyHours is a string that represents 
        the new weekly hours worked by the doctor.

        Ensures:
        The weekly hours worked by the doctor are updated.
        """
        self._weeklyHours = weeklyHours

    def setDoctor(self, doctor):
        """
        Sets the attributes of the doctor.

        Requires:
        doctor is a list containing the attributes of the doctor.

        Ensures:
        The attributes of the doctor are updated.
        """
        self._doctor = doctor

    def setStatus(self, status):
        """
        Sets the status of the doctor.

        Requires:
        status is a boolean that represents the new status of the doctor 
        (True if he is assigned, False otherwise).

        Ensures:
        The status of the doctor is updated.
        """
        self._isDoctorAssigned = status

    ############################################################################
    ################################# GETTERS ##################################
    ############################################################################

    def getName(self):
        """
        Gets the name of the doctor.

        Ensures:
        The string name of the doctor.
        """
        return self._name
    
    def getSkill(self):
        """
        Gets the skill level of the doctor.

        Ensures:
        Int skill level of the doctor.
        """
        return int(self._skill)

    def getNextFreeHours(self):
        """
        Gets the next free hours of the doctor.

        Ensures:
        String 'Weekly leave' if the doctor has the weekly leave,
        List in the format of [HH, MM] that represents 
        the next free hours of the doctor otherwise,
        using function from the Helper class.
        """
        if self._nextFreeHours == self.WKL_PAUSE:
            return self.WKL_PAUSE
        else:
            return Helper().timeToInt(self._nextFreeHours)
    
    def getDailyMinutes(self):
        """
        Gets the daily minutes worked by the doctor.

        Ensures:
        Int daily minutes worked by the doctor.
        """
        return int(self._dailyMinutes)
    
    def getWeeklyHours(self):
        """
        Gets the weekly hours worked by the doctor.

        Ensures:
        List that represents the weekly hours 
        worked by the doctor, in the format of [HH, MM],
        using function from the Helper class.
        """
        return Helper().timeToInt(self._weeklyHours)
    
    def getDoctor(self):
        """
        Gets the attributes of the doctor.

        Ensures:
        List containing the attributes of the doctor.
        """
        return self._doctor
    
    def getStatus(self):
        """
        Gets the status of the doctor.

        Ensures:
        True if the doctor is assigned, False otherwise.
        """
        return self._isDoctorAssigned

    ############################################################################
    ################################ SORT KEYS #################################
    ############################################################################

    def sortDoctorsKeys(self):
        """
        Generates sorting keys for doctors based on skill level, 
        time to next pause, and time to weekly pause.

        Ensures:
        Tuple containing sorting keys for the doctor.
        Where:
        Skills, time to next pause, and time weekly pause are sorted in descending order
        and names in alphabetical order.
        """
        # calculating time untill the next pause
        if self.getDailyMinutes() > 240:
            timeToPause = 240 * 2 - self.getDailyMinutes()
        else:
            timeToPause = 240 - self.getDailyMinutes()

        # calculating total minutes worked weekly
        totalMinutesWeeklyWorked = self.getWeeklyHours()[self.HOURS_IDX] * 60 + \
            self.getWeeklyHours()[self.MINUTES_IDX]

        # calculating time to weekly pause
        timeToWeeklyPause = 40 * 60 - totalMinutesWeeklyWorked

        return (-self.getSkill(), -timeToPause, -timeToWeeklyPause, self.getName())

    ############################################################################
    ############################## UPDATING TIME ###############################
    ############################################################################
    
    def updateDoctorsTime(self, minutesToAdd):
        """
        Updates the time attributes of the doctor by the given amount of minutes

        Requires:
        minutesToAdd is an int that represents 
        the number of minutes to be added to the doctor's time.

        Ensures:
        The time attributes of the doctor are updated 
        by the given amount of minutes to add.
        """
        # declaring variables for old hours
        oldFreeHours = self.getNextFreeHours()
        oldDailyMinutes = self.getDailyMinutes()
        oldWeeklyHours = self.getWeeklyHours()
 
        # declaring variables for new hours
        newFreeHours = None
        newWeeklyHours = None

        # new daily minutes are already updated
        newDailyMinutes = int(oldDailyMinutes) + minutesToAdd

        # assigning variables for old hours and minutes
        # from the old next free hours
        hoursFromOldHours, minutesFromOldHours = oldFreeHours

        # assigning variables for old hours and minutes
        # from the old weekly hours
        hoursFromOldWeeklyHours, minutesFromOldWeeklyHours = oldWeeklyHours 

        # updating hours to the time of the new schedule
        # if already updated hours are less than this time
        # using time functions from the Helper class
        if minutesFromOldHours < 30:
            # updating old minutes
            minutesFromOldHours = minutesFromOldHours + \
                (30 - minutesFromOldHours)
            
            # converting old hours from list to string
            oldFreeHours = Helper().intToTime(hoursFromOldHours, minutesFromOldHours)
            # assigning updated hours
            newFreeHours = Helper().updateHours(oldFreeHours, minutesToAdd)
        
        # if old daily minutes were less than 240
        if int(oldDailyMinutes) < 240:
            # if new daily minutes are greater or equal 240
            if newDailyMinutes >= 240:
                # adding one hour and minutesToAdd to the new free hours
                newFreeHours = Helper().intToTime(hoursFromOldHours + 1, 
                                                  minutesFromOldHours + minutesToAdd)
            # otherwise
            else:
                # just updating next free hours with the given amount of minutes
                newFreeHours = Helper().updateHours(Helper().intToTime(
                    hoursFromOldHours, minutesFromOldHours), minutesToAdd)
        # otherwise
        else:
            # just updating next free hours with the given amount of minutes
            newFreeHours = Helper().updateHours(Helper().intToTime(
                hoursFromOldHours, minutesFromOldHours), minutesToAdd)

        # updating weekly hours with the given amount of minutes
        newWeeklyHours = Helper().updateHours(Helper().intToTime(
            hoursFromOldWeeklyHours, minutesFromOldWeeklyHours), minutesToAdd)

        # if new weekly hours are greater than 40
        if Helper().timeToInt(newWeeklyHours)[self.HOURS_IDX] >= 40:
            # then the doctor receives a weekly pause
            newFreeHours = self.WKL_PAUSE

        # updatind doctor's info by setting new attributes
        # basically updating them
        self.setDailyMinutes(newDailyMinutes)
        self.setNextFreeHours(newFreeHours)
        self.setWeeklyHours(newWeeklyHours)
        self.setDoctor([self.getName(), 
                        self.getSkill(), 
                        self.getNextFreeHours(), 
                        self.getDailyMinutes(), 
                        self.getWeeklyHours()])
    
    ############################################################################
    ################################## STRING ##################################
    ############################################################################
    
    def __str__(self):
        """
        String representation of the doctor object.

        Ensures:
        String representation of the doctor.
        """
        # if the doctor has weekly pause
        if self.getNextFreeHours() == self.WKL_PAUSE:
            return f'{str(self.getName())}, {str(self.getSkill())}, ' \
                   f'{self.getNextFreeHours()}, {str(self.getDailyMinutes())}, ' \
                   f'{Helper().intToTime(*self.getWeeklyHours())}'
        # otherwise
        else:
            return f'{str(self.getName())}, {str(self.getSkill())}, ' \
                   f'{Helper().intToTime(*self.getNextFreeHours())}, ' \
                   f'{str(self.getDailyMinutes())}, ' \
                   f'{Helper().intToTime(*self.getWeeklyHours())}'
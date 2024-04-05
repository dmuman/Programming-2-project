# 2023-2024 Programação 2
# Grupo 25
# 59348 Dmytro Umanskyi
# 62235 Duarte Alberto

from Helper import Helper  # importing Helper

class Schedule:
    """
    Schedule class representing a schedule with attributes 
    such as schedule time, mother's name, and doctor's name.
    """
    # class variables (constants)
    HOURS_IDX = 0       # hours index
    MINUTES_IDX = 1     # minutes index

    ############################################################################
    ############################## INITIALIZATION ##############################
    ############################################################################

    def __init__(self, scheduleTime, motherName, doctorName):
        """
        Initializes a Schedule object.

        Requires:
        scheduleTime is a string that represents the time of the schedule.
        motherName is a string that represents the name of the mother.
        doctorName is a string that represents the name of the doctor.

        Ensures:
        A Schedule object is initialized with the specified attributes.
        """
        self._scheduleTime = scheduleTime
        self._motherName = motherName
        self._doctorName = doctorName
        self._schedule = [self.getScheduleTime(), self.getMotherName(), 
                          self.getDoctorName()]

    ############################################################################
    ################################# SETTERS ##################################
    ############################################################################

    def setScheduleTime(self, scheduleTime):
        """
        Sets the schedule time.

        Requires:
        scheduleTime is a string that represents the new schedule time.

        Ensures:
        The schedule time is updated.
        """
        self._scheduleTime = scheduleTime
    
    def setMotherName(self, motherName):
        """
        Sets the mother's name.

        Requires:
        motherName is a string that represents the new mother's name.

        Ensures:
        The mother's name is updated.
        """
        self._motherName = motherName

    def setDoctorName(self, doctorName):
        """
        Sets the doctor's name.

        Requires:
        doctorName is a string that represents the new doctor's name.

        Ensures:
        The doctor's name is updated.
        """
        self._doctorName = doctorName

    def setSchedule(self, schedule):
        """
        Sets the schedule.

        Requires:
        schedule is a list containing the attributes of the schedule.

        Ensures:
        The schedule is updated.
        """
        self._schedule = schedule

    ############################################################################
    ################################# GETTERS ##################################
    ############################################################################

    def getScheduleTime(self):
        """
        Gets the schedule time.

        Ensures:
        List in the format of [HH, MM], that represents the schedule time,
        using function from the Helper class.
        """
        return Helper().timeToInt(self._scheduleTime)
    
    def getMotherName(self):
        """
        Gets the mother's name.

        Ensures:
        String mother's name.
        """
        return self._motherName

    def getDoctorName(self):
        """
        Gets the doctor's name.

        Ensures:
        String doctor's name.
        """
        return self._doctorName
    
    def getSchedule(self):
        """
        Gets the schedule.

        Ensures:
        List containing the attributes of the schedule.
        """
        return self._schedule

    ############################################################################
    ################################ SORT KEYS #################################
    ############################################################################

    def sortSchedulesKeys(self):
        """
        Generates sorting keys for schedules basen on schedule time,
        mother's and doctor's names.

        Ensures:
        Tuple containing sorting keys for the schedule.
        Where:
        Schedule times are sorted in ascending order,
        mother's and doctor's names are sorted in alphabetical order.
        """
        # calculating total time
        totalTime = self.getScheduleTime()[0] * 60 + self.getScheduleTime()[1]
        return totalTime, self.getMotherName(), self.getDoctorName()
    
    ############################################################################
    ################################## STRING ##################################
    ############################################################################

    def __str__(self):
        """
        String representation of the schedule object.

        Ensures:
        String representation of the schedule.
        """
        return f'{Helper().intToTime(*self.getScheduleTime())}, ' \
               f'{str(self.getMotherName())}, {self.getDoctorName()}'
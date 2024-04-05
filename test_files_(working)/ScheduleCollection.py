from Schedule import Schedule   # importing Schedule
from Helper import Helper       # importing Helper
from copy import deepcopy       # importing deepcopy

class ScheduleCollection:
    """
    Schedule collection class representing a collection of schedules.
    """
    # declaring class variables (constants)
    REDIR_STR = 'redirected to other network'   # redirecting string
    HOURS_IDX = 0       # hours index
    MINUTES_IDX = 1     # minutes index
    TIME_HEAD_IDX = 3   # header time index

    ############################################################################
    ############################## INITIALIZATION ##############################
    ############################################################################
    
    def __init__(self, filename):
        """
        Initializes a ScheduleCollection object.
        Makes a collection of Schedule objects.
        Uses readFile method from the Helper class.

        Requires:
        filename is a string representing the name of the file 
        containing schedule data.
        File is in the same directory as the program in the .txt format.

        Ensures:
        Using readFile function from the Helper class,
        a ScheduleCollection object is initialized with the specified filename,
        header, time in header, and schedules data, which is a list, 
        containing Schedule objects.
        """
        self._filename = filename
        self._header, self._schedulesData = Helper().readFile(self.getFilename())
        self._headerTime = self._header[self.TIME_HEAD_IDX]
        self._schedules = []
        for data in self.getSchedulesData():
            scheduleTime, motherName, doctorName = data
            schedule = Schedule(scheduleTime, motherName, doctorName)
            self._schedules.append(schedule)

    ############################################################################
    ################################# SETTERS ##################################
    ############################################################################
    
    def setHeader(self, header):
        """
        Sets the header of the schedule collection.

        Requires:
        header is a list, representing the new header
        information to be set.

        Ensures:
        The header of the schedule collection is updated.
        """
        self._header = header

    def setHeaderTime(self, headerTime):
        """
        Updates header's time with the provided time.

        Requires:
        headerTime is a string representing the new 
        header's time to be set.

        Ensures:
        headerTime is updated by the provided time.
        """
        self.getHeader()[self.TIME_HEAD_IDX] = headerTime

    def setSchedulesData(self, schedulesData):
        """
        Sets the schedules' data of the schedule collection.

        Requires:
        schedulesData is a list, representing the new
        schedules' data to be set.

        Ensures:
        The schedules' data of the schedule collection is updated.
        """
        self._schedulesData = schedulesData

    def setSchedules(self, schedules):
        """
        Sets the list of schedules in the schedule collection.

        Requires:
        schedules is a list, representing the list of 
        Schedule objects to be set.

        Ensures:
        The list of schedules in the schedule collection is updated.
        """
        self._schedules = schedules


    ############################################################################
    ################################# GETTERS ##################################
    ############################################################################
    
    def getFilename(self):
        """
        Gets the filename of the schedule collection.

        Ensures:
        The filename of the schedule collection.
        """
        return self._filename
    
    def getHeader(self):
        """
        Gets the header of the schedule collection.

        Ensures:
        The header of the schedule collection.
        """
        return self._header
    
    def getHeaderTime(self):
        """
        Using a function from the Helper class, gets the time
        from the header.

        Ensures:
        List, containing the time from the header in the
        format of [HH, MM] 
        """
        return Helper().timeToInt(self._headerTime)

    def getSchedulesData(self):
        """
        Gets the schedules' data of the schedule collection.

        Ensures:
        The list of schedules' data of the schedule collection.
        """
        return self._schedulesData
    
    def getSchedules(self):
        """
        Gets the list of schedules in the schedule collection.

        Ensures:
        The list of schedules in the schedule collection.
        """
        return self._schedules

    ############################################################################
    ########################### HEADER TIME UPDATE #############################
    ############################################################################

    def updateHeadersTime(self, minutesToAdd):
        """
        Updates headers time by the given amount of minutes,
        using a function from the Helper class.

        Requires:
        minutesToAdd is an int.

        Ensures:
        Header's time is updated with the given amount of minutes.
        """
        self.setHeaderTime(Helper().updateHours(self._headerTime, minutesToAdd))

    ############################################################################
    ################################# SORTING ##################################
    ############################################################################

    def sortSchedules(self):
        """
        Sorts the list of schedules in the schedule collection based on predefined 
        in the Schedule class keys.

        Ensures:
        The list of schedules is sorted according to predefined sorting keys.
        """
        self.getSchedules().sort(key = Schedule.sortSchedulesKeys)
    
    ############################################################################
    ###################### UPDATING SCHEDULE AND DOCTORS #######################
    ############################################################################

    def updateSchedule(self, doctors, requests):
        """
        
        """
        # create a deepcopy of current schedules and clear it
        newScheduleList = deepcopy(self.getSchedules())
        newScheduleList.clear()

        # create a deepcopy of current doctors and clear it
        newDoctorsList = deepcopy(doctors)
        newDoctorsList.clear()

        # declaring variables for hours and minutes from the header
        hoursFromHeader, minutesFromHeader = self.getHeaderTime()

        # converting it string time using Helper's function
        timeFromHeader = Helper().intToTime(hoursFromHeader, minutesFromHeader)

        # declaring a variable for the next (new) time
        nextTime = Helper().updateHours(timeFromHeader, 30)

        # part for adding the appointment from the last schedule
        # if the time of the appointment is greater than the
        # updated time of schedule
        # searching through the previous schedule
        for appointment in self.getSchedules():
            # checking if its hours and minutes are greater than the new schedule
            if (appointment.getScheduleTime()[self.HOURS_IDX] >= \
                Helper().timeToInt(nextTime)[self.HOURS_IDX] and \
                    appointment.getScheduleTime()[self.MINUTES_IDX] >= \
                        Helper().timeToInt(nextTime)[self.MINUTES_IDX]):
                # if so => adding it to the new schedule
                newScheduleList.append(appointment)

                # searching through doctors
                for doctor in doctors:
                    # and new schedules
                    for newAppointment in newScheduleList:
                        # if doctor's name is in here => 
                        # he is added to the new doctors list
                        if doctor.getName() in newAppointment.getSchedule():
                            newDoctorsList.append(doctor)

        # part for redirecting to other network
        # if the appointment's time is greater than
        # 20 hours
        # searching through the new schedules
        for schedule in newScheduleList:
            # checking if updated hours from it are greater than 20
            if (schedule.getScheduleTime()[self.HOURS_IDX] * 60 + \
                schedule.getScheduleTime()[self.MINUTES_IDX] + 20 >= 20 * 60):
                # if so => assigned hours will be equal 
                # to the new schedule time in the header
                schedule.setScheduleTime(nextTime)

                # and doctor's name will be equal to
                # redirecting string
                schedule.setDoctorName(self.REDIR_STR)

                # setting the schedule
                schedule.setSchedule([schedule.getScheduleTime(), 
                                      schedule.getMotherName(), 
                                      schedule.getDoctorName()])

        # if the doctor is in the last schedule 
        # and the time of the appointment exceeds 
        # the time of the old schedule =>
        # => the doctor is occupied and is added to the new schedule
        # searching through doctors
        for doctor in doctors:
            # and schedules
            for schedule in self.getSchedules():
                # checing if doctor's name is in the last schedule
                # and the time of the appointment exceeds 
                # the time of the old schedule
                if (doctor.getName() in schedule.getSchedule()) and \
                    (schedule.getScheduleTime()[self.HOURS_IDX] * 60 + \
                     schedule.getScheduleTime()[self.MINUTES_IDX] > \
                        self.getHeaderTime()[0] * 60 + \
                            self.getHeaderTime()[self.MINUTES_IDX] + 30):
                    # if so => setting doctor's status to True
                    # which means he's occupied
                    doctor.setStatus(True)

        # part for assigning doctors to mothers
        # searching through mothers
        for mother in requests:
            # declaring variables for the name and the risk level
            motherName = mother.getName()
            riskLevel = mother.getRiskLevel()

            # part for findind a suitable doctor for the current mother
            # declaring a variable for the suitable doctor
            suitableDoctor = None

            # searching through doctors
            for doctor in doctors:
                
                if doctor.getSkill() >= 2 and riskLevel == 'high' and not doctor.getStatus():
                    suitableDoctor = doctor
                    break
                elif doctor.getSkill() >= 1 and riskLevel == 'low' and not doctor.getStatus():
                    suitableDoctor = doctor
                    break

            if suitableDoctor:
                doctor.setStatus(True)  # Mark the doctor as assigned
                
                assignedHours = suitableDoctor.getNextFreeHours()
                assignedDoctor = suitableDoctor.getName()

                if assignedHours[self.HOURS_IDX]*60 + assignedHours[self.MINUTES_IDX] < Helper().timeToInt(nextTime)[self.HOURS_IDX]*60 + Helper().timeToInt(nextTime)[self.MINUTES_IDX]:    #checks if the assigned hours are less than the updated time of the schedule
                    assignedHours = Helper().timeToInt(nextTime)

                appointment = Schedule(Helper().intToTime(assignedHours[self.HOURS_IDX], assignedHours[self.MINUTES_IDX]), motherName, assignedDoctor)
                newScheduleList.append(appointment)

                doctor.updateDoctorsTime(20)
                newDoctorsList.append(doctor)
            else:
                # If no suitable doctor found, redirect the request
                appointment = Schedule(nextTime, motherName, self.REDIR_STR)
                newScheduleList.append(appointment)

        newScheduleList.sort(key = Schedule.sortSchedulesKeys)
        newDoctorsList.sort(key = lambda x: x.getName())


        return [newScheduleList, newDoctorsList]
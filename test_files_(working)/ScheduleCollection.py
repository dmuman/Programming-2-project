# 2023-2024 Programação 2
# Grupo 25
# 59348 Dmytro Umanskyi
# 62235 Duarte Alberto

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
        Updates the schedule and doctors, based on given list of
        doctors and requests and on the previous schedule.
        Assigns mothers to suitable doctors.
        Redirecting to other network if necessary.

        Requires:
        doctors is a list that contains information
        about previous doctors states. (DoctorCollection)
        requests is a list that contains information
        about requests. (MotherCollection)

        Ensures:
        list that contains a list with updated schedules (Schedule classes)
        and a list with updated doctors (Doctor classes).
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
                # checking if the doctor's skill is high enough
                # work with high risk level
                # and if the doctor is not assigned 
                if doctor.getSkill() >= 2 and riskLevel == 'high' and \
                    not doctor.getStatus():
                    # if there is such a doctor =>
                    # he becomes suitable
                    suitableDoctor = doctor
                    # breaking the search 
                    break
                # searching free doctors with basic skill
                # and mother with low risk
                elif doctor.getSkill() >= 1 and riskLevel == 'low' and \
                    not doctor.getStatus():
                    # assigning suitable doctor
                    suitableDoctor = doctor
                    # breaking the search
                    break

            # in case suitable doctor is found
            if suitableDoctor:
                # his status is now True (assigned)
                doctor.setStatus(True)
                
                # assigning hours and doctor to the mother
                assignedHours = suitableDoctor.getNextFreeHours()
                assignedDoctor = suitableDoctor.getName()

                # checking if the assigned hours are less than the updated time of the schedule 
                if assignedHours[self.HOURS_IDX]*60 + assignedHours[self.MINUTES_IDX] < \
                    Helper().timeToInt(nextTime)[self.HOURS_IDX]*60 + \
                        Helper().timeToInt(nextTime)[self.MINUTES_IDX]:
                    # if so, assigned hours are now equal
                    # to the nextTime
                    # (new schedule's time)
                    assignedHours = Helper().timeToInt(nextTime)

                # making an appointment
                appointment = Schedule(Helper().intToTime(assignedHours[self.HOURS_IDX], 
                                                          assignedHours[self.MINUTES_IDX]), 
                                                          motherName, 
                                                          assignedDoctor)
                # appending new schedules list
                newScheduleList.append(appointment)

                # updating suitable doctor's time
                # by 20 minutes (appointment duration)
                doctor.updateDoctorsTime(20)
                # appending the new list of doctors 
                newDoctorsList.append(doctor)
            # If no suitable doctor found => redirect the mother
            else:
                # making schedule with the time of the new schedule
                # and doctor's name that equals to the 
                # redirection string
                appointment = Schedule(nextTime, motherName, self.REDIR_STR)

                # appending new appointments list
                newScheduleList.append(appointment)

        # sorting schedules with the keys from Schedule class
        newScheduleList.sort(key = Schedule.sortSchedulesKeys)
        # sorting doctors by their names
        # (alphabetical order)
        newDoctorsList.sort(key = lambda x: x.getName())

        # returniing a list with updated schedules and doctors
        return [newScheduleList, newDoctorsList]
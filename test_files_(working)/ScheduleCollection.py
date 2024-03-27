from Schedule import *
from DoctorCollection import *
from MotherCollection import *
from Helper import *
from copy import deepcopy

class ScheduleCollection:
    REDIR_STR = 'redirected to other network'
    TIME_HEAD_IDX = 3
    HOURS_IDX = 0
    MINUTES_IDX = 1
    def __init__(self, filename):
        self._filename = filename
        self._header, self._schedulesData = self.readFile()
        self._headerTime = self._header[self.TIME_HEAD_IDX]
        self._schedules = []
        for data in self.getSchedulesData():
            scheduleTime, motherName, doctorName = data
            schedule = Schedule(scheduleTime, motherName, doctorName)
            self._schedules.append(schedule)

    def getFilename(self):
        return self._filename

    def readFile(self):
        with open(self.getFilename(), 'r', encoding='utf-8') as inFile:
            lines = inFile.readlines()

            header = [line.rstrip() for line in lines[:7] if line.strip()]

            schedulesData = [line.strip().split(", ") for line in lines[7:] if line.strip()]

        return header, schedulesData
    
    def setHeader(self, header):
        self._header = header

    def setSchedulesData(self, schedulesData):
        self._schedulesData = schedulesData

    def setSchedules(self, schedules):
        self._schedules = schedules

    def getHeader(self):
        return self._header

    def getSchedulesData(self):
        return self._schedulesData
    
    def getSchedules(self):
        return self._schedules

    def sortSchedules(self):
        self.getSchedules().sort(key = Schedule.sortSchedulesKeys)

    def timeToInt(self, time):
        t = time.split("h")
        hours = int(t[self.HOURS_IDX])
        minutes = int(t[self.MINUTES_IDX])

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
    
    def getHeaderTime(self):
        return self.timeToInt(self._headerTime)

    def updateHours(self, hoursToUpdate, minutesToAdd):
        #declaring variables for holding the int representatin of hours, minutes and total minutes
        intHours = None 
        intMinutes = None
        totalMinutes = None

        #declaring variable for the new, updated hours
        updatedHours = None

        #in case new minutes are greater than 60
        if self.timeToInt(hoursToUpdate)[self.MINUTES_IDX] + minutesToAdd > 60:
            intHours = self.timeToInt(hoursToUpdate)[self.HOURS_IDX]                                   #assigning hours
            intMinutes = self.timeToInt(hoursToUpdate)[self.MINUTES_IDX]                               #assigning minutes
            totalMinutes = intHours * 60 + intMinutes + minutesToAdd                    #new totalMinutes
            updatedHours = self.intToTime((totalMinutes // 60), (totalMinutes % 60))    #new, updated hours, based on totalMinutes

        #in case new minutes are equal 60
        elif self.timeToInt(hoursToUpdate)[self.MINUTES_IDX] + minutesToAdd == 60:
            intHours = self.timeToInt(hoursToUpdate)[self.HOURS_IDX] + 1                   #updating hours(adding 1 hour)
            intMinutes = 0                                                  #updating minutes(equal 00)
            updatedHours = self.intToTime(intHours, intMinutes)             #new, updated hours

        #in case new minutes are less than 60
        else:
            intHours = self.timeToInt(hoursToUpdate)[self.HOURS_IDX]                       #assigning hours. they remain the same
            intMinutes = self.timeToInt(hoursToUpdate)[self.MINUTES_IDX] + minutesToAdd    #updating minutes with minutesToAdd
            updatedHours = self.intToTime(intHours, intMinutes)             #new, updated hours
        return updatedHours

    def updateSchedule(self, doctors, requests):
        newScheduleList = deepcopy(self.getSchedules())  # Create a deep copy of current schedules
        newScheduleList.clear()  # Clear the new schedule list
        newDoctorsList = deepcopy(doctors)
        newDoctorsList.clear()

        hoursFromHeader, minutesFromHeader = self.getHeaderTime()
        timeFromHeader = self.intToTime(hoursFromHeader, minutesFromHeader)
        nextTime = self.updateHours(timeFromHeader, 30)  # Get the updated time

        for appointment in self.getSchedules():  # Reading and searching through the previous schedule
            if appointment.getScheduleTime()[0] >= self.timeToInt(nextTime)[self.HOURS_IDX] and appointment.getScheduleTime()[1] >= self.timeToInt(nextTime)[self.MINUTES_IDX]:  # Checks if its hours and minutes are greater than the new schedule
                newScheduleList.append(appointment)
                for doctor in doctors:
                    for newAppointment in newScheduleList:
                        if doctor.getName() in newAppointment.getSchedule():
                            newDoctorsList.append(doctor)

        for schedule in newScheduleList:
            if schedule.getScheduleTime()[0] * 60 + schedule.getScheduleTime()[1] + 20 >= 20 * 60:  # Checks if updated hours from it are greater than 20
                schedule.setScheduleTime(nextTime)  # Assigned hours will be equal to the new schedule time in the header
                schedule.setDoctorName(self.REDIR_STR)
                schedule.setSchedule([schedule.getScheduleTime(), schedule.getMotherName(), schedule.getDoctorName()])

        # If the doctor is in the last schedule and the time of the appointment exceeds the time of the old schedule =>
        # => the doctor is occupied and is added to the new schedule
        for doctor in doctors:
            for schedule in self.getSchedules():
                if (doctor.getName() in schedule.getSchedule()) and (schedule.getScheduleTime()[0] * 60 + schedule.getScheduleTime()[1] > self.getHeaderTime()[0] * 60 + self.getHeaderTime()[1] + 30):
                    doctor.setStatus(True)

        for mother in requests:
            motherName = mother.getName()
            riskLevel = mother.getRiskLevel()

            # Find a suitable doctor for the current mother
            suitableDoctor = None
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

                if assignedHours[0]*60 + assignedHours[1] < self.timeToInt(nextTime)[self.HOURS_IDX]*60 + self.timeToInt(nextTime)[self.MINUTES_IDX]:    #checks if the assigned hours are less than the updated time of the schedule
                    assignedHours = self.timeToInt(nextTime)

                appointment = Schedule(self.intToTime(assignedHours[0], assignedHours[1]), motherName, assignedDoctor)
                newScheduleList.append(appointment)

                doctor.updateDoctorsTime(20)
                newDoctorsList.append(doctor)
            else:
                # If no suitable doctor found, redirect the request
                appointment = Schedule(nextTime, motherName, self.REDIR_STR)
                newScheduleList.append(appointment)

        newScheduleList.sort(key=Schedule.sortSchedulesKeys)
        newDoctorsList.sort(key = lambda x: x.getName())


        return newScheduleList, newDoctorsList


schedules = ScheduleCollection('txt_files/testSet2/schedule14h00.txt')
schedules.sortSchedules()

doctors = DoctorCollection('txt_files/testSet2/doctors14h00.txt')
doctors.sortDoctors()
doctorsList = doctors.getDoctors()
print(doctorsList)

requests = MotherCollection('txt_files/testSet2/requests14h30.txt')
requests.sortMothers()
requestsList = requests.getMothers()
print(requestsList)

for app in schedules.updateSchedule(doctorsList, requestsList):
    print(app)
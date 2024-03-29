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
    
    def getHeaderTime(self):
        return Helper().timeToInt(self._headerTime)

    def updateSchedule(self, doctors, requests):
        newScheduleList = deepcopy(self.getSchedules())  # Create a deep copy of current schedules
        newScheduleList.clear()  # Clear the new schedule list
        newDoctorsList = deepcopy(doctors)
        newDoctorsList.clear()

        hoursFromHeader, minutesFromHeader = self.getHeaderTime()
        timeFromHeader = Helper().intToTime(hoursFromHeader, minutesFromHeader)
        nextTime = Helper().updateHours(timeFromHeader, 30)  # Get the updated time

        for appointment in self.getSchedules():  # Reading and searching through the previous schedule
            if appointment.getScheduleTime()[self.HOURS_IDX] >= Helper().timeToInt(nextTime)[self.HOURS_IDX] and appointment.getScheduleTime()[self.MINUTES_IDX] >= Helper().timeToInt(nextTime)[self.MINUTES_IDX]:  # Checks if its hours and minutes are greater than the new schedule
                newScheduleList.append(appointment)
                for doctor in doctors:
                    for newAppointment in newScheduleList:
                        if doctor.getName() in newAppointment.getSchedule():
                            newDoctorsList.append(doctor)

        for schedule in newScheduleList:
            if schedule.getScheduleTime()[self.HOURS_IDX] * 60 + schedule.getScheduleTime()[self.MINUTES_IDX] + 20 >= 20 * 60:  # Checks if updated hours from it are greater than 20
                schedule.setScheduleTime(nextTime)  # Assigned hours will be equal to the new schedule time in the header
                schedule.setDoctorName(self.REDIR_STR)
                schedule.setSchedule([schedule.getScheduleTime(), schedule.getMotherName(), schedule.getDoctorName()])

        # If the doctor is in the last schedule and the time of the appointment exceeds the time of the old schedule =>
        # => the doctor is occupied and is added to the new schedule
        for doctor in doctors:
            for schedule in self.getSchedules():
                if (doctor.getName() in schedule.getSchedule()) and (schedule.getScheduleTime()[self.HOURS_IDX] * 60 + schedule.getScheduleTime()[self.MINUTES_IDX] > self.getHeaderTime()[0] * 60 + self.getHeaderTime()[self.MINUTES_IDX] + 30):
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

        newScheduleList.sort(key=Schedule.sortSchedulesKeys)
        newDoctorsList.sort(key = lambda x: x.getName())


        return newScheduleList, newDoctorsList


schedules = ScheduleCollection('txt_files/testSet1/schedule10h00.txt')
schedules.sortSchedules()

doctors = DoctorCollection('txt_files/testSet1/doctors10h00.txt')
doctors.sortDoctors()
doctorsList = doctors.getDoctors()
print(doctorsList)

requests = MotherCollection('txt_files/testSet1/requests10h30.txt')
requests.sortMothers()
requestsList = requests.getMothers()
print(requestsList)

for app in schedules.updateSchedule(doctorsList, requestsList):
    for elem in app:
        print(elem)
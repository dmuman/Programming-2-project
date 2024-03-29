from Helper import *

class Schedule:
    HOURS_IDX = 0
    MINUTES_IDX = 1
    def __init__(self, scheduleTime, motherName, doctorName):
        self._scheduleTime = scheduleTime
        self._motherName = motherName
        self._doctorName = doctorName
        self._schedule = [self.getScheduleTime(), self.getMotherName(), self.getDoctorName()]

    def setScheduleTime(self, scheduleTime):
        self._scheduleTime = scheduleTime
    
    def setMotherName(self, motherName):
        self._motherName = motherName

    def setDoctorName(self, doctorName):
        self._doctorName = doctorName

    def setSchedule(self, schedule):
        self._schedule = schedule

    def getScheduleTime(self):
        return Helper().timeToInt(self._scheduleTime)
    
    def getMotherName(self):
        return self._motherName

    def getDoctorName(self):
        return self._doctorName
    
    def getSchedule(self):
        return self._schedule

    def sortSchedulesKeys(self):

        totalTime = self.getScheduleTime()[0]*60 + self.getScheduleTime()[1]

        return totalTime, self.getMotherName(), self.getDoctorName()
    
    def __repr__(self):
        return str(self.getSchedule())
    
    def __str__(self):
        return f'{Helper().intToTime(*self.getScheduleTime())}, {str(self.getMotherName())}, {self.getDoctorName()}'
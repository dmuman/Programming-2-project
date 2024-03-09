from ScheduleTest import *

class ScheduleCollectionTest:
    def __init__(self, filename):
        self._filename = filename
        self._header, self._schedulesData = self.readFile()
        self._schedules = []
        for data in self.getSchedulesData():
            scheduleTime, motherName, doctorName = data
            schedule = ScheduleTest(scheduleTime, motherName, doctorName)
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
        self.getSchedules().sort(key = ScheduleTest.sortSchedulesKeys)

    def items(self):
        for elem in self._schedules:
            yield elem

    #TODO

    def writeSchedulesFile(self):
        pass

#if doctor is not already assigned => we can assign him to mother in schedule and update the time. Can check it in the schedule
#if he was assigned before => do not update him(and do not assign to mother). Just add his old assigment to the new schedule

mothers = ScheduleCollectionTest('schedule10h00.txt')
print(mothers.getHeader())
print(mothers.getSchedulesData())
print(mothers.getSchedules())

mothers.sortSchedules()
print(mothers.getSchedules())

for schedule in mothers.getSchedules():
    print(type(schedule))
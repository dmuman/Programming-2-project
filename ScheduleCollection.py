from Helpers import *

class ScheduleCollection:
    def __init__(self, filename):
        inFile = Helpers.removeHeader(open(filename, 'r', encoding='utf-8'))
        self._schedules = []
        for line in inFile:
            schedulesData = line.rstrip().split(", ")
            if len(schedulesData) != 1:                                       
                self._schedules.append(schedulesData)
    
    def setSchedules(self, schedules):
        self._schedules = schedules

    def getSchedules(self):
        return self._schedules

    #string
    def __str__(self):
        
        return f'{self.getSchedules()}'
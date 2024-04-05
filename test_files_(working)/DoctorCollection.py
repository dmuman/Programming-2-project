from Doctor import *
from Helper import *

class DoctorCollection:
    """
    Doctor collection class
    """
    HOURS_IDX = 0
    MINUTES_IDX = 1
    TIME_HEAD_IDX = 3
    NUM_HEAD_LINES = 7
    def __init__(self, filename):
        self._filename = filename
        self._header, self._doctorsData = Helper().readFile(self.getFilename())
        self._headerTime = self._header[self.TIME_HEAD_IDX]
        self._doctors = []
        for data in self.getDoctorsData():
            name, skill, nextFreeHours, dailyMinutes, weeklyHours = data
            doctor = Doctor(name, skill, nextFreeHours, dailyMinutes, weeklyHours)
            self._doctors.append(doctor)

    # setters
    def setHeader(self, header):
        self._header = header

    def setHeaderTime(self, headerTime):
        self.getHeader()[self.TIME_HEAD_IDX] = headerTime

    def setDoctorsData(self, doctorsData):
        self._doctorsData = doctorsData

    def setDoctors(self, doctors):
        self._doctors = doctors

    # getters
    def getFilename(self):
        return self._filename
    
    def getHeader(self):
        return self._header
    
    def getHeaderTime(self):
        return Helper().timeToInt(self._headerTime)

    def getDoctorsData(self):
        return self._doctorsData
    
    def getDoctors(self):
        return self._doctors

    # updating header's time
    def updateHeadersTime(self, minutesToAdd):
        self.setHeaderTime(Helper().updateHours(self._headerTime, minutesToAdd))
        self.getHeader
    
    # sorting doctors data by the keys from the Doctor class
    def sortDoctors(self):
        self.getDoctors().sort(key = Doctor.sortDoctorsKeys)
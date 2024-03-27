from Doctor import *

class DoctorCollection:
    TIME_HEAD_IDX = 3
    NUM_HEAD_LINES = 7
    HOURS_IDX = 0
    MINUTES_IDX = 1
    def __init__(self, filename):
        self._filename = filename
        self._header, self._doctorsData = self.readFile()
        self._headerTime = self._header[self.TIME_HEAD_IDX]
        self._doctors = []
        for data in self.getDoctorsData():
            name, skill, nextFreeHours, dailyMinutes, weeklyHours = data
            doctor = Doctor(name, skill, nextFreeHours, dailyMinutes, weeklyHours)
            self._doctors.append(doctor)

    def getFilename(self):
        return self._filename

    def readFile(self):
        with open(self.getFilename(), 'r', encoding='utf-8') as inFile:
            lines = inFile.readlines()

            header = [line.rstrip() for line in lines[:self.NUM_HEAD_LINES] if line.strip()]

            doctorsData = [line.strip().split(", ") for line in lines[self.NUM_HEAD_LINES:] if line.strip()]

        return header, doctorsData
    
    def setHeader(self, header):
        self._header = header

    def setHeaderTime(self, headerTime):
        self._headerTime = headerTime

    def setDoctorsData(self, doctorsData):
        self._doctorsData = doctorsData

    def setDoctors(self, doctors):
        self._doctors = doctors

    def getHeader(self):
        return self._header
    
    def getHeaderTime(self):
        return self.timeToInt(self._headerTime)

    def getDoctorsData(self):
        return self._doctorsData
    
    def getDoctors(self):
        return self._doctors

    def sortDoctors(self):
        self.getDoctors().sort(key = Doctor.sortDoctorsKeys)

    def timeToInt(self, time):
        t = time.split("h")
        hours = int(t[self.HOURS_IDX])
        minutes = int(t[self.MINUTES_IDX])

        return [hours, minutes]
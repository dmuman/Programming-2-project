from Helpers import *

class DoctorCollection:
    def __init__(self, filename):
        self._filename = filename
        self._header = Helpers.saveHeader(filename)
        inFile = Helpers.removeHeader(open(filename, 'r', encoding='utf-8'))
        self._doctors = []
        for line in inFile:
            doctorsData = line.rstrip().split(", ")
            if len(doctorsData) != 1:                                       
                self._doctors.append(doctorsData)

    def setDoctors(self, doctors):
        self._doctors = doctors

    def setHeader(self, header):
        self._header = header

    def getDoctors(self):
        return self._doctors
    
    def getHeader(self):
        return self._header

    #string
    def __str__(self):
        
        return f'{self.getDoctors()}'
    
    
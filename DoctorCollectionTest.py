from DoctorTest import *

class DoctorCollectionTest:
    def __init__(self, filename):
        self._filename = filename
        self._header, self._doctorsData = self.readFile()
        self._doctors = []
        for data in self.getDoctorsData():
            name, skill, nextFreeHours, dailyMinutes, weeklyHours = data
            doctor = DoctorTest(name, skill, nextFreeHours, dailyMinutes, weeklyHours)
            self._doctors.append(doctor)

    def getFilename(self):
        return self._filename

    def readFile(self):
        with open(self.getFilename(), 'r', encoding='utf-8') as inFile:
            lines = inFile.readlines()

            header = [line.rstrip() for line in lines[:7] if line.strip()]

            doctorsData = [line.strip().split(", ") for line in lines[7:] if line.strip()]

        return header, doctorsData
    
    def setHeader(self, header):
        self._header = header

    def setDoctorsData(self, doctorsData):
        self._doctorsData = doctorsData

    def setDoctors(self, doctors):
        self._doctors = doctors

    def getHeader(self):
        return self._header

    def getDoctorsData(self):
        return self._doctorsData
    
    def getDoctors(self):
        return self._doctors
    
    #TODO

    def sortDoctors(self):
        pass

    def writeDoctorsFile(self):
        pass
    
doctors = DoctorCollectionTest('doctors10h00.txt')
print(doctors.getHeader())
print(doctors.getDoctorsData())
print(doctors.getDoctors())


print(doctors.getDoctors()[1].__lt__(doctors.getDoctors()[0]))
print(doctors.getDoctors()[0].__eq__(doctors.getDoctors()[1]))
#for doctor in doctors.getDoctors():
#   print(type(doctor))
from DoctorTest import *

class DoctorCollectionTest:
    def __init__(self, filename):
        self._filename = filename
        self._header, self._doctorsData = self.readFile()

    def getFilename(self):
        return self._filename

    def readFile(self):
        with open(self.getFilename(), 'r', encoding='utf-8') as inFile:
            lines = inFile.readlines()
            #print(lines)

            header = [line.rstrip() for line in lines[:7] if line.strip()]

            doctorsData = [line.strip().split(", ") for line in lines[7:] if line.strip()]

        return header, doctorsData
    
    def getHeader(self):
        return self._header

    def getDoctorsData(self):
        return self._doctorsData
    
    def getDoctors(self):
        doctors = []
        for data in self.getDoctorsData():
            name, skill, nextFreeHours, dailyMinutes, weeklyHours = data
            doctor = DoctorTest(name, int(skill), nextFreeHours, int(dailyMinutes), weeklyHours)
            doctors.append(doctor)

        return doctors
    
doctors = DoctorCollectionTest('doctors10h00.txt')
print(doctors.getHeader())
print(doctors.getDoctorsData())
print(doctors.getDoctors())
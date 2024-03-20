from DoctorTest import *

class DoctorCollectionTest:
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
            doctor = DoctorTest(name, skill, nextFreeHours, dailyMinutes, weeklyHours)
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
        self.getDoctors().sort(key = DoctorTest.sortDoctorsKeys)

    def timeToInt(self, time):
        t = time.split("h")
        hours = int(t[self.HOURS_IDX])
        minutes = int(t[self.MINUTES_IDX])

        return [hours, minutes]

    #TODO

    def writeDoctorsFile(self):
        pass

    def updateDoctors(self):
        doctorList = self.getDoctors()                         
        headerTime = self.getHeaderTime()                                   #declaring variable for the time in header

        for doctor in doctorList:                                           #searching through doctors list

            #if (doctor.getNextFreeHours()[0] * 60 + \
            #    doctor.getNextFreeHours()[1]) > ((headerTime[0]+1) * 60):
            #    doctor.setStatus(True)

            if (doctor.getNextFreeHours()[DoctorTest.HOURS_IDX] * 60 + \
                doctor.getNextFreeHours()[DoctorTest.MINUTES_IDX]) < ((headerTime[DoctorTest.HOURS_IDX]+1) * 60):   #checks if doctor's old free hours are less than time in the header of old doctors file
                
                doctor.updateDoctorsTime(20)                                #if so, updating his info with updateDoctorsTime() function

#if doctor is not already assigned => we can assign him to mother in schedule and update the time. Can check it in the schedule
#if he was assigned before => do not update him(and do not assign to mother). Just add his old assigment to the new schedule
    
#doctors = DoctorCollectionTest('doctors10h00.txt')
#doctors.sortDoctors()
#print(doctors.getDoctors())
#doctors.updateDoctors()
#print(doctors.getDoctors())
#for doctor in doctors.getDoctors():
#    print(doctor.getStatus())

#print(doctors.getDoctors()[1].__lt__(doctors.getDoctors()[0]))
#print(doctors.getDoctors()[0].__eq__(doctors.getDoctors()[1]))

#якщо час доктора в розкладі більший, ніж час наступного розкладу - він зайнятий. його час не оновлюється, він нікому не приписується
                
#doctors = DoctorCollectionTest('test_files_(working)\doctors10h00.txt')
#print(doctors.getDoctors())
#
#doctors.updateDoctors()
#
#print(doctors.getDoctors())

#print(doctors.getDoctors())
#for doctor in doctors.getDoctors():
    #print(type(doctor))
    #for info in doctor.getDoctor():
    #    print(info)
#    print(doctor)

#    doctor.updateDoctorsTime(20)
#    print(doctor)
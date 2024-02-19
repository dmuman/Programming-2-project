from DoctorTest import *

class DoctorCollectionTest:
    def __init__(self, filename):
        self._filename = filename
        self._header, self._doctorsData = self.readFile()
        self._headerTime = self._header[3]
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

    def items(self):
        for elem in self._doctors:
            yield elem

    def timeToInt(self, time):
        t = time.split("h")
        hours = int(t[0])
        minutes = int(t[1])

        return [hours, minutes]

    #TODO

    def writeDoctorsFile(self):
        pass

    def updateDoctors(doctors):
        """
        Update the doctors information taking into account a previous doctors information.
        
        Requires:
        doctors is a list of lists with the structure as in the output of
        infoFromFiles.readDoctorsFile concerning the time of previous schedule;
        
        Ensures:
        a list of doctors, representing the doctors updated at
        the current update time (= previous update time + 30 minutes),
        according to the conditions indicated in the general specification
        of the project (omitted here for the sake of readability).
        """
        doctorList = readDoctorsFile(doctors)                           #declaring variable and storing info from doctors file using readDoctorsFile() function from the infoFromFiles module
        timeInHeader = saveHeader(doctors)[HEADER_TIME_IDX][0]          #declaring variable for the time in header
        newDoctors = []                                                 #declaring list for new doctors

        for doctor in doctorList:                                       #searching through doctors list
            if hourToInt(doctor[DOCT_BIRTH_END_IDX])*60 + \
                minutesToInt(doctor[DOCT_BIRTH_END_IDX]) < (hourToInt(timeInHeader)+1)*60:  #checks if doctor's old free hours are less than time in the header of old doctors file
                
                doctor = updateDoctorsTime(doctor, 20)      #if so, updating his info with updateDoctorsTime() function
                newDoctors.append(doctor)                   #appending new doctors file
            else:                                           #checks if doctor's old free hours are greater than time in the header of old doctors file
                newDoctors.append(doctor)                   #keeping his old free hours and appending new doctors file

        return newDoctors 
    
doctors = DoctorCollectionTest('doctors10h00.txt')
print(doctors.getHeaderTime())
#print(doctors.getHeader())
#print(doctors.getDoctorsData())
#print(doctors.getDoctors())
#
doctors.sortDoctors()
#print(doctors.getDoctors())
#
#for doctor in doctors.getDoctors():
#    print(doctor)
#    doctor.updateDoctorsTime(20)
#    print(doctor)
#
print(doctors.getDoctors())
newDoctors = []                                                 #declaring list for new doctors

for doctor in doctors.getDoctors():                                  #searching through doctors list
    if (doctor.getNextFreeHours()[0] * 60 + doctor.getNextFreeHours()[1]) < ((doctors.getHeaderTime()[0]+1) * 60):  #checks if doctor's old free hours are less than time in the header of old doctors file
        
        doctor.updateDoctorsTime(20)      #if so, updating his info with updateDoctorsTime() function
        newDoctors.append(doctor)                   #appending new doctors file
    else:                                           #checks if doctor's old free hours are greater than time in the header of old doctors file
        newDoctors.append(doctor)


print(newDoctors)

#print(doctors.getDoctors()[1].__lt__(doctors.getDoctors()[0]))
#print(doctors.getDoctors()[0].__eq__(doctors.getDoctors()[1]))
#for doctor in doctors.getDoctors():
#   print(type(doctor))
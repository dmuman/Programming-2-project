from Schedule import *
from DoctorCollection import *
from MotherCollection import *
from Helper import *
from copy import deepcopy

class ScheduleCollection:
    REDIR_STR = 'redirected to other network'
    TIME_HEAD_IDX = 3
    def __init__(self, filename):
        self._filename = filename
        self._header, self._schedulesData = self.readFile()
        self._headerTime = self._header[self.TIME_HEAD_IDX]
        self._schedules = []
        for data in self.getSchedulesData():
            scheduleTime, motherName, doctorName = data
            schedule = Schedule(scheduleTime, motherName, doctorName)
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
        self.getSchedules().sort(key = Schedule.sortSchedulesKeys)

    def items(self):
        for elem in self._schedules:
            yield elem

    def oldScheduleToNew(self):
        newScheduleList = []
        for appointment in self.getSchedules():                             #reading and searching through the previous schedule
            if appointment.getScheduleTime()[0] >= 10\
                and appointment.getScheduleTime()[1] >= 30:           #checks if its hours and minutes are greater than the new schedule
                newScheduleList.append(appointment)
        return newScheduleList
    
    def redirecting(self):
        #redirecter if hours > 20 or there're no free doctors
        for schedule in self.oldScheduleToNew():                         #reading and searching through the previous schedule
            print(type(schedule))
            if schedule.getScheduleTime()[0]*60 + schedule.getScheduleTime()[1] + 20 >= 20*60:                    #ckecks if updated hours from it are greater than 20
                schedule.setScheduleTime('10h00')   #assigned hours will be equal to the new schedule time in the header
                schedule.setDoctorName(self.REDIR_STR)
                schedule.setSchedule([schedule.getScheduleTime(), schedule.getMotherName(), schedule.getDoctorName()])
                print(schedule.getSchedule())

    def timeToInt(self, time):
        return [self.hoursToInt(time), self.minutesToInt(time)]
    
    def hoursToInt(self, time):
        t = time.split("h")
        hours = int(t[0])

        return hours
    
    def minutesToInt(self, time):
        t = time.split("h")
        minutes = int(t[1])

        return minutes
    
    def intToTime(self, hour, minutes):
        h = str(hour)
        m = str(minutes)

        if hour < 10:
            h = "0" + h

        if minutes < 10 or minutes == 0:
            m = "0" + m

        time = f"{h}h{m}"

        return time
    
    def getHeaderTime(self):
        return self.timeToInt(self._headerTime)

    def updateHours(self, hoursToUpdate, minutesToAdd):
        #declaring variables for holding the int representatin of hours, minutes and total minutes
        intHours = None 
        intMinutes = None
        totalMinutes = None
        #declaring variable for the new, updated hours
        updatedHours = None
        #in case new minutes are greater than 60
        if self.minutesToInt(hoursToUpdate) + minutesToAdd > 60:
            intHours = self.hoursToInt(hoursToUpdate)                                #assigning hours
            intMinutes = self.minutesToInt(hoursToUpdate)                            #assigning minutes
            totalMinutes = intHours * 60 + intMinutes + minutesToAdd            #new totalMinutes
            updatedHours = self.intToTime((totalMinutes // 60), (totalMinutes % 60)) #new, updated hours, based on totalMinutes
        #in case new minutes are equal 60
        elif self.minutesToInt(hoursToUpdate) + minutesToAdd == 60:
            intHours = self.hoursToInt(hoursToUpdate) + 1         #updating hours(adding 1 hour)
            intMinutes = 0                                  #updating minutes(equal 00)
            updatedHours = self.intToTime(intHours, intMinutes)  #new, updated hours
        #in case new minutes are less than 60
        else:
            intHours = self.hoursToInt(hoursToUpdate)                     #assigning hours. they remain the same
            intMinutes = self.minutesToInt(hoursToUpdate) + minutesToAdd #updating minutes with minutesToAdd
            updatedHours = self.intToTime(intHours, intMinutes)          #new, updated hours
        return updatedHours
            
    def updateSchedule(self, doctors, requests):
        assignedHours = None
        assignedDoctor = None
        newScheduleList = deepcopy(self.getSchedules())
        newScheduleList.clear()
        assignedDoctors = []
        hoursFromHeader, minutesFromHeader = self.getHeaderTime()
        timeFromHeader = self.intToTime(hoursFromHeader, minutesFromHeader)
        nextTime = self.updateHours(timeFromHeader, 30)

        for appointment in self.getSchedules():                             #reading and searching through the previous schedule
            if appointment.getScheduleTime()[0] >= self.hoursToInt(self.intToTime(*self.getHeaderTime()))\
                and appointment.getScheduleTime()[1] >= self.minutesToInt(self.intToTime(*self.getHeaderTime())):           #checks if its hours and minutes are greater than the new schedule
                newScheduleList.append(appointment)
        
        for schedule in newScheduleList:
            if schedule.getScheduleTime()[0]*60 + schedule.getScheduleTime()[1] + 20 >= 20*60:                    #ckecks if updated hours from it are greater than 20
                schedule.setScheduleTime(nextTime)   #assigned hours will be equal to the new schedule time in the header
                schedule.setDoctorName(self.REDIR_STR)
                schedule.setSchedule([schedule.getScheduleTime(), schedule.getMotherName(), schedule.getDoctorName()])

        # if the doctor is in the last schedule and the time of the appointment exceeds the time of the old schedule => 
        # => the doctor is occupied and is added to the new schedule
        for doctor in doctors:
            for schedule in self.getSchedules():
                if (doctor.getName() in schedule.getSchedule()) and (schedule.getScheduleTime()[0]*60 + schedule.getScheduleTime()[1] > self.getHeaderTime()[0]*60 + self.getHeaderTime()[1]+30):
                    doctor.setStatus(True)
            if doctor.getStatus():
                assignedDoctors.append(doctor.getName())

        for mother in requests:
            for doctor in doctors:
                if ((mother.getRiskLevel() == "high" and doctor.getSkill() >= 2 and not doctor.getStatus())
                or (mother.getRiskLevel() == "low" and doctor.getSkill() >= 1 and not doctor.getStatus())):
                    
                    assignedHours = doctor.getNextFreeHours()  #if so, assigned hours will be equal to the hours when the doctor is free
                    assignedDoctor = doctor.getName()      #assigned doctor will be equal to the doctor's name
                    doctor.updateDoctorsTime(20)
                    
                    if assignedHours[0]*60 + assignedHours[1] < \
                        self.hoursToInt(nextTime)*60 + self.minutesToInt(nextTime):    #checks if the assigned hours are less than the updated time of the schedule
                        assignedHours = nextTime                            #if so, assigned hours will be equal to the updated schedule's time

                    assignedHours = self.intToTime(*assignedHours)

                    appointment = Schedule(assignedHours, mother.getName(), assignedDoctor)    #declaring new appointment, containing assigned hours, mother's and doctor's names
                    newScheduleList.append(appointment)                                     #appending new schedule list
                    assignedDoctors.append(doctor)                                          #appending siigned doctors list
                    doctor.setStatus(True)      
       

        return newScheduleList #, assignedDoctors

    #TODO

    def writeSchedulesFile(self):
        pass

#if doctor is not already assigned => we can assign him to mother in schedule and update the time. Can check it in the schedule
#if he was assigned before => do not update him(and do not assign to mother). Just add his old assigment to the new schedule

schedules = ScheduleCollection('txt_files/schedule10h00.txt')
#print(schedules.getHeader())
#print(schedules.getSchedulesData())
#print(schedules.getSchedules())

schedules.sortSchedules()
#print(schedules.getSchedules())

#for schedule in schedules.getSchedules():
#    print(type(schedule))


doctors = DoctorCollection('txt_files/doctors10h00.txt')
doctors.sortDoctors()
doctorsList = doctors.getDoctors()

requests = MotherCollection('txt_files/requests10h30.txt')
requests.sortMothers()
requestsList = requests.getMothers()

for app in schedules.updateSchedule(doctorsList, requestsList):
    print(app)

#for app in schedules.updateSchedule(doctorsList, requestsList):
#    for i in app:
#        print(i)
#        print(type(i))
    # print(type(app))

#TODO
      

"""def updateSchedules(self, doctors, requests, nextTime):
    #declaring variables for assigned hours and doctor
    horasAssigned = None
    doctorAssigned = None
    
    #declaring cariable for the new schedule list
    newScheduleList = []

    #part for redirecting to the other network if hours are greater then 20
    for assignedTimeFromOldSchedule in readScheduleFile(self.getSchedules()):                         #reading and searching through the previous schedule
        if hourToInt(updateHours(assignedTimeFromOldSchedule[0], 20)) >= 20:                    #ckecks if updated hours from it are greater than 20
            horasAssigned = intToTime(hourToInt(saveHeader(requests)[HEADER_TIME_IDX][0]), \
                                      minutesToInt(saveHeader(requests)[HEADER_TIME_IDX][0]))   #assigned hours will be equal to the new schedule time in the header
            doctorAssigned = REDIR_STR                                                          #assigned doctor will be equal to "redirected to other network"

    #part for adding mothers from the old schedule if the time of the appointment 
    #is bigger than the time of the new schedule
    for appointment in readScheduleFile(self.getSchedules()):                             #reading and searching through the previous schedule
        if hourToInt(appointment[0]) >= hourToInt(nextTime)\
              and minutesToInt(appointment[0]) >= minutesToInt(nextTime):           #checks if its hours and minutes are greater than the new schedule
            newScheduleList.append(appointment)                                     #if so, this appointment will be added to the new schedule
            
    assignedDoctors = []                                    #declaring variable for assigned doctors list

    mothersList = readRequestsFile(requests)                #declaring variable for old mothers from the previous schedule
    doctorsList = readDoctorsFile(doctors)                  #declaring variable for doctors from the previous doctors
    
    sortedMothers = sorted(mothersList, key=sortRequests)   #declaring variable for sorted mothers
    sortedDoctors = sorted(doctorsList, key=sortDoctors)    #declaring variable for sorted doctors

    for mother in sortedMothers:                            #searching through sorted mothers
        isDoctorAssigned = False                            #declaring variable for the doctor's state

        for doctor in sortedDoctors:                        #searching through sorted doctors
            if ((mother[MOTH_RISK_IDX] == "high" and int(doctor[DOCT_SKILL_IDX]) >= 2 and isDoctorAssigned == False)
                or (mother[MOTH_RISK_IDX] == "low" and int(doctor[DOCT_SKILL_IDX]) >= 1 and isDoctorAssigned == False))\
                         and doctor not in assignedDoctors: #checks if mother's risk is "high" and doctor's skill is greater or equal 2 
                                                            #or mother's risk is "low" and doctor's skill is greater or equal 1
                                                            #and doctor is not yet assigned
                
                horasAssigned = doctor[DOCT_BIRTH_END_IDX]  #if so, assigned hours will be equal to the hours when the doctor is free
                doctorAssigned = doctor[DOCT_NAME_IDX]      #assigned doctor will be equal to the doctor's name
                
                if hourToInt(horasAssigned)*60 + minutesToInt(horasAssigned) < \
                    hourToInt(nextTime)*60 + minutesToInt(nextTime):    #checks if the assigned hours are less than the updated time of the schedule
                    horasAssigned = nextTime                            #if so, assigned hours will be equal to the updated schedule's time

                appointment = [horasAssigned, mother[MOTH_NAME_IDX], doctorAssigned]    #declaring new appointment, containing assigned hours, mother's and doctor's names
                newScheduleList.append(appointment)                                     #appending new schedule list
                assignedDoctors.append(doctor)                                          #appending siigned doctors list
                isDoctorAssigned = True                                                 #making doctor assigned

        if not isDoctorAssigned:                                #checks if doctor is already assigned and there's no free doctors
            horasAssigned = intToTime(hourToInt(saveHeader(requests)[HEADER_TIME_IDX][0]), \
                                      minutesToInt(saveHeader(requests)[HEADER_TIME_IDX][0]))   #assigned hours will be equal to the new schedule time in the header
            doctorAssigned = REDIR_STR                                                          #assigned doctor will be equal to "redirected to other network"
            appointment = [horasAssigned, mother[MOTH_NAME_IDX], doctorAssigned]                #declaring new appointment, containing assigned hours, mother's name and redirected string
            newScheduleList.append(appointment)                                                 #appending new schedule list

    newSortedScheduleList = sorted(newScheduleList, key=sortSchedule)   #declaring new, sorted by time schedule 

    return newSortedScheduleList         """  
from ScheduleTest import *

class ScheduleCollectionTest:
    REDIR_STR = 'redirected to other network'
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
                schedule.setDoctorName('kaka')
                schedule.setSchedule([schedule.getScheduleTime(), schedule.getMotherName(), schedule.getDoctorName()])
                print(schedule.getSchedule())

            
    

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



print(mothers.oldScheduleToNew())
print(mothers.redirecting()) 

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
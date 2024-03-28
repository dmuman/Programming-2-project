from DoctorCollection import DoctorCollection
from MotherCollection import MotherCollection
from ScheduleCollection import ScheduleCollection
from sys import argv

doctorsFileName = 'txt_files/testSet1/schedule10h00.txt'
scheduleFileName = 'txt_files/testSet1/doctors10h00.txt'
requestsFileName = 'txt_files/testSet1/requests10h30.txt'

#TODO

def plan(doctorsFileName, scheduleFileName, requestsFileName):
    try:
        schedules = ScheduleCollection(doctorsFileName)
        schedules.sortSchedules()

        doctors = DoctorCollection(scheduleFileName)
        doctors.sortDoctors()
        doctorsList = doctors.getDoctors()

        requests = MotherCollection(requestsFileName)
        requests.sortMothers()
        requestsList = requests.getMothers()

        for app in schedules.updateSchedule(doctorsList, requestsList):
            for elem in app:
                print(elem)

    except Exception:       #cathing and exception
            print("", end="")

plan(doctorsFileName, scheduleFileName, requestsFileName)
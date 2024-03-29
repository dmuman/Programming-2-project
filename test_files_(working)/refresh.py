from DoctorCollection import DoctorCollection
from MotherCollection import MotherCollection
from ScheduleCollection import ScheduleCollection
from Helper import Helper
from sys import argv

scheduleFileName = argv[1]
doctorsFileName = argv[2]
requestsFileName = argv[3]

#TODO

def plan(scheduleFileName, doctorsFileName, requestsFileName):
    try:
        
        schedules = ScheduleCollection(scheduleFileName)
        schedules.sortSchedules()
        schedules.updateHeadersTime(30)

        doctors = DoctorCollection(doctorsFileName)
        doctors.sortDoctors()
        doctors.updateHeadersTime(30)
        doctorsList = doctors.getDoctors()

        requests = MotherCollection(requestsFileName)
        requests.sortMothers()
        requestsList = requests.getMothers()

        schedulesData, doctorsData = schedules.updateSchedule(doctorsList, requestsList)

        Helper().writeFile(scheduleFileName, schedules.getHeader(), schedulesData)
        Helper().writeFile(doctorsFileName, doctors.getHeader(), doctorsData)

    except Exception:       #cathing an exception
            print("", end="")

plan(scheduleFileName, doctorsFileName, requestsFileName)
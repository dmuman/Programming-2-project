from DoctorTest import *
from DoctorCollectionTest import *

from MotherTest import *
from MotherCollectionTest import *

from ScheduleTest import *
from ScheduleCollectionTest import *

doctors = DoctorCollectionTest('doctors10h00.txt')
doctors.sortDoctors()
mothers = MotherCollectionTest('requests10h30.txt')
schedules = ScheduleCollectionTest('schedule10h00.txt')

newStringHeaderTime = schedules.getHeader()[3]

for doctor in doctors.getDoctors():
    #print(doctor.getStatus())
    for schedule in schedules.getSchedules():
        if (doctor.getName() in schedule.getSchedule()) and (schedule.getScheduleTime()[0]*60 + schedule.getScheduleTime()[1] > doctor.timeToInt(newStringHeaderTime)[0]*60 + doctor.timeToInt(newStringHeaderTime)[1]+30):
            doctor.setStatus(True)

    print(doctor.getName())
    print(doctor.getStatus())
    print(doctors.getDoctors())
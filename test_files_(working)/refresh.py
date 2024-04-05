# 2023-2024 Programação 2
# Grupo 25
# 59348 Dmytro Umanskyi
# 62235 Duarte Alberto

from DoctorCollection import DoctorCollection       # importing DoctorCollection
from MotherCollection import MotherCollection       # importing MotherCollection
from ScheduleCollection import ScheduleCollection   # importing ScheduleCollection
from Helper import Helper                           # importing HelperCollection
from sys import argv                                # importing argv from sys

# assigning variables ti corresponding argv indexes 
scheduleFileName = argv[1]
doctorsFileName = argv[2]
requestsFileName = argv[3]

############################################################################
############################## MAIN FUNCTION ###############################
############################################################################

def plan(scheduleFileName, doctorsFileName, requestsFileName):
    """
    Main function, that runs the whole program.
    Receives three input files (scheduleXXhYY.txt, 
    doctorsXXhYY.txt and requestsXXhYY.txt) 
    with all the necessary inforamtion, which then uses 
    to make two output files with updated information. 
    scheduleXXhYY.txt and doctorsXXhYY.txt in particular.

    Requires:
    {name}FileName are all strings, received from the 
    command line. All represents text file with the
    .txt format. 
    Files stays in the same directory, as the program.
    Files are not empty.

    Ensures:
    Two text files, created inside the same directory,
    as the program. Both in .txt format.
    doctorsXXhYY.txt and scheduleXXhYY.txt
    Files contain updated information about Schedule and Doctors.
    """
    # using try except to catch any errors
    try:
        # declaring ScheduleCollection
        schedules = ScheduleCollection(scheduleFileName)
        # sorting it
        schedules.sortSchedules()
        # updating time in the header
        schedules.updateHeadersTime(30)

        # declaring DoctorCollection
        doctors = DoctorCollection(doctorsFileName)
        # sorting it
        doctors.sortDoctors()
        # updating time in the header
        doctors.updateHeadersTime(30)
        # making a list out of doctors to then be able to use it
        doctorsList = doctors.getDoctors()

        # declaring MotherCollection
        requests = MotherCollection(requestsFileName)
        # sorting it
        requests.sortMothers()
        # making a list out of mothers to then be able to use it
        requestsList = requests.getMothers()

        # assigning updated data from the updateShedule function
        # to new variables
        schedulesData, doctorsData = schedules.updateSchedule(doctorsList, requestsList)

        # writing both files using Helper's writeFile function
        # parameter are:
        # old files' names
        # updated header (which is a list)
        # updated data (which is also a list)
        Helper().writeFile(scheduleFileName, schedules.getHeader(), schedulesData)
        Helper().writeFile(doctorsFileName, doctors.getHeader(), doctorsData)

    # cathing an exception
    except Exception:
            # and ignoring it, if it's not the IOError from reading the files
            print("", end="")

# executing the function
plan(scheduleFileName, doctorsFileName, requestsFileName)
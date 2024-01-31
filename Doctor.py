from Helpers import *
from DoctorCollection import *

class Doctor(DoctorCollection):
    DOCT_NAME_IDX = 0
    DOCT_SKILL_IDX = 1
    DOCT_FREEHOURS_IDX = 2
    DOCT_DAILYMIN_IDX = 3
    DOCT_WEEKHOURS_IDX = 4
    def __init__(self, filename):
        super().__init__(filename)
        for doctor in super().getDoctors():
            self._name = doctor[Doctor.DOCT_NAME_IDX]
            self._skill = int(doctor[Doctor.DOCT_SKILL_IDX])
            self._nextFreeHours = doctor[Doctor.DOCT_FREEHOURS_IDX]
            self._dailyMinutes = int(doctor[Doctor.DOCT_DAILYMIN_IDX])
            self._weeklyHours = doctor[Doctor.DOCT_WEEKHOURS_IDX]
            self._doctor = [self._name, self._skill, self._nextFreeHours, self._dailyMinutes, self._weeklyHours]
    # bello
    #setters
    def setDoctor(self, doctor):
        self._doctor = doctor     

    def setName(self, name):
        self._name = name
    
    def setSkill(self, skill):
        self._skill = skill

    def setNextFreeHours(self, nextFreeHours):
        self._nextFreeHours = nextFreeHours
    
    def setDailyMinutes(self, dailyMinutes):
        self._dailyMinutes = dailyMinutes
    
    def setWeeklyHours(self, weeklyHours):
        self._weeklyHours = weeklyHours

    #getters
    def getDoctor(self):
        return self._doctor  

    def getName(self):
        return self._name
    
    def getSkill(self):
        return self._skill

    def getNextFreeHours(self):
        return self._nextFreeHours
    
    def getDailyMinutes(self):
        return self._dailyMinutes
    
    def getWeeklyHours(self):
        return self._weeklyHours
    
    def sortDoctors(self):
        """
        Sorts doctors in decrescent order of their skills.
        If they're the same - in decrescent order of time that's left until 1 hour pause.
        If they're the same - in decrescent order of time that's left until weekly leave.
        If they're the same - in the alphabetical order of the names.

        Requires: doctorsList is a list of list, each list represents a doctor.

        Ensures: tuple, containing the skill, time left unti 1 hour pause, 
        time left unti weekly leave and name of the corresponding doctor.
        """
        if self.getDailyMinutes() > 240:                                    #checks if the daily worked minutes are greater than 240
            timeToPause = 240*2 - self.getDailyMinutes()                    #if so, timeToPause will be 240*2(i.e. limit times 2) - daily worked minutes
        else:                                                               #if it's not greater than 240(i.e. less than 240)
            timeToPause = 240 - self.getDailyMinutes()                      #timeToPause will be 240(i.e. limit) - daily worked minutes

        totalMinutesWeeklyWorked = (Helpers.hourToInt(self.getNextFreeHours()) * 60 \
                        + Helpers.minutesToInt(self.getNextFreeHours()))    #gaining totalMinutes for weekly work
        
        timeToWeeklyPause = 40 * 60 - totalMinutesWeeklyWorked              #calculating the time left until weekly pause

        return (-(self.getSkill()), -timeToPause, \
                -timeToWeeklyPause, self.getName())                         #returning skill, time left to one hour pause, time left to weekly pause and the name

    #string
    def __str__(self):
        return f'{self.getDoctor()}'

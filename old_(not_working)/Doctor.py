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
    
    #string
    def __str__(self):
        return f'{self.getDoctor()}'

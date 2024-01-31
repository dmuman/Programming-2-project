class Schedule:
    def __init__(self, scheduledHours, assignedMother, assignedDoctor):
        self._scheduledHours = scheduledHours
        self._assignedMother = assignedMother
        self._assignedDoctor = assignedDoctor

    #setters
    def setScheduledHours(self, scheduledHours):
        self._scheduledHours = scheduledHours
    
    def setAssignedMother(self, assignedMother):
        self._assignedMother = assignedMother

    def setAssignedDoctor(self, assignedDoctor):
        self._assignedDoctor = assignedDoctor

    #getters
    def getScheduledHours(self):
        return self._scheduledHours
    
    def getAssignedMother(self):
        return self._assignedMother

    def getAssignedDoctor(self):
        return self._assignedDoctor

    #string
    def __str__(self):
        return f'Scheduled Hours: {self.getScheduledHours()}\n\
                Assigned Mother`s name: {self.getAssignedMother()}\n\
                Assigned Doctor`s name: {self.getAssignedDoctor()}'
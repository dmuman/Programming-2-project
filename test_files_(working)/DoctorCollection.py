from Doctor import Doctor   # importing Doctor
from Helper import Helper   # importing Helper

class DoctorCollection:
    """
    Doctor collection class representing a collection of doctors.
    """
    # declaring class variables (constants)
    HOURS_IDX = 0       # hours index
    MINUTES_IDX = 1     # minutes index
    TIME_HEAD_IDX = 3   # time in header index
    
    ############################################################################
    ############################## INITIALIZATION ##############################
    ############################################################################

    def __init__(self, filename):
        """
        Initializes a DoctorCollection object.
        Makes a collection of Doctor objects.
        Uses readFile method from the Helper class.

        Requires:
        filename is a string representing the name of the file 
        containing doctor data.
        File is in the same directory as the program in the .txt format.

        Ensures:
        Using readFile function from the Helper class,
        a DoctorCollection object is initialized with the specified filename,
        header, time in header, and doctors data, which is a list, 
        containing Doctor objects.
        """
        self._filename = filename
        self._header, self._doctorsData = Helper().readFile(self.getFilename())
        self._headerTime = self._header[self.TIME_HEAD_IDX]
        self._doctors = []
        for data in self.getDoctorsData():
            name, skill, nextFreeHours, dailyMinutes, weeklyHours = data
            doctor = Doctor(name, skill, nextFreeHours, dailyMinutes, weeklyHours)
            self._doctors.append(doctor)

    ############################################################################
    ################################# SETTERS ##################################
    ############################################################################

    def setHeader(self, header):
        """
        Sets the header of the doctor collection.

        Requires:
        header is a list, representing the new header
        information to be set.

        Ensures:
        The header of the doctor collection is updated.
        """
        self._header = header

    def setHeaderTime(self, headerTime):
        """
        Updates header's time with the provided time.

        Requires:
        headerTime is a string representing the new 
        header's time to be set.

        Ensures:
        headerTime is updated by the provided time.
        """
        self.getHeader()[self.TIME_HEAD_IDX] = headerTime

    def setDoctorsData(self, doctorsData):
        """
        Sets the doctors' data of the doctor collection.

        Requires:
        doctorsData is a list, representing the new
        doctors' data to be set.

        Ensures:
        The doctors' data of the doctor collection is updated.
        """
        self._doctorsData = doctorsData

    def setDoctors(self, doctors):
        """
        Sets the list of doctors in the doctor collection.

        Requires:
        doctors is a list, representing the list of 
        Doctor objects to be set.

        Ensures:
        The list of doctors in the doctor collection is updated.
        """
        self._doctors = doctors

    ############################################################################
    ################################# GETTERS ##################################
    ############################################################################

    def getFilename(self):
        """
        Gets the filename of the doctor collection.

        Ensures:
        The filename of the doctor collection.
        """
        return self._filename
    
    def getHeader(self):
        """
        Gets the header of the doctor collection.

        Ensures:
        The header of the doctor collection.
        """
        return self._header
    
    def getHeaderTime(self):
        """
        Using a function from the Helper class, gets the time
        from the header.

        Ensures:
        List, containing the time from the header in the
        format of [HH, MM] 
        """
        return Helper().timeToInt(self._headerTime)

    def getDoctorsData(self):
        """
        Gets the doctors' data of the doctor collection.

        Ensures:
        The list of doctors' data of the doctor collection.
        """
        return self._doctorsData
    
    def getDoctors(self):
        """
        Gets the list of doctors in the doctor collection.

        Ensures:
        The list of doctors in the doctor collection.
        """
        return self._doctors

    ############################################################################
    ########################### HEADER TIME UPDATE #############################
    ############################################################################

    def updateHeadersTime(self, minutesToAdd):
        """
        Updates headers time by the given amount of minutes,
        using a function from the Helper class.

        Requires:
        minutesToAdd is an int.

        Ensures:
        Header's time is updated with the given amount of minutes.
        """
        self.setHeaderTime(Helper().updateHours(self._headerTime, minutesToAdd))

    ############################################################################
    ################################# SORTING ##################################
    ############################################################################

    def sortDoctors(self):
        """
        Sorts the list of doctors in the doctor collection based on predefined 
        in the Doctor class keys.

        Ensures:
        The list of doctors is sorted according to predefined sorting keys.
        """
        self.getDoctors().sort(key = Doctor.sortDoctorsKeys)
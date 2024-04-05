from Mother import Mother   # importing Mother
from Helper import Helper   # importing Helper

class MotherCollection:
    """
    Mother collection class representing a collection of mothers.
    """

    ############################################################################
    ############################## INITIALIZATION ##############################
    ############################################################################

    def __init__(self, filename):
        """
        Initializes a MotherCollection object.
        Makes a collection of Mother objects.
        Uses readFile method from the Helper class.

        Requires:
        filename is a string representing the name of the file 
        containing mother data.
        File is in the same directory as the program in the .txt format.

        Ensures:
        Using readFile function from the Helper class,
        a MotherCollection object is initialized with the specified filename,
        header, and mothers data, which is a list, containing Mother objects.
        """
        self._filename = filename
        self._header, self._mothersData = Helper().readFile(self.getFilename())
        self._mothers = []
        for data in self.getMothersData():
            name, age, tagColour, riskLevel = data
            mother = Mother(name, age, tagColour, riskLevel)
            self._mothers.append(mother)

    ############################################################################
    ################################# SETTERS ##################################
    ############################################################################

    def setHeader(self, header):
        """
        Sets the header of the mother collection.

        Requires:
        header is a list, representing the new header
        information to be set.

        Ensures:
        The header of the mother collection is updated.
        """
        self._header = header

    def setMothersData(self, mothersData):
        """
        Sets the mothers' data of the mother collection.

        Requires:
        mothersData is a list, representing the new
        mothers' data to be set.

        Ensures:
        The mothers' data of the mother collection is updated.
        """
        self._mothersData = mothersData

    def setMothers(self, mothers):
        """
        Sets the list of mothers in the mother collection.

        Requires:
        mothers is a list, representing the list of 
        Mother objects to be set.

        Ensures:
        The list of mothers in the mother collection is updated.
        """
        self._mothers = mothers

    ############################################################################
    ################################# GETTERS ##################################
    ############################################################################

    def getFilename(self):
        """
        Gets the filename of the mother collection.

        Ensures:
        The filename of the mother collection.
        """
        return self._filename
    
    def getHeader(self):
        """
        Gets the header of the mother collection.

        Ensures:
        The header of the mother collection.
        """
        return self._header

    def getMothersData(self):
        """
        Gets the mothers' data of the mother collection.

        Ensures:
        The list of mothers' data of the mother collection.
        """
        return self._mothersData
    
    def getMothers(self):
        """
        Gets the list of mothers in the mother collection.

        Ensures:
        The list of mothers in the mother collection.
        """
        return self._mothers

    ############################################################################
    ################################# SORTING ##################################
    ############################################################################

    def sortMothers(self):
        """
        Sorts the list of mothers in the mother collection based on predefined 
        in the Mother class keys.

        Ensures:
        The list of mothers is sorted according to predefined sorting keys.
        """
        self.getMothers().sort(key = Mother.sortMothersKeys)
# 2023-2024 Programação 2
# Grupo 25
# 59348 Dmytro Umanskyi
# 62235 Duarte Alberto

class Mother:
    """
    Mother class representing a mother with attributes 
    such as name, age, tag colour, and risk level.
    """

    ############################################################################
    ############################## INITIALIZATION ##############################
    ############################################################################

    def __init__(self, name, age, tagColour, riskLevel):
        """
        Initializes a Mother object.

        Requires:
        name is a string that represents the name of the mother.
        age is a string that represents the age of the mother.
        tagColour is a string that represents the tag colour of the mother.
        riskLevel is a string that represents the risk level of the mother.

        Ensures:
        A Mother object is initialized with the specified attributes.
        """
        self._name = name
        self._age = age
        self._tagColour = tagColour
        self._riskLevel = riskLevel
        self._mother = [self.getName(), self.getAge(), self.getTagColour(), 
                        self.getRiskLevel()]

    ############################################################################
    ################################# SETTERS ##################################
    ############################################################################

    def setName(self, name):
        """
        Sets the name of the mother.

        Requires:
        name is a string that represents the new name of the mother.

        Ensures:
        The name of the mother is updated.
        """
        self._name = name
    
    def setAge(self, age):
        """
        Sets the age of the mother.

        Requires:
        age is a string that represents the new age of the mother.

        Ensures:
        The age of the mother is updated.
        """
        self._age = age

    def setTagColour(self, tagColour):
        """
        Sets the tag colour of the mother.

        Requires:
        tagColour is a string that represents the new tag colour of the mother.

        Ensures:
        The tag colour of the mother is updated.
        """
        self._tagColour = tagColour
    
    def setRiskLevel(self, riskLevel):
        """
        Sets the risk level of the mother.

        Requires:
        riskLevel is a string that represents the new risk level of the mother.

        Ensures:
        The risk level of the mother is updated.
        """
        self._riskLevel = riskLevel

    def setMother(self, mother):
        """
        Sets the attributes of the mother.

        Requires:
        mother is a list containing the attributes of the mother.

        Ensures:
        The attributes of the mother are updated.
        """
        self._mother = mother

    ############################################################################
    ################################# GETTERS ##################################
    ############################################################################

    def getName(self):
        """
        Gets the name of the mother.

        Ensures:
        The string name of the mother.
        """
        return self._name
    
    def getAge(self):
        """
        Gets the age of the mother.

        Ensures:
        The int age of the mother.
        """
        return int(self._age)

    def getTagColour(self):
        """
        Gets the tag colour of the mother.

        Ensures:
        The string tag colour of the mother.
        """
        return self._tagColour
    
    def getRiskLevel(self):
        """
        Gets the risk level of the mother.

        Ensures:
        The string risk level of the mother.
        """
        return self._riskLevel
    
    def getMother(self):
        """
        Gets the attributes of the mother.

        Ensures:
        List containing the attributes of the mother.
        """
        return self._mother

    ############################################################################
    ################################ SORT KEYS #################################
    ############################################################################
    
    def sortMothersKeys(self):
        """
        Generates sorting keys for mothers based on 
        risk level, tag colour, age, and name,
        by assigning int representations to the risk levels and tag colours

        Ensures:
        Tuple containing sorting keys for the mother.
        Where: 
        Risks are in decrescending order, tags are in crescending, 
        ages are in decrescending and names are in alphabetical oreder
        """
        # assigning int representation of the risk levels
        risks = {"high": 1, "low": 2}

        # assigning int representation of the tag colours           
        tags = {"red": 3, "yellow": 2, "green": 1}

        return (-risks[self.getRiskLevel()], tags[self.getTagColour()], 
                -self.getAge(), self.getName())
    
    ############################################################################
    ################################## STRING ##################################
    ############################################################################
    
    def __str__(self):
        """
        String representation of the mother object.

        Ensures:
        String representation of the mother.
        """
        return str(self.getMother())
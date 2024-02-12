class DoctorCollectionTest:
    def __init__(self, filename):
        self._filename = filename
        self._header, self._doctors = self.readFile()

    def getFilename(self):
        return self._filename

    def readFile(self):
        with open(self.getFilename(), 'r', encoding='utf-8') as inFile:
            lines = inFile.readlines()

            headerTemp = lines[:7]
            header = []

            for line in headerTemp:
                headerTemp = line.rstrip('\n')
                header.append(headerTemp)

            doctors = [line.strip().split(", ") for line in lines[7:] if line.strip()]

        return header, doctors
    
    def getHeader(self):
        return self._header

    def getDoctors(self):
        return self._doctors
    

doctors = DoctorCollectionTest('doctors10h00.txt')
print(doctors.getHeader())
print(doctors.getDoctors())
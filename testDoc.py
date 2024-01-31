from DoctorCollection import *
from Doctor import *

#doctors = DoctorCollection('doctors10h00.txt')

#print(doctors.getHeader())

#print(doctors.getDoctors())

#print(type(doctors))

#doctorsCol = []
#
#for doctor in doctors.getDoctors():
#    print(doctor)
#    #print(type(doctor))
#    #for docInfo in doctor:
#    doctorsCol.append(Doctor(doctor).getDoctor())
#    
#print(doctorsCol)
    

#doctor = Doctor(doctors.getDoctors()[0])

#print(doctor)

doctor = Doctor('doctors10h00.txt')

print(doctor)

print(doctor.getDoctor())
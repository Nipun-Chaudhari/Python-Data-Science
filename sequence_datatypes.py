# SEQUENCE DATATYPES

string = "My name is Nipun"

from array import *
arraySample = array('i',[1,2,3,4])

# Printing an array
for x in arraySample:
    print(x)
    
# Tuple and Tuple packing
tupleSam = ("Nipun",3,4,5)
tuplePack = 'asdw',5,6,7

# Dictionary
dictSample = {'car':'nexon','bike':'unicorn','scooter':'activa'}
print(dictSample)

# Sets in Python
#   list and another set cannot be the part of a set
setSample = {'sample',3,4,5,int()}

set2 = set('Nipun')
print(set2)

# Range
rangeSample = range(1,12,3)
print(rangeSample)
for x in rangeSample:
    print(x)
import numpy as np
# print(np.__version__)
a=[1,2,3,4]
# Nupmy array
a_ar = np.array(a)
b_ar = np.array([10,20,30,40])
print(a_ar,a)

#Accessing first item from numpy array
print(a_ar[0])

#Slicing 
print(a_ar[0:3])

#filtering based on boolean condtion
print(b_ar[(b_ar<40) & (b_ar>10)])

#Basic operation..
print(a_ar+b_ar)
print(a_ar-b_ar)
print(a_ar*b_ar)
print(b_ar/a_ar)

# Maths methods..
print(np.max(a_ar))
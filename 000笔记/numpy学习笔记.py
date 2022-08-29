import numpy as np
print(np.__version__)

# The NumPy library is the core library for scientific computing in Python.
# It provides a high-performance multidimensional array object, and tools for# working with these arrays

# ----------------------
# creating arrays
# ----------------------
a = np.array([1,2,3])
b = np.array([(1.5,2,3),(4,5,6)],dtype=float)
c = np.array([[(1.5,2,3),(4,5,6)],[(3,2,1),(4,5,6)]],dtype=float)
# initial placeholders
d = np.zeros((3,4))#Create an array of zeros
e = np.ones((2,3,4),dtype=np.int16)#Create an array of ones
f = np.arange(10,25,5)#Create an array of evenly spaced values (step value)
g = np.linspace(0,2,9)#Create an array of evenly spaced values (number of samples)
h = np.full((2,2),7)#Create a constant array
i = np.eye(2)#Create a 2X2 identity matrix
j = np.empty((3,2))#Create an empty array = np.random.random((2,2))#Create an array with random values












# ********** Lec 1 [ Introduction to Numpy ]


#************************************************** 
#! PYTHON_LIST VS NUMPYARRAY
#************************************************** 
#************************************************** 


# PythonList and NumpyArray both are different

#? PYTHON LIST
a = [42]
b = [1, 2, 3, 4, 5]
c = [[1, 2, 3], [4, 5, 6]]

d = [[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]]      
#* Even though we tried making it a 3d list but python is considering it as 1d entity with some nesting


print(a, '\n')
print(b, '\n')
print(c, '\n')
print(d, '\n')


#**********************************************
#**********************************************


#? NUMPY_ARRAY
import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a, a.ndim, '\n')
print(b, b.ndim, '\n')
print(c, c.ndim, '\n')
print(d, d.ndim, '\n')

import numpy as np


# array_1d = np.array([[1,2,3],[4,5,6],[7,8,9]])
# array_2d = np.array([[11,12,13],[14,15,16],[17,18,19]])
# concat = np.concatenate(array_1d + array_2d)

# print(concat)


#print(np.concat((array_1d , array_2d),0))
# concat=np.concatenate((array_1d,array_2d),axis=1)
# concat1=np.concatenate((array_1d,array_2d),axis=0)
# print(concat)
# print(concat1)

# ************************************  Ravel or Flatten ***************************************************
# It convert Multidimestional array into the single Array..

# array1 = np.array([[1,2,3], [4,5,6], [7,8,9]])

# print(array1.shape)
# print(array1.size)
# # print(array1.max)
# # print(array1.min)
# # print(array1.sum)

# ravel_array = array1.ravel()
# ravel_array[0] = 100

# print(ravel_array)
# print(array1)
# print(ravel_array.ndim)


# array1 = np.array([[1,2,3], [4,5,6], [7,8,9]])

# print(array1.shape)
# print(array1.size)
# # print(array1.max)
# # print(array1.min)
# # print(array1.sum)

# flatten_array = array1.flatten()
# flatten_array[0] = 100
# print(flatten_array)
# print(array1)
# print(flatten_array.ndim)      # tell the 1 means that 1D array return by flatten Array


# **************************************************************************************************************************************************************

array1 = np.array([1,1,2,2,3,3,4,4,5,5,6,6,7])

# array2 = np.unique(array1)
# array2 = np.unique_all(array1)
# array2 = np.unique(array1, return_index=True)
# array2 = np.unique(array1, return_counts=True)    # return the count of each and every element.
# array2 = np.unique(array1, return_inverse=True)

# array2 = np.unique(array1)

# print(array2)

# array2 = np.array([[[1,2,3], [4,5,6], [7,8,9]], [[1,2,3], [4,5,6], [7,8,9]]])

# returnArr = np.unique(array2)
# # returnArr = np.unique_all(array2)
# print(returnArr)

# array1 = np.array([[1,2,3], [4,5,6], [7,8,9]])

# array2 = np.zeros((1,3))
# array3 = np.ones((1,3))

# print(array2)
# print(array1)
# print(array3)
# array1[0:2] = 0

# array2 = np.linspace(0,10,5)
# array2 = np.arange(36).reshape(3,3,4)
# array2 = np.arange(36).reshape(4,9)
# array2 = np.arange(36).reshape(9,4)

# array2 = np.tile(1,4)
# array2 = np.where(False,10,[1,100])

# print(array2)


# array2 = np.append()
# array2 = array1.tolist()
# array2 = np.ravel(array1).size
# array2 = np.ravel(array1).shape(3,3)
# print(array2)

# arr1 = [1,2,3,4]
# arr2 = [5,6,7,8]

# array2 = np.subtract(arr1,arr2)
# print(array2)

# arr1 = [1,2,3,4]
# arr2 = [5,6,7,8]

# array2 = np.multiply(arr1,arr2)
# print(array2)

# arr1 = [1,2,3,4]
# arr2 = [5,6,7,8]

# array2 = np.divide(arr1,arr2)
# print(array2)

# arr1 = [1,2,3,4]
# arr2 = [5,6,7,8]

# array2 = np.add(arr1,arr2)
# print(array2)

array1 = np.array([[1,2,3], [4,5,6], [7,8,9]])

# array1[0:1,0:1] = 0
# array1[0:3,0:3] = 0
# array1[0:3,0:2] = 0
# array1[0:3,0:2] = 0

print(array1)

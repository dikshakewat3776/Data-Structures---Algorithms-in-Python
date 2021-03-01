from array import array
import numpy as np


# Creating an Array
arr1 = array('i', [1, 2, 3, 4, 5, 6])
arr2 = array('d', [1.1, 2.2, 3.3, 4.4, 5.5, 6.6])

print(arr1)
print(arr2)

# Array Insertion
arr1.insert(6, 7)
arr1.insert(0, 0)
arr1.insert(2, 9)

print(arr1)
print(type(arr1))


# Array Traversal
def traverseArray(arr):
    print("Traversing Array")
    for i in arr:
        print(i)
traverseArray(arr1)


# Array access
def accessElement(arr, index):
    print("Accessing Array Element")
    if index > len(arr):
        print("No element at this index")
    else:
        print("Element accessed at:" + str(arr[index]))
accessElement(arr1, 4)


# Array Search
def searchElement(arr, value):
    print("Searching Array Element")
    for i in arr:
        if i == value:
            print("Element found.")
            return True
    print("Element not found.")
    return False


searchElement(arr1, 9)
searchElement(arr1, 99)

# Array Deletion
arr1.remove(1)
print(arr1)

arr1.remove(7)
print(arr1)


# Array Insertion
arr1.append(7)  # inserts only at the end of an array
arr1.insert(1, 1)
arr1.insert(3, 5)
print(arr1)


# Extend Python Array
arr3 = array('i', [7, 8])
arr1.extend(arr3)
print(arr1)


# Add items from list to array
tempList = [11, 12, 13, 14, 15]
arr1.fromlist(tempList)
print(arr1)
print(type(arr1))


# Remove array elements
arr1.remove(15)
print(arr1)
arr1.pop()  # removes only last element
print(arr1)


# Reverse python array
arr1.reverse()
print(arr1)


# Count array element occurences
c = arr1.count(7)
print(c)


# array to string
s = arr1.tostring()
print(s)

# Array Slicing
s1 = arr1[1:4]
print(s1)
s2 = arr1[::2]
print(s2)


# array to list
l = arr1.tolist()
print(l)
print(type(l))


# creating 2D array
tdArray = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11,  12]])
print(tdArray)


# 2D array insertion
colstdarray = np.insert(tdArray, 0, [[1, 2, 3]], axis=1)
print(colstdarray)

rowstdarray = np.insert(tdArray, 1, [[1, 2, 3]], axis=1)
print(rowstdarray)


# 2D array access
def accessElements(arr, rowIndex, colIndex):
    if rowIndex >= len(arr) and colIndex >= len(arr[0]):
        print("No element at this index")
    else:
        print(arr[rowIndex][colIndex])


accessElements(tdArray, 1, 2)


# 2D array traversal
def traverse2Darray(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j])


traverse2Darray(tdArray)


# 2D array search
def search2Darray(arr, value):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == value:
                print("The value is located at index: " + str(i) + "," + str(j))
                return True
    print("Element not found.")
    return False


search2Darray(tdArray, 7)


# 2D array deletion
row_deltdArray = np.delete(tdArray, 0, axis=0)  # deleting first row
print(row_deltdArray)

col_deltdArray = np.delete(tdArray, 1, axis=1)  # deleting first column
print(col_deltdArray)

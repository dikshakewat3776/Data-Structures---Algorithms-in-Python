from array import array

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
import numpy as np
tdArray = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11,  12]])
print(tdArray)


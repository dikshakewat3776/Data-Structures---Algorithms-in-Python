# Dictionary Creation
myDict = dict()
print(myDict)
print(type(myDict))

myDict = {"1": "One", "2": "Two", "3": "Three", "4": "Four", "5": "Five"}

# Dictionary Access
print(myDict["1"])

# Dictionary Insertion
myDict["10"] = "Ten"
print(myDict)


# Dictionary Traversal
def traverseDict(sampleDict):
    for key in sampleDict:
        print(key, sampleDict[key])

traverseDict(myDict)


# Dictionary Search
def searchDict(sampleDict, value):
    for key in sampleDict:
        if sampleDict[key] == value:
            print("Value Found: " + str(key) + "," + str(value))
            return
    print("Value doesn't exist")
    return


searchDict(myDict, 'Four')
searchDict(myDict, '4')


# Dictionary Deletion
myDict.pop('10')
myDict.popitem()
del myDict['3']
print(myDict)

myDict.clear()
print(myDict)
del myDict
# print(myDict)   Exception thrown


# Dictionary Methods
myDict1 = {"1": "One", "2": "Two", "3": "Three", "4": "Four", "5": "Five"}

myDict2 = myDict1.copy()
print(myDict2)


myDict3 = {}.fromkeys([1, 2, 3], 0)
print(myDict3)

print(myDict1.get('1'))

print(myDict1.items())

print(myDict1.values())

print(myDict1.keys())

myDict1.setdefault('default', 'Ten')
print(myDict1)

myDict1.update(myDict3)
print(myDict1)


# Dictionary Functions
print(all(myDict1))

print(any(myDict1))

print(sorted(myDict1))

print(sorted(myDict1, reverse=True))

print(sorted(myDict1, key=True))








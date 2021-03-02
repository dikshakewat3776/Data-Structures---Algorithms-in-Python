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
del myDict


# Dictionary Methods
myDict1 = {"1": "One", "2": "Two", "3": "Three", "4": "Four", "5": "Five"}

myDict2 = myDict1.copy()
print(myDict2)
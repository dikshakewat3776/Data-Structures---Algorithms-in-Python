# List creation
my_list = [1, 2, 3, 4, 5, 6, 7]


# list traversal
def traverseList(sampleList):
    print("Traversing List")
    for i in sampleList:
        print(i)


traverseList(my_list)


# list insertion
my_list.insert(0, 11)
my_list.insert(1, 12)
my_list.insert(2, 13)
my_list.append(22)
my_list.extend([10, 20, 30, 40])
print(my_list)


# list deletion
my_list.pop(9)
del my_list[3]
my_list.remove(22)
print(my_list)


# list search
def searchInList(list, value):
    for i in list:
        if i == value:
            print("Value found at index: " + str(list.index(value)))
            return
        else:
            pass
    print("Value doesn't exist.")
    return


searchInList(my_list, 10)
searchInList(my_list, 99)


# list operations
my_list1 = [1, 2, 3]
my_list2 = [4, 5, 6]

# concatenation
my_list3 = my_list1 + my_list2
print(my_list3)

# repetition
my_list4 = my_list3 * 2
print(my_list4)

# length
print(len(my_list4))

# maximum
print(max(my_list4))

# minimum
print(max(my_list4))

# average
print(sum(my_list4)/len(my_list4))

# list and strings
my_string = "Hello"

# string to list
my_list5 = list(my_string)
print(my_list5)

my_string1 = "Hello Hello Hello"
my_list5 = my_string1.split()
print(my_list5)
print(type(my_list5))

my_string1 = "Hello1-Hello2-Hello3"
my_list5 = my_string1.split('-')
print(my_list5)
print(type(my_list5))

# find pairs of integers from a list whose sum is  equal to a given number
# Ex.
# Input: [2,3,6,9,11] is the list and given number is 9
# Output: [6,3]


def findPairs(someList, sum):
    for i in range(len(someList)):
        for j in range(i+1, len(someList)):
            if (someList[i] + someList[j]) == sum:
                print("Pairs found: " + str(someList[i]) + "," + str(someList[j]))
                return
            else:
                pass
    print("Pairs not found.")
    return


findPairs(my_list4, 10)
findPairs(my_list4, 100)


# find maximum product pairs in a list whose product is the highest
# Ex.
# Input: [2,3,6,9,11] is the list
# Output: [9,11] is the max product pair since the highest product is 99.


def findMaxProduct(someList):
    maxProduct = 0
    for i in range(len(someList)):
        for j in range(i+1, len(someList)):
            if someList[i] * someList[j] > maxProduct:
                maxProduct = someList[i] * someList[j]
                pairs = str(someList[i]) + "," + str(someList[j])
    print("Pairs Found:" + str(pairs))
    print("Max product:" + str(maxProduct))
    return


findMaxProduct([2, 3, 6, 9, 11])


# find unique elements in a list
# Ex.
# Input: [1, 2, 3, 7, 7, 9] is the input list
# Output: [1, 2, 3, 7, 9] is the unique list


def isUniqueList(someList):
    a = []
    for i in someList:
        if i in a:
            print("Element already exists:" + str(i))
        else:
            print("Unique Element:" + str(i))
            a.append(i)
    print("Unique list is:" + str(a))
    return


isUniqueList([1, 2, 3, 7, 7, 9])


# find permutations in a list
# Ex.
# peek - keep, rail - liar are permutations of eaach other


def permutationList(l1, l2):
    l2.reverse()
    if l1 == l2:
        print("Permutation List")
        return True
    else:
        print("Not a permutation List")
        return False


permutationList(l1=[1, 2, 3, 4], l2=[4, 3, 2, 1])
permutationList(l1=[1, 2, 3, 4], l2=[4, 3, 3, 1])




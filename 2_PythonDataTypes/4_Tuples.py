# Tuple creation
my_tuple = ('a', 'b', 'c', 'd', 'e')
print(my_tuple)
print(type(my_tuple))


# Tuple Access
print(my_tuple[1])
print(my_tuple[-1])


# Tuples traversal
for i in my_tuple:
    print(i)


# Tuples search
def searchTuple(someTuple, value):
    for i in someTuple:
        if i == value:
            print("Element Found at: " + str(someTuple.index(i)))
            return
    print("Element not found")
    return


searchTuple(my_tuple, 'a')
searchTuple(my_tuple, 'z')


# Tuple Operations

my_tuple1 = tuple('ewhdg')
my_tuple2 = tuple('oqwert')
print(my_tuple1)
print(my_tuple2)

# Concatenation
print(my_tuple1+my_tuple2)

# Repetition
print(my_tuple1*3)

# Count elements
print(my_tuple1.count('g'))

print(len(my_tuple1))
print(max(my_tuple1))
print(min(my_tuple1))

# List to tuple
print(tuple([1, 2, 3]))

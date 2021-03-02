"""
ALGORITHM: CREATION OF SINGLY LINKED LISTS
1. Create head and tail, initialize with null
2. Create a blank node and assign a value to it and reference to null
3. Link head and tail with node
"""


class Node:
    # Node class creates nodes with values and reference to the next node
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    # Empty SLL with head and tail as None
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        # iterate through the nodes
        node = self.head
        while node:
            yield node
            node = node.next


SLL = SinglyLinkedList()

# Node creation with value and reference
node = Node(1)
node.next = None

# Link head and tail to the node
SLL.head = node
SLL.tail = node

print([node.value for node in SLL])

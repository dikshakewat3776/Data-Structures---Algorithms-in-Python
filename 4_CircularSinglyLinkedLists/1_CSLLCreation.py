"""
ALGORITHM: CREATION OF CIRCULAR SINGLY LINKED LISTS
1. Create a node and assign a value to it. NODE.VALUE = VALUE
2. Set the reference of node to itself. NODE.NEXT = NODE
3. Set head and tail to node. HEAD = NODE, TAIL = NODE
4. Terminate
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class CircularSinglyLinkedLists:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node == self.tail.next:
                break
            node = node.next

    def create_csll(self, nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node
        print("CSLL has been created.")


CSLL = CircularSinglyLinkedLists()
CSLL.create_csll(nodeValue=1)
print([node.value for node in CSLL])


"""
OUTPUT:
CSLL has been created.
[1]
"""



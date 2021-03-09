"""
ALGORITHM: CREATION OF DOUBLY LINKED LISTS
1. Create head and tail, initialize with null
2. Create a blank node and assign a value to it.
3. Set reference to next node as NULL.
4. Set reference to previous node as NULL.
3. Link head and tail with node.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedLists:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def create_dll(self, nodeValue):
        node = Node(nodeValue)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
        print("DLL has been created.")
        return


dll = DoublyLinkedLists()
dll.create_dll(1)
print([node.value for node in dll])


"""
OUTPUT:
DLL has been created.
[1]
"""

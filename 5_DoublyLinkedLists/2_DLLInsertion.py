"""
ALGORITHM: INSERTION OF DOUBLY LINKED LISTS
1. Get nodeValue(node to insert) and location(where to insert).
2. Check if head is None. If yes terminate else create new node and assign a value to it and check location to insert.
    (no nodes case)
3. If location is first, NEWNODE.PREV = NONE, NEWNODE.NEXT = HEAD, HEAD.PREV = NEWNODE, HEAD= NEWNODE and terminate else
    check for last location. (insert at start case)
4. If location is last, NEWNODE.NEXT = NONE, NEWNODE.PREV = TAIL, TAIL.NEXT = NEWNODE, TAIL = NEWNODE and terminate else
    find location. (insert at end case)
5. Find location via LOOP, NEWNODE.NEXT = CURRENTNODE.NEXT, NEWNODE.PREV = CURRENTNODE, NEWNODE.NEXT.PREV = NEWNODE
    CURRENTNODE.NEXT = NEWNODE and terminate.
    (insert in the middle case)
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


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

    def insert_node(self, value, location):
        if self.head is None:
            print("No nodes in DLL")
            return
        else:
            newNode = Node(value)
            if location == 0:
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
                print("Node inserted at the beginning of DLL.")
                return
            elif location == 1:
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
                print("Node inserted at the end of DLL.")
                return
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode
                print("Node inserted in the DLL at location: " + str(location))
                return


dll = DoublyLinkedLists()
dll.create_dll(1)
print([node.value for node in dll])
dll.insert_node(value=2, location=0)
print([node.value for node in dll])
dll.insert_node(value=3, location=0)
print([node.value for node in dll])
dll.insert_node(value=4, location=0)
print([node.value for node in dll])
dll.insert_node(value=5, location=1)
print([node.value for node in dll])
dll.insert_node(value=6, location=2)
print([node.value for node in dll])
dll.insert_node(value=7, location=3)
print([node.value for node in dll])

"""
OUTPUT:
DLL has been created.
[1]
Node inserted at the beginning of DLL.
[2, 1]
Node inserted at the beginning of DLL.
[3, 2, 1]
Node inserted at the beginning of DLL.
[4, 3, 2, 1]
Node inserted at the end of DLL.
[4, 3, 2, 1, 5]
Node inserted in the DLL at location: 2
[4, 3, 6, 2, 1, 5]
Node inserted in the DLL at location: 3
[4, 3, 6, 7, 2, 1, 5]
"""



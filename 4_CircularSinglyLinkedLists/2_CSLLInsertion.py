"""
ALGORITHM: INSERTION IN CIRCULAR SINGLY LINKED LISTS
1. Get nodeValue(node to insert) and location(where to insert).
2. Check if head is None. If yes terminate else create new node and assign a value to it and check location to insert.
    (no nodes case)
3. If location is first, NEWNODE.NEXT = HEAD, HEAD = NEWNODE, TAIL.NEXT = NEWNODE and terminate else
    check for last location. (insert at start case)
4. If location is last, NEWNODE.NEXT = TAIL.NEXT, TAIL.NEXT = NEWNODE, TAIL = NEWNODE and terminate else
    find location. (insert at end case)
5. Find location via LOOP, NEWNODE.NEXT = CURRENTNODE.NEXT, CURRENTNODE.NEXT = NEWNODE and terminate.
    (insert in the middle case)
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
            if node.next == self.head:
                break
            node = node.next

    def create_CSLL(self, nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node
        print("CSLL has been created.")
        return

    def insert_node(self, value, location):
        if self.head is None:
            print("No nodes in CSLL.")
            return
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
                print("Node inserted at the beginning of CSLL.")
                return
            elif location == 1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
                print("Node inserted at the end of CSLL.")
                return
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                print("Node inserted in CSLL at location " + str(location))
                return


CSLL = CircularSinglyLinkedLists()
CSLL.create_CSLL(1)
print([node.value for node in CSLL])
CSLL.insert_node(value=2, location=0)
print([node.value for node in CSLL])
CSLL.insert_node(value=3, location=0)
print([node.value for node in CSLL])
CSLL.insert_node(value=4, location=0)
print([node.value for node in CSLL])
CSLL.insert_node(value=5, location=0)
print([node.value for node in CSLL])
CSLL.insert_node(value=6, location=1)
print([node.value for node in CSLL])
CSLL.insert_node(value=22, location=2)
print([node.value for node in CSLL])
CSLL.insert_node(value=33, location=3)
print([node.value for node in CSLL])

"""
OUTPUT:
CSLL has been created.
[1]
Node inserted at the beginning of CSLL.
[2, 1]
Node inserted at the beginning of CSLL.
[3, 2, 1]
Node inserted at the beginning of CSLL.
[4, 3, 2, 1]
Node inserted at the beginning of CSLL.
[5, 4, 3, 2, 1]
Node inserted at the end of CSLL.
[5, 4, 3, 2, 1, 6]
Node inserted in CSLL at location 2
[5, 4, 22, 3, 2, 1, 6]
Node inserted in CSLL at location 3
[5, 4, 22, 33, 3, 2, 1, 6]
"""

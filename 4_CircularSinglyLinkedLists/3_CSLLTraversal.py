"""
ALGORITHM: TRAVERSAL OF CIRCULAR SINGLY LINKED LISTS
1. Check if head is none, if yes terminate, else loop through all nodes and print node values.
2. If current node is the last node referencing head then break.
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

    def insert_node(self, value, location):
        newNode = Node(value)
        if self.head is None:
            print("No nodes in CSLL.")
            return
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location == 1:
                newNode.next = self.tail.next
                self.tail = newNode
                self.tail.next = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

    def traverse_nodes(self):
        if self.head is None:
            print("No nodes in CSLL.")
        else:
            tempNode = self.head
            while tempNode:
                print("Traversing Node: " + str(tempNode.value))
                tempNode = tempNode.next
                if tempNode == self.head:
                    break


CSLL = CircularSinglyLinkedLists()
CSLL.create_CSLL(1)
CSLL.insert_node(value=1, location=0)
CSLL.insert_node(value=2, location=0)
CSLL.insert_node(value=3, location=0)
CSLL.insert_node(value=4, location=1)
CSLL.insert_node(value=5, location=2)
print([node.value for node in CSLL])

CSLL.traverse_nodes()


"""
OUTPUT:
[3, 2, 5, 1, 1]
Traversing Node: 3
Traversing Node: 2
Traversing Node: 5
Traversing Node: 1
Traversing Node: 1
"""
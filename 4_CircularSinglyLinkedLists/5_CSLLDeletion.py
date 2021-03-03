"""
ALGORITHM: DELETION IN CIRCULAR SINGLY LINKED LIST
1. Get node location.
2. Check if head is none, terminate else check first location. (no nodes case)
3. If location is first, (if only one node) HEAD = NULL , TAIL = NULL, FIRST.NEXT = NULL
                         (if many nodes) HEAD = FIRST.NEXT, TAIL.NEXT = HEAD
                         and terminate
                         else check last location. (delete at start case)
4. If location is last, (if only one node) HEAD = NULL, TAIL = NULL, FIRST.NEXT = NULL
                        (if many nodes) Find BEFORELAST node via LOOP, TAIL = CURRENTNODE, CURRENTNODE.NEXT = HEAF
                        and terminate
                        else find location. (delete at end case)
5. Find location via LOOP, CURRENT.NEXT = NEXTNODE.NEXT and terminate. (delete in the middle case)


ALGORITHM: DELETION OF ENTIRE CIRCULAR SINGLY LINKED LIST
    Set HEAD and TAIL to NULL
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

    def search_node(self, nodetoSearch):
        if self.head is None:
            print("No nodes in CSLL.")
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodetoSearch:
                    print("Node Found")
                    return True
                else:
                    tempNode = tempNode.next
                    if tempNode == self.head:
                        break
            print("Node not found")
            return False

    def delete_node(self, location):
        if self.head is None:
            print("No nodes in CSLL.")
            return
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == 1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = self.head
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
        print("Node deleted")
        return

    def delete_entire_csll(self):
        if self.head is None:
            print("No nodes in CSLL.")
        else:
            self.head = None
            self.tail = None
        print("Entire SLL deleted with head as: " + str(self.head) + " and tail as: " + str(self.tail))


CSLL = CircularSinglyLinkedLists()
CSLL.create_CSLL(1)
CSLL.insert_node(value=1, location=0)
CSLL.insert_node(value=2, location=0)
CSLL.insert_node(value=3, location=0)
CSLL.insert_node(value=4, location=1)
CSLL.insert_node(value=5, location=2)
CSLL.insert_node(value=6, location=3)
CSLL.insert_node(value=7, location=1)
print([node.value for node in CSLL])

CSLL.delete_node(location=0)
print([node.value for node in CSLL])
CSLL.delete_node(location=1)
print([node.value for node in CSLL])
CSLL.delete_node(location=2)
print([node.value for node in CSLL])
CSLL.delete_node(location=3)
print([node.value for node in CSLL])


CSLL.delete_entire_csll()
print([node.value for node in CSLL])


"""
ALGORITHM: DELETION IN SINGLY LINKED LIST
1. Get node location.
2. Check if head is none, terminate else check first location. (no nodes case)
3. If location is first, (if only one node) HEAD = NULL , TAIL = NULL,
                         (if many nodes) HEAD = FIRST.NEXT
                         and terminate
                         else check last location. (delete at start case)
4. If location is last, (if only one node) HEAD = NULL, TAIL = NULL,
                        (if many nodes) Find BEFORELAST node via LOOP, BEFORELAST.NEXT = NULL, TAIL = BEFORELAST
                        and terminate
                        else find location. (delete at end case)
5. Find location via LOOP, CURRENT.NEXT = NEXTNODE.NEXT and terminate. (delete in the middle case)


ALGORITHM: DELETION OF ENTIRE SINGLY LINKED LIST
    Set HEAD and TAIL to NULL>
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insert_node(self, value, location):
        newNode = Node(value=value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
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
            print("No nodes in SLL")
        else:
            node = self.head
            while node is not None:
                print("Traversing node: " + str(node.value))
                node = node.next

    def search_node(self, nodetoSearch):
        if self.head is None:
            print("SLL does not exists")
        else:
            print("Searching node: " + str(nodetoSearch))
            node = self.head
            while node is not None:
                if node.value == nodetoSearch:
                    print("Node Found")
                    return node.value
                node = node.next
            print("Node doesn't exist")
            return

    def delete_node(self, location):
        if self.head is None:
            print("No nodes in SLL.")
        else:
            if location == 0:
                print("Deleting node from the beginning of SLL.")
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == 1:
                print("Deleting node from the end of SLL.")
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                print("Deleting node from the SLL at middle location: " + str(location))
                tempNode = self.head
                index = 0
                if index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next

    def delete_entire_sll(self):
        if self.head is None:
            print("No nodes in SLL.")
        else:
            self.head = None
            self.tail = None
        print("Entire SLL deleted with head as: " + str(self.head) + " and tail as: " + str(self.tail))


SLL = SinglyLinkedList()
SLL.insert_node(value=0, location=0)
SLL.insert_node(value=1, location=0)
SLL.insert_node(value=2, location=0)
SLL.insert_node(value=3, location=0)
SLL.insert_node(value=4, location=1)
SLL.insert_node(value=10, location=2)
print([node.value for node in SLL])

SLL.delete_node(0)
print([node.value for node in SLL])
SLL.delete_node(1)
print([node.value for node in SLL])
SLL.delete_node(2)
print([node.value for node in SLL])
SLL.delete_node(3)
print([node.value for node in SLL])

SLL.delete_entire_sll()
print([node.value for node in SLL])


"""
OUTPUT:
[3, 2, 10, 1, 0, 4]
Deleting node from the beginning of SLL.
[2, 10, 1, 0, 4]
Deleting node from the end of SLL.
[2, 10, 1, 0]
Deleting node from the SLL at middle location: 2
[2, 10, 0]
Deleting node from the SLL at middle location: 3
[2, 10]
Entire SLL deleted with head as: None and tail as: None
[]
"""



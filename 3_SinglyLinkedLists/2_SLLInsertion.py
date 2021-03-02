"""
ALGORITHM:
1. Get Node value(node to insert) and location(where to insert)
2. Create a new node and assign value to it.
3. Check if head is none, if yes HEAD = NODE, TAIL = NODE and terminate, else check first location. (no nodes case)
4. If location is first, NODE.NEXT = HEAD, HEAD =  NODE and terminate, else check last location. (insert at start case)
5. If location is last, NODE.NEXT = NULL, LAST.NEXT = NODE, TAIL = NODE and terminate else find location.
    (insert at end case)
6. Find location via LOOP, CURRENT.NEXT = NODE, NODE.NEXT = NEXT NODE and terminate. (insert in the middle case)
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
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            print("Node inserted in an empty SLL.")
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                print("Node inserted at the beginning of SLL.")
            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
                print("Node inserted at the end of SLL.")
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                print("Node inserted in the SLL at location: " + str(location))


SLL = SinglyLinkedList()
SLL.insert_node(value=0, location=0)
print([node.value for node in SLL])
SLL.insert_node(value=1, location=0)
print([node.value for node in SLL])
SLL.insert_node(value=2, location=0)
print([node.value for node in SLL])
SLL.insert_node(value=3, location=0)
print([node.value for node in SLL])
SLL.insert_node(value=4, location=1)
print([node.value for node in SLL])
SLL.insert_node(value=10, location=2)
print([node.value for node in SLL])


"""
OUTPUT:
Node inserted in an empty SLL.
[0]
Node inserted at the beginning of SLL.
[1, 0]
Node inserted at the beginning of SLL.
[2, 1, 0]
Node inserted at the beginning of SLL.
[3, 2, 1, 0]
Node inserted at the end of SLL.
[3, 2, 1, 0, 4]
Node inserted in the SLL at location: 2
[3, 2, 10, 1, 0, 4]
"""
"""
ALGORITHM: SEARCHING IN SINGLY LINKED LISTS
1.  Check if head is none, if yes terminate, else loop through all nodes.
2.  Search node value, if found terminate
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
            print("SLL does not exists")
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


SLL = SinglyLinkedList()
SLL.insert_node(value=0, location=0)
SLL.insert_node(value=1, location=0)
SLL.insert_node(value=2, location=0)
SLL.insert_node(value=3, location=0)
SLL.insert_node(value=4, location=1)
SLL.insert_node(value=10, location=2)
print([node.value for node in SLL])


SLL.search_node(10)

SLL.search_node(100)


"""
OUTPUT:
[3, 2, 10, 1, 0, 4]
Searching node: 10
Node Found
Searching node: 100
Node doesn't exist
"""



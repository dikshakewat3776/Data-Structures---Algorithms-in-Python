"""
ALGORITHM: TRAVERSAL OF DOUBLY LINKED LISTS
    Check if head is none, if yes terminate, else loop through all nodes and print node values
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
        return

    def insert_node(self, value, location):
        if self.head is None:
            print("No nodes in DLL.")
            return
        else:
            newNode = Node(value)
            if location == 0:
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
                return
            elif location == 1:
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
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
                return

    def traverse_nodes(self):
        if self.head is None:
            print("No nodes in SLL.")
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


dll = DoublyLinkedLists()
dll.create_dll(1)
dll.insert_node(value=2, location=0)
dll.insert_node(value=3, location=0)
dll.insert_node(value=4, location=0)
dll.insert_node(value=5, location=1)
dll.insert_node(value=6, location=2)
dll.insert_node(value=7, location=3)
print([node.value for node in dll])
dll.traverse_nodes()


dll.search_node(7)

dll.search_node(77)

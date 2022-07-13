class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head

    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            new_node.prev = node
            node.next = new_node
            self.tail = new_node

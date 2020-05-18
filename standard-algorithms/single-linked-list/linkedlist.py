from node import Node

class LinkedList:
    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0

    def append(self, data):
        if self.tail:
            self.tail.next = Node(data)
            self.tail = self.tail.next
        else:
            self.head = Node(data)
            self.tail = self.head
        self.size += 1

    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def delete(self, data):
        current = self.head
        prev = self.head
        while current.data != data:
            prev = current
            current = current.next
        if current:
            prev.next = current.next
            self.size -= 1

    def contains(self, data):
        current = self.head
        while current and current.data != data:
            current = current.next
        return current != None
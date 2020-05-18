from node import Node

class TwoWaysLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        if self.tail:
            self.tail.next = Node(data)
            self.tail.next.previous = self.tail
            self.tail = self.tail.next
        else:
            self.tail = Node(data)
            self.head = self.tail

    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def delete(self, data):
        current = self.head
        while current.data != data:
            current = current.next
        if current:
            current.previous.next = current.next

    
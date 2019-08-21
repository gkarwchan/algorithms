import node

class LinkedList:
  def __init__(self, head=None):
    self.head = head

  def insert(self, data):
    new_node = node.Node(data)
    new_node.set_next(self.head)
    self.head = new_node
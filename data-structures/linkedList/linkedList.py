class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class SinglyLinkedList:
  def __init__(self):
    self.tail = None
  
  def append(self, data):
    node = Node(data)
    if self.tail == None:
      self.tail = node
    else:
      current = self.tail
      while current.next:
        current = current.next
      current.next = node
  
  def iter(self):
    current = self.tail
    while current:
      val = current.data
      current = current.next
      yield val

if __name__ == '__main__':
  list = SinglyLinkedList()
  list.append(1)
  list.append(2)

  for i in list.iter():
    print(i)
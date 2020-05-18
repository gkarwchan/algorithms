import unittest
from node import Node
from linkedlist import LinkedList


class TestNode(unittest.TestCase):

    def test_toString_should_return_value(self):
        node1 = Node('Sam')
        self.assertEqual(str(node1), 'Sam')

    def test_next(self):
        node1 = Node('Sam')
        node1.next = Node('Harris')
        self.assertEqual(str(node1.next), 'Harris')


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.__element = LinkedList()
        self.__element.append('Sam')
        self.__element.append('Harris')
        self.__element.append('Jessy')

    def tearDown(self):
        self.__element = None

    def test_initialize(self):
        linked = LinkedList()
        self.assertIsNone(linked.tail)

    def test_head_should_always_point_to_first_item(self):
        self.assertEqual(str(self.__element.head), 'Sam')

    def test_tail_should_point_to_last_item(self):
        self.assertEqual(str(self.__element.tail), 'Jessy')

    def test_size_should_report_size(self):
        self.assertEqual(self.__element.size, 3)      

    def test_should_iterate(self):
        vals = [x for x in self.__element.iter()]
        self.assertEqual(vals[0], 'Sam')  
        self.assertEqual(vals[2], 'Jessy')
        self.assertEqual(len(vals), 3)

    def test_delete(self):
        self.__element.delete('Harris')
        vals = [x for x in self.__element.iter()]
        self.assertEqual(vals[1], 'Jessy')
        self.assertEqual(len(vals), 2)
        self.assertEqual(str(self.__element.head.next), 'Jessy')
        self.assertEqual(self.__element.size, 2)

    def test_search(self):
        self.assertFalse(self.__element.contains('Far'))
        self.assertTrue(self.__element.contains('Harris'))



if __name__ == '__main__':
    unittest.main()
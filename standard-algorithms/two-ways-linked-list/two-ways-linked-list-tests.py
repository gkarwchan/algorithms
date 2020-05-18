import unittest
from node import Node
from twowayslinkedlist import TwoWaysLinkedList

class TestNode(unittest.TestCase):

    def test_toString_should_return_value(self):
        node1 = Node('Sam')
        self.assertEqual(str(node1), 'Sam')

    def test_next(self):
        node1 = Node('Sam')
        node1.next = Node('Harris')
        node1.previous = Node('Jessy')
        self.assertEqual(str(node1.next), 'Harris')
        self.assertEqual(str(node1.previous), 'Jessy')

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.__element = TwoWaysLinkedList()
        self.__element.append('Sam')
        self.__element.append('Harris')
        self.__element.append('Jessy')

    def tearDown(self):
        self.__element = None

    def test_should_have_first_element_as_head(self):
        self.assertEqual(str(self.__element.head), 'Sam')

    def test_should_have_last_element_as_tail(self):
        self.assertEqual(str(self.__element.tail), 'Jessy')

    def test_next_should_point_to_next(self):
        self.assertEqual(str(self.__element.head.next), 'Harris')

    def test_previous_should_point_to_previous(self):
        self.assertEqual(str(self.__element.tail.previous), 'Harris')

    def test_iter_should_return_iteration(self):
        vals = [ x for x in self.__element.iter() ]
        self.assertEqual(vals[0], 'Sam')
        self.assertEqual(vals[2], 'Jessy')


if __name__ == '__main__':
    unittest.main()
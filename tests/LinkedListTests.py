import unittest

from datastructs.linkedlist import linkedlist


class LinkedListTests(unittest.TestCase):

    def test_create_empty(self):
        list = linkedlist()
        self.assertTrue(list.head is None, "failed to initialize empty linked list")

    def test_create(self):
        list = linkedlist(5)
        self.assertEqual(list.head.data, 5)
        self.assertTrue(list.head.next is None)

    def test_contains_iterative(self):
        list = linkedlist(5)
        list.append(3)
        list.insert_front(1)
        self.assertTrue(list.contains_iterative(1))
        self.assertTrue(list.contains_iterative(3))
        self.assertTrue(not list.contains_iterative(2))

    def test_contains_recursive(self):
        list = linkedlist(5)
        list.append(3)
        list.insert_front(1)
        self.assertTrue(list.contains_recursive(1))
        self.assertTrue(list.contains_recursive(3))
        self.assertTrue(not list.contains_recursive(2))

    def test_containt_empty_list(self):
        list = linkedlist()
        self.assertTrue(not list.contains_iterative(1))

    def test_delete(self):
        list = linkedlist(2)
        list.append(3)
        list.append(4)
        list.delete_node(3)
        self.assertTrue(not list.contains_iterative(3))

    def test_delete_empty_list(self):
        list = linkedlist()
        list.delete_node(1)

    def test_delete_all(self):
        list = linkedlist(2)
        list.append(3)
        list.append(4)
        list.append(3)
        list.delete_all(3)
        self.assertTrue(not list.contains_iterative(3))

    def test_count_recursive(self):
        list = linkedlist(1)
        for i in range(4):
            list.append(1)
        self.assertEqual(list.get_length_recursive(), 5)

    def test_count_iterative(self):
        list = linkedlist(1)
        for i in range(4):
            list.append(1)
        self.assertEqual(list.get_length_iterative(), 5)

    def test_count_recursive_empty_list(self):
        list = linkedlist()
        self.assertEqual(list.get_length_recursive(), 0)

    def test_count_iterative_empty_list(self):
        list = linkedlist()
        self.assertEqual(list.get_length_iterative(), 0)

    def test_get_nth_element(self):
        list = linkedlist()
        list.append(1)
        self.assertEqual(list.get_nth_element(0), 1)

    def test_get_nth_element_non_existing_index(self):
        list = linkedlist()
        list.append(1)
        self.assertRaises(AssertionError)
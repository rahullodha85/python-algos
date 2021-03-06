import unittest

from rl.datastructs.linkedlist import linkedlist


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

    def test_get_nth_from_end(self):
        list = linkedlist()
        list.append(1)
        list.append(2)
        list.append(3)
        list.append(4)
        self.assertEqual(list.nth_node_from_end(2), 3)
        self.assertEqual(list.nth_node_from_end(1), 4)

    # def test_get_nth_index_larger_than_list_length(self):
    #     list = linkedlist()
    #     self.assertRaises(AssertionError(), list.nth_node_from_end(1))

    def test_middle_node_odd_nodes(self):
        list = linkedlist()
        list.append(1)
        list.append(2)
        list.append(3)
        list.append(4)
        list.append(5)

        self.assertEqual(3, list.middle_node())

    def test_middle_node_even_nodes(self):
        list = linkedlist()
        list.append(1)
        list.append(2)
        list.append(3)
        list.append(4)
        list.append(5)
        list.append(6)

        self.assertEqual(4, list.middle_node())

    def test_get_frequency(self):
        list = linkedlist()
        list.append(1)
        list.append(2)
        list.append(1)

        self.assertEqual(2, list.get_frequency_iterative(1))

    def test_get_frequency_empty_list(self):
        list = linkedlist()

        self.assertEqual(0, list.get_frequency_iterative(1))

    def test_get_frequency_no_number(self):
        list = linkedlist()
        list.append(2)

        self.assertEqual(0, list.get_frequency_iterative(1))

    def test_get_frequency_recursive(self):
        list = linkedlist()
        list.append(1)
        list.append(2)
        list.append(1)

        self.assertEqual(2, list.get_frequency_recursive(list.head, 1))

    def test_get_frequency_recursive_empty_list(self):
        list = linkedlist()

        self.assertEqual(0, list.get_frequency_recursive(list.head, 1))

    def test_get_frequency_recursive_no_number(self):
        list = linkedlist()
        list.append(2)

        self.assertEqual(0, list.get_frequency_recursive(list.head, 1))

    def test_detect_loop_empty_list(self):
        list = linkedlist()
        self.assertFalse(list.detect_loop())

    def test_no_loop_list(self):
        list = linkedlist(1)
        list.append(2)
        list.append(3)
        list.append(4)
        list.append(4)
        list.append(4)
        list.append(4)
        list.append(4)

        self.assertFalse(list.detect_loop())

    def test_loop(self):
        list = linkedlist(1)
        list.append(2)
        list.append(3)
        list.append(4)
        list.append(4)
        list.append(4)

        curr = list.head
        curr.next.next.next.next = curr.next

        self.assertTrue(list.detect_loop())

    def test_length_of_loop(self):
        list = linkedlist(1)
        list.append(2)
        list.append(3)
        list.append(4)
        list.append(5)
        list.append(6)

        curr = list.head
        curr.next.next.next.next = curr.next

        self.assertEqual(3, list.length_of_loop())

    def test_delete_duplicates(self):
        list = linkedlist(1)
        list.append(2)
        list.append(2)
        list.append(2)
        list.append(2)
        list.append(3)

        dict = list.remove_duplicates()

        for key in dict:
            self.assertEqual(1, list.get_frequency_iterative(key))

    def test_delete_duplicates_empty_list(self):
        list = linkedlist()
        dict = list.remove_duplicates()

        self.assertEqual(0, dict.keys().__len__())
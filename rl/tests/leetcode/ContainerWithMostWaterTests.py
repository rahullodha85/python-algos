import unittest

from rl.leetcode.contianer_with_most_water import ContainerWithMostWater


class ContainerWithMostWaterTests(unittest.TestCase):

    def test_brute_force(self):

        test_object = ContainerWithMostWater()

        self.assertEqual(49, test_object.brute_force([1,8,6,2,5,4,8,3,7]))


    def test_two_pointers(self):

        test_object = ContainerWithMostWater()

        self.assertEqual(49, test_object.two_pointer([1,8,6,2,5,4,8,3,7]))

    def test_two_pointers_2(self):

        test_object = ContainerWithMostWater()

        self.assertEqual(1, test_object.two_pointer([1, 1]))
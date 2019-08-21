import unittest

from rl.projecteuler.Multiple3and5 import Multiple3and5


class Multiple3and5Tests(unittest.TestCase):

    def test_brute_force(self):
        test_obj = Multiple3and5()
        self.assertEqual(23, test_obj.brute_force(10))

    def test_math(self):
        test_obj = Multiple3and5()
        self.assertEqual(23, test_obj.math(10))

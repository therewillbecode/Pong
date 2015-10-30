__author__ = 'Tom'
import unittest
from playabout import permutations as permutations

class Test(unittest.TestCase):

    def test_1(self):
        Test.assert_equals(sorted(permutations('a')), ['a'])

    def test_2(self):
        Test.assert_equals(sorted(permutations('ab')), ['ab', 'ba'])

    def test_3(self):
        Test.assert_equals(sorted(permutations('aabb')), ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])

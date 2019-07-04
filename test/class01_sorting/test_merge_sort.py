from unittest import TestCase
from leetcode.class1_sorting.merge_sort import *


class TestMergeSort(TestCase):
    def test_merge_sort(self):
        merge_sort = MergeSort().merge_sort
        self.assertEqual([1, 2, 3, 4], merge_sort([1, 4, 2, 3]))
        self.assertNotEqual([1, 3, 3], merge_sort([1, 3, 2]))
        self.assertEqual([], merge_sort([]))

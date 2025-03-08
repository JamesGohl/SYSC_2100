"""SYSC 2100 Winter 2024 Lab 8: some unit tests for Exercises 1, 2, 3 and 7."""

import unittest

from lab8_binarytree import BinaryTree, \
    build_10_20_30, build_binary_tree, build_perfect_binary_tree


class Build_10_20_30_TestCase(unittest.TestCase):
    """Test build_10_20_30. (Exercise 1)."""

    def test_1(self):
        tree = build_10_20_30()
        # Check the root node
        self.assertEqual(tree._root.x, 10)

        # Check the root's left child
        left_child = tree._root.left
        self.assertEqual(left_child.x, 20)
        self.assertIsNone(left_child.left)
        self.assertIsNone(left_child.right)

        # Check the root's right child
        right_child = tree._root.right
        self.assertEqual(right_child.x, 30)
        self.assertIsNone(right_child.left)
        self.assertIsNone(right_child.right)


class Build_Binary_Tree_TestCase(unittest.TestCase):
    """Test build_binary_tree (Exercise 2)."""


class Build_Perfect_Binary_Tree_TestCase(unittest.TestCase):
    """Test build_perfect_binary_tree. (Exercise 3)."""


class CountTestCase(unittest.TestCase):
    """Test the count method (Exercise 7)."""


if __name__ == '__main__':
    unittest.main(verbosity=2)

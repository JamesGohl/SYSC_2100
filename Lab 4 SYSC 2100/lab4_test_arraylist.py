# SYSC 2100 Winter 2024 Lab 4: Unit tests.

import unittest

from lab4_arraylist import ArrayList


class IterTestCase(unittest.TestCase):
    """Test __iter__."""

    def test_iter1(self):
        """Test iteration over an empty list."""
        lst = ArrayList()
        elems = []
        for elem in lst:
            elems.append(elem)
        self.assertEqual(elems, [])

    def test_iter2(self):
        """Test iteration over a list containing some duplicate elements."""
        lst = ArrayList([1, 4, 4, 1, 9, 4, 6, 6])
        elems = []
        for elem in lst:
            elems.append(elem)
        self.assertEqual(sorted(elems), [1, 1, 4, 4, 4, 6, 6, 9])

# The following classes test the ArrayList methods developed during Lab 4.


class ExtendTestCase(unittest.TestCase):
    """Test extend (Exercise 1)."""


class IndexTestCase(unittest.TestCase):
    """Test index (Exercise 2)."""

    def test_index1(self):
        """Test an empty list."""
        lst = ArrayList()
        with self.assertRaises(ValueError):
            lst.index(10)

    def test_index2(self):
        """Test finding the index of an item that isn't in the list."""
        lst = ArrayList([1, 3, 4, 4, 7, 2, 3])
        with self.assertRaises(ValueError):
            lst.index(10)


class PopTestCase(unittest.TestCase):
    """Test pop (Exercise 3)."""

    def test_pop1(self):
        """Test popping an item from an empty list."""
        lst = ArrayList()
        with self.assertRaises(IndexError):
            lst.pop(0)

    def test_pop2(self):
        """Test popping from a location with an invalid index."""
        lst = ArrayList([1, 3, 4, 4, 7, 2, 3])
        with self.assertRaises(IndexError):
            lst.pop(len(lst))
        with self.assertRaises(IndexError):
            lst.pop(-len(lst) - 1)


class ReversedTestCase(unittest.TestCase):
    """Test __reversed__ (Exercise 4)."""
    # Hint - use the methods in IterTestCase as a starting point for defining
    # test mwthods for the reverse iterator.


if __name__ == '__main__':
    unittest.main(verbosity=2)

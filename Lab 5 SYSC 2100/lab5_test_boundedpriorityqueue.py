"""SYSC 2100 Winter 2024 Lab 5 - Some unit tests for class BoundedPriorityQueue."""

import unittest

from collections import deque

from lab5_boundedpriorityqueue import BoundedPriorityQueue

NUM_LEVELS = 10


def build_priority_queue() -> BoundedPriorityQueue:
    """Return a priority queue with NUM_LEVELS levels, containing 6 items
    added in order listed here: ("purple", 5), ("black", 0), ("orange", 3),
    ("white", 0), ("green", 1), ("yellow", 5)
    """
    pq = BoundedPriorityQueue(NUM_LEVELS)
    pq.add("purple", 5)
    pq.add("black", 0)
    pq.add("orange", 3)
    pq.add("white", 0)
    pq.add("green", 1)
    pq.add("yellow", 5)
    return pq


class InitTestCase(unittest.TestCase):
    """Test __init__"""

    # The tests in this class access the "private" attributes (instance
    # variables) in the BoundedPriorityQueue object directly, because __init__
    # is the first method we implement, so most of the other methods won't be
    # available.

    def test_init1(self):
        """Verify pq = BoundedPriorityQueue(NUM_LEVELS) creates an empty priority queue with NUM_LEVELS levels"""
        pq = BoundedPriorityQueue(NUM_LEVELS)
        self.assertEqual(pq._num_items, 0)
        self.assertEqual(len(pq._queues), NUM_LEVELS)

        # Verify that the BoundedPriorityQueue's array contains NUM_LEVELS
        # empty deques.

        for i in range(NUM_LEVELS):
            self.assertIsInstance(pq._queues[i], deque)
            self.assertEqual(len(pq._queues[i]), 0)

    def test_init2(self):
        """Verify pq = BoundedPriorityQueue(num_levels) raises a ValueError if num_levels <= 0"""
        with self.assertRaises(ValueError):
            pq = BoundedPriorityQueue(0)

        with self.assertRaises(ValueError):
            pq = BoundedPriorityQueue(-1)


class StrTestCase(unittest.TestCase):
    """Test __str__."""

    def test_str1(self):
        """Verify str(pq) using pq = BoundedPriorityQueue(NUM_LEVELS)"""
        pq = BoundedPriorityQueue(NUM_LEVELS)
        self.assertEqual(str(pq), "[]")

    # The following test won't pass until we've implemented the add method.

    def test_str2(self):
        """Verify str(pq) after ("purple", 5), ("black", 0), ("orange", 3), ("white", 0), ("green", 1), ("yellow", 5) added to an empty priority queue"""
        pq = build_priority_queue()
        self.assertEqual(str(pq), "[(0, 'black'), (0, 'white'), (1, 'green'), (3, 'orange'), (5, 'purple'), (5, 'yellow')]")


class ReprTestCase(unittest.TestCase):
    """Test __repr__."""

    def test_repr1(self):
        """Verify repr(pq) using pq = BoundedPriorityQueue(NUM_LEVELS)"""
        pq = BoundedPriorityQueue(NUM_LEVELS)
        self.assertEqual(repr(pq), 'BoundedPriorityQueue({0})'.format(NUM_LEVELS))


class LenTestCase(unittest.TestCase):
    """Test __len__ ."""

    def test_len1(self):
        """Verify len(pq) using pq = BoundedPriorityQueue(NUM_LEVELS)"""
        pq = BoundedPriorityQueue(NUM_LEVELS)
        self.assertEqual(len(pq), 0)

    # The following test won't pass until we've implemented the add method.

    def test_len2(self):
        """Verify len(pq) after ("purple", 5), ("black", 0), ("orange", 3), ("white", 0), ("green", 1), ("yellow", 5) added to an empty priority queue"""
        pq = build_priority_queue()
        self.assertEqual(len(pq), 6)


# The following classes test the methods developed during Lab 5.

class AddTestCase(unittest.TestCase):
    """Test add (Exercise 3)."""

    def test_add1(self):
        """Verify pq = BoundedPriorityQueue(NUM_LEVELS), pq.add("purple", 5)"""
        pq = BoundedPriorityQueue(NUM_LEVELS)
        pq.add("purple", 5)

        self.assertEqual(len(pq), 1, msg='len(pq) should return 1')

        # Verify that the item we added is in the correct queue.
        # BoundedPriorityQueue doesn't provide accessor methods,
        # so we access the queues directly.

        self.assertEqual(pq._queues[5][0], "purple", msg='pq._queues[5][0] should contain "purple"')
        self.assertEqual(len(pq._queues[5]), 1, msg='len(ps._queues[5]) should return 1')

    def test_add2(self):
        """Verify pq = BoundedPriorityQueue(NUM_LEVELS), pq.add("purple", 5), pq.add("black", 0)"""
        pq = BoundedPriorityQueue(NUM_LEVELS)
        pq.add("purple", 5)
        pq.add("black", 0)

        self.assertEqual(len(pq), 2, msg='len(pq) should return 2')

        self.assertEqual(pq._queues[0][0], "black", msg='pq._queues[0][0] should contain "black"')
        self.assertEqual(len(pq._queues[0]), 1, msg='len(ps._queues[0]) should return 1')
        self.assertEqual(pq._queues[5][0], "purple", msg='pq._queues[5][0] should contain "purple"')
        self.assertEqual(len(pq._queues[5]), 1, msg='len(ps._queues[5]) should return 1')

    def test_add_valueerror(self):
        """Verify pq = BoundedPriorityQueue(NUM_LEVELS), pq.add("pink", -1), pq.add("red", 6)"""
        pq = BoundedPriorityQueue(NUM_LEVELS)

        with self.assertRaises(ValueError, msg='pq.add("pink", -1) should raise a ValueError'):
            pq.add("pink", -1)

        with self.assertRaises(ValueError, msg='pq.add("red", NUM_LEVELS) should raise a ValueError'):
            pq.add("red", NUM_LEVELS)


class RemoveTestCase(unittest.TestCase):
    """Test remove (Exercise 4)."""

    def test_remove1(self):
        """Verify pq = BoundedPriorityQueue(NUM_LEVELS), pq.add("purple", 5), pq.add("black", 0), pq.remove(), pq.remove()"""
        pq = BoundedPriorityQueue(NUM_LEVELS)
        pq.add("purple", 5)
        pq.add("black", 0)

        self.assertEqual(pq.remove(), "black", msg='First pq.remove() should return "black"')
        self.assertEqual(pq.remove(), "purple", msg='Second pq.remove() should return "purple"')

        self.assertEqual(len(pq), 0, 'len(pq) should return 0')

        # Check the length of the queues from which the elements were removed.
        self.assertEqual(len(pq._queues[0]), 0, msg='len(pq._queues[0]) should be 0')
        self.assertEqual(len(pq._queues[5]), 0, msg='len(pq._queues[5]) should be 0')

    def test_remove_indexerror(self):
        """Verify pq = BoundedPriorityQueue(NUM_LEVELS), pq.remove() raises a ValueError (empty priority queue)."""
        pq = BoundedPriorityQueue(NUM_LEVELS)

        # Attempt to remove an element from an empty BoundedPriorityQueue.
        with self.assertRaises(IndexError, msg='pq.remove() should raise an IndexError'):
            pq.remove()


if __name__ == '__main__':
    unittest.main(verbosity=2)

# Class BinaryHeap implements the priority queue interface, using a min-heap
# as the underlying data structure. (The lower the value of an element, the
# higher its priority.) The remove/delete_min operations remove the
# highest-priority element.
#
# Some code in this module was adapted from code from the Open Data Structures
# project, opendatastructures.org.
#
# This code (and the code from which it was derived) is released under a
# Creative Commons Attribution (CC BY) license. The full text of the license is
# available here:
#
# http://creativecommons.org/licenses/by/2.5/ca/

__author__ = 'bailey'
__version__ = '1.01'
__date__ = 'Mar. 24, 2023'

# History:
# Version 1.00 March 23, 2023 - Modified the array-based BinaryHeap to store the
#                               heap's tree in a list instead of an array.
# Version 1.01 March 24, 2023 - Updated comments.

# Class BinaryHeap stores a heap as a complete binary tree. Typically,
# the tree is represesented as an array, with the nodes arranged in
# breadth-first order. (The root is stored at index 0, the root's left
# child is stored at index 1, the root's right child is stored at index 2,
# etc.)

# BinaryHeap uses a Python list instead of an array, because (unlike a
# fixed-capacity array), a list keeps track of the number of objects it
# contains and it will increase its capacity as required.

# Given the index of a node, we can call these functions to determine the
# index of the node's parent, left child and right child.


def left(i: int) -> int:
    """Return the index of the left child of the node at index i.
    """
    return 2 * i + 1


def right(i: int) -> int:
    """Return the index of the right child of the node at index i.
    """
    return 2 * (i + 1)


def parent(i: int) -> int:
    """Return the index of the parent of the node at index i."""
    return (i - 1) // 2


class BinaryHeap:

    def __init__(self, iterable=[]) -> None:
        """Initialize this BinaryHeap.

        If no iterable is provided, the new BinaryHeap is empty.
        Otherwise, initialize the BinaryHeap by inserting the values
        provided by the iterable.
        """
        self._elems = []
        for elem in iterable:
            self.add(elem)

    def __str__(self) -> str:
        """Return a string representation of this BinaryHeap."""
        # Use repr(x) instead of str(x) in the list comprehension so that
        # elements of type str are enclosed in quotes.
        return "[{0}]".format(", ".join([repr(x) for x in self]))

    def __repr__(self) -> str:
        """Return the canonical string representation of this BinaryHeap."""
        # For a BinaryHeap object, obj, the expression eval(repr(obj))
        # returns a new BinaryHeap that is identical to obj.
        return "{0}({1})".format(self.__class__.__name__, str(self))

    def __len__(self) -> int:
        """Return the number of elements in this BinaryHeap."""
        return len(self._elems)

    def __iter__(self):
        """Return an iterator for this BinaryHeap.

        Elements are returned in breadth-first order, starting with the
        root of the heap's tree.
        """
        # for i in range(len(self)):
        #     yield self._elems[i]

        return iter(self._elems)   # Use the list's iterator.

    def add(self, x: any) -> None:
        """Insert x in this BinaryHeap."""

        # Store x in a new node in the heap's tree, ensuring that it remains
        # a complete binary tree.
        # The heap contains n elements stored at indices 0 .. n - 1 in
        # self._elems, so x must be stored at index n.
        self._elems.append(x)

        # "Bubble" x up the heap's tree until the heap property has been
        # restored.
        self._bubble_up(len(self) - 1)

    def _bubble_up(self, i: int) -> None:
        """A new element was stored at index i in the heap's "array" (list).
        Bubble this element up the tree until the heap has been reformed.
        """
        # Repeatedly swap the element at index i with its parent, until the
        # element is is no longer smaller than its parent.
        p = parent(i)
        while i > 0 and self._elems[i] < self._elems[p]:
            self._elems[i], self._elems[p] = self._elems[p], self._elems[i]
            i = p
            p = parent(i)

    def remove(self) -> any:
        """Remove the smallest value from this BinaryHeap and return it.

        Raises IndexError if the heap is empty.
        """
        if len(self) == 0:
            raise IndexError('remove: empty heap')

        x = self._elems[0]  # Smallest value is in the root.

        # Replace the root element with the value from the rightmost node in
        # the lowest level of the heap's tree, then delete that node.
        # The node is located at index n - 1 in the list, where n == len(self).
        self._elems[0] = self._elems[len(self) - 1]

        # Call pop to remove the rightmost node/reduce the list's length by 1.
        # We don't need the value returned by pop, as it has already been
        # copied to the root.
        self._elems.pop()

        # "Trickle" the root element down the heap's tree until the heap
        # property has been restored.
        self._trickle_down(0)

        return x

    # Provide delete_min as a synonym for remove.
    delete_min = remove

    def _trickle_down(self, i: int) -> None:
        """Starting with the element stored at index i in the heap's array,
        trickle this element down the tree until the heap has been reformed.
        """
        # Repeatedly swap the element at index i with its smallest child,
        # until the element is no longer larger than its children.

        n = len(self)
        while i >= 0:
            # j will be assigned the index of the child that will be
            # swapped with the element at index i.
            j = -1
            r = right(i)
            # Elements are stored at indices 0..n-1, so the element at
            # index i has a right child at index r if r < n.
            if r < n and self._elems[r] < self._elems[i]:
                # This chunk of code handles the case where the element at
                # index i has two children and the element is larger than
                # the right child, so we need to swap the element with its
                # smallest child.
                # Determine which of the two children will be swapped with
                # the element.
                l = left(i)
                if self._elems[l] < self._elems[r]:
                    # The left child is the smallest child.
                    j = l
                else:
                    # The right child is the smallest child.
                    j = r
            else:
                l = left(i)
                # The element at index i has a left child if l < n.
                if l < n and self._elems[l] < self._elems[i]:
                    # This chunk of code handles two cases:
                    # Case 1: the element at index i has one child (a left
                    # child) and the element is larger than that child, so we
                    # need to swap the element and its child.
                    # Case 2: the element at index i has two children and the
                    # element is smaller than the right child, but larger than
                    # the left child.
                    # For both cases, the left child will be swapped with the
                    # element.
                    j = l

            # No swap is required if the element at index i is a leaf or is
            # smaller than its children. In that case, j is still -1.
            if j >= 0:
                # Swap element at index i with its child at index j.
                self._elems[j], self._elems[i] = self._elems[i], self._elems[j]

            # If a swap occurred, the element we're trickling down is now
            # at index j. If no swap occurred, j is -1, and we're done.
            i = j

    def peek(self) -> any:
        """Return, but don't remove, the smallest value in this BinaryHeap.

        Raises IndexError if the heap is empty.
        """
        if len(self) == 0:
            raise IndexError("peek: empty heap")
        return self._elems[0]

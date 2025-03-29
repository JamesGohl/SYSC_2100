# An implementation of ADT Map that uses a binary search tree as the
# underlying data structure.

# Some methods were adapted from methods in class BinarySearchTree in Lee and
# Hubbard's "Data Structures and Algorithms with Python", Section 6.5.1.

__author__ = 'James Gohl'
__student_number__ = '101299043'


class BSTMap:

    class _Node:
        def __init__(self, key: any, value: any, left: '_Node' = None, right: '_Node' = None) -> None:
            """Initialize a node containing a key, the value associated with
            the key, and links to the node's left and right children.
            """
            self.key = key
            self.value = value
            self.left = left
            self.right = right

        def __iter__(self):
            """Return an iterator that performs an inorder traversal of the
            tree rooted at this node, returning the keys.
            """
            if self.left is not None:
                for elem in self.left:
                    yield elem

            yield self.key

            if self.right is not None:
                for elem in self.right:
                    yield elem

    def __init__(self, iterable=[]) -> None:
        """Initialize this BSTMap.

        If no iterable is provided, the map is empty.
        Otherwise, initialize the map by inserting the key/value pairs
        provided by the iterable.

        Precondition: the iterable is a sequence of tuples, with each tuple
        containing one (key, value) pair.

        >>> map = BSTMap()
        >>> map
        {}

        # In this example each key/value pair is a tuple containing a
        # 6-digit student number (an int) and that student's letter grade
        # (a str).

        >>> grades = BSTMap([(111537, 'A+'), (101156, 'A+'), (127118, 'B')])
        >>> grades
        {101156: 'A+', 111537: 'A+', 127118: 'B', }
        """
        self._root = None

        # Number of entries in the map; i.e., the number of key/value pairs.
        self._num_entries = 0

        for key, value in iterable:
            self[key] = value  # updates self._num_entries

    def __str__(self) -> str:
        """Return a string representation of this BSTMap (inorder traversal of
        the nodes), using the format: "{key_1: value_1, key_2: value_2, ...}"

        >>> grades = BSTMap([(111537, 'A+'), (101156, 'A+'), (127118, 'B')])
        >>> str(grades)
        "{101156: 'A+', 111537: 'A+', 127118: 'B'}"
        """
        # Use repr(x) instead of str(x) in the list comprehension so that
        # elements of type str are enclosed in quotes.
        return "{{{0}}}".format(", ".join([repr(key) + ': ' + repr(self[key]) for key in self]))

    __repr__ = __str__

    def __iter__(self):
        """Return an iterator that performs an inorder traversal of the nodes
        in this BSTMap, returning the keys.
        """
        if self._root is not None:
            return self._root.__iter__()
        else:
            # The tree is empty, so use an empty list's iterator
            # as the tree's iterator.
            return iter([])

        """
        New code added by James Gohl 1001299043
        """

    def __setitem__(self, key: any, value: any) -> 'BSTMap._Node':
        """ Adds the key value pair to the map
        or  changes the value if the key already exists
        >>> grades = BSTMap([(111537, 'A+'), (101156, 'A+'), (127118, 'B')]) 
        >>> grades[123] = "A+"
        >>> grades
        {123: 'A+', 101156: 'A+', 111537: 'A+', 127118: 'B'}

        """
        def _add(node: 'BSTMap._Node', key: any, value: any) -> 'BSTMap._Node':
            """Insert x into the binary search tree rooted at node and
            return the reference to tree's root node.
            """
            if node is None:
                self._num_entries += 1
                return self._Node(key, value)
            if node.key < key:
                node.right = _add(node.right, key, value)
            elif node.key > key:
                node.left = _add(node.left, key, value)
            else:
                node.value = value
            return node
            # return node

        self._root = _add(self._root, key, value)

    def __getitem__(self, key: any) -> any:
        """ Returns the value value associated with the key
        or  raises a key error if the key isnt in the map
        >>> grades = BSTMap([(111537, 'A+'), (101156, 'A+'), (127118, 'B')]) 
        >>> grades[111537] 
        'A+'

        """
        def _get(node: 'BSTMap._Node', key: any) -> any:
            """Find the value of the key recursively and raise KeyError
            is no key exists.
            """
            if node is None:
                raise KeyError(key)
            if node.key < key:
                return _get(node.right, key)
            elif node.key > key:
                return _get(node.left, key)
            if node.key == key:
                return node.value

        return _get(self._root, key)

    def get(self, key: any, default=None) -> any:
        """ Returns the value value associated with the key
        or  returns a default value or passed in default value Nne
        >>> grades = BSTMap([(111537, 'A+'), (101156, 'A+'), (127118, 'B')]) 
        >>> grades.get(111537)
        'A+'
        >>> grades.get(1, "test")
        "test"
        >>> grades.get(1)
        default
        """
        def _get(node: 'BSTMap._Node', key: any, default) -> any:
            """Find the value of the key recursively and raise default
            is no key exists.
            """
            if node is None:
                return default
            if node.key < key:
                return _get(node.right, key, default)
            elif node.key > key:
                return _get(node.left, key, default)
            if node.key == key:
                return node.value

        return _get(self._root, key, default)

    def __len__(self) -> int:
        """
        Returns the length of the ditionary
        >>> grades = BSTMap([(111537, 'A+'), (101156, 'A+'), (127118, 'B')]) 
        >>> len(grades)
        >>> 3
        """
        return self._num_entries

    """
    ADD DOC STRING
    """

    def _contains(self, node: 'BSTMap._Node', key: any):
        if node is None:
            return False
        if key < node.key:
            return self._contains(node.left, key)
        if key > node.key:
            return self._contains(node.right, key)
        else:
            return True

    def __contains__(self, key):
        return self._contains(self._root, key)





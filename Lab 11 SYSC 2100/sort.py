# SYSC 2100 Winter 2023 Lab 11/Asst 2

def bubble_sort(a, n: int) -> None:
    """Bubble sort the first n elements of a into ascending order.

    Precondition: a is a mutable sequence; e.g., a list or a fixed-capacity
    array.

    Best case: list is already sorted in ascending order.
    >>> a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> bubble_sort(a_list, len(a_list))
    >>> a_list
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    Worst case: list is sorted in descending order.
    >>> a_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    >>>  bubble_sort(a_list, len(a_list))
    >>> a_list
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]


def selection_sort(a, n: int) -> None:
    """Sort the first n elements of a into ascending order.

    Precondition: a is a mutable sequence; e.g., a list or a fixed-capacity
    array.
    """
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            a[min_idx], a[i] = a[i], a[min_idx]


def insertion_sort(a, n: int) -> None:
    """Sort the first n elements of a into ascending order.

    Precondition: a is a mutable sequence; e.g., a list or a fixed-capacity
    array.
    """
    for i in range(1, n):
        elem = a[i]
        j = i

        # Search for the location j where we'll insert element a[i]
        # while shifting the elements stored in a[j] .. a[i-1] to the right,
        # to make room for a[i]

        while j > 0 and a[j - 1] > elem:
            a[j] = a[j - 1]
            j -= 1
        a[j] = elem


def heapsort(a, n: int) -> None:
    """ Sort the first n elements in a into ascending order.

    Precondition: a is a mutable sequence; e.g., a list or a fixed-capacity
    array.

    This function is an "in-place" implementation of the heapsort algorithm
    in which the running time to build the initial heap is O(n) and the
    running time to remove all elements from the heap is O(n log n).

    To sort all the elements in a list:

    >>> lst = []
    >>> for i in range(10):
    ...     lst.append(random.randint(1, 100))
    ...
    >>> lst
    [99, 95, 21, 18, 65, 50, 5, 53, 32, 77, 70]

    >>> heapsort(lst, len(lst))
    >>> lst
    [5, 18, 21, 32, 50, 53, 65, 70, 77, 95, 99]
    """
    # Form a[0] .. a[n - 1] into a min-heap.

    # The following for loop is equivalent to:
    # m = n div 2
    # for i in m - 1, m - 2, m - 3, ..., 0 do:
    for i in range(n // 2 - 1, -1, -1):
        trickle_down(a, i, n)

    # Sort a[0] .. a[n - 1] into descending order.

    i = n
    while i > 1:
        i -= 1
        # Remove the smallest element from the heap (located at (at a[0])
        # by swapping it and the rightmost child on the lowest level.
        a[i], a[0] = a[0], a[i]

        # Treat a[0] .. a[i-1] as a heap, except the root element may not be
        # in the correct position.
        # Reform a[0] .. a[i-1] into a heap, by trickling the root element
        # down the heap's tree until the heap property has been restored.
        trickle_down(a, 0, i)

        # Now, a[0] .. a[i-1] is a min heap, and a[i] .. a[n - 1]
        # contains the elements that were removed from the heap, sorted in
        # descending order.

    # Rearrange a's elements into ascending order.
    reverse(a, n)


# For a detailed description of the trickle-down algorithm,
# see method _trickle_down in class BinaryHeap.


def trickle_down(a, i: int, n: int) -> None:
    """Starting with the element stored at index i in the heap's array,
    trickle this element down the tree until the heap has been reformed.

    The heap has n elements.
    """
    # Repeatedly swap the element at index i with its smallest child,
    # until the element is no longer larger than its children.

    while i >= 0:
        j = -1
        r = right(i)
        if r < n and a[r] < a[i]:
            l = left(i)
            if a[l] < a[r]:
                j = l
            else:
                j = r
        else:
            l = left(i)
            if l < n and a[l] < a[i]:
                j = l

        if j >= 0:
            a[j], a[i] = a[i], a[j]
        i = j


def left(i: int) -> int:
    """Return the index of the left child of the node at index i in the array.
    """
    return 2 * i + 1


def right(i: int) -> int:
    """Return the index of the right child of the node at index i in the array.
    """
    return 2 * (i + 1)


def parent(i: int) -> int:
    """Return the index of the parent of the node at index i in the array."""
    return (i - 1) // 2


def reverse(a, n):
    """Reverse the first n elements of sequence a in place."""
    for i in range(n // 2):
        a[i], a[n - 1 - i] = a[n - 1 - i], a[i]


def quick_sort(a, n: int) -> None:
    """Quick sort the first n elements of a into ascending order.

    Precondition: a is a mutable sequence; e.g., a list or a fixed-capacity
    array.

    Note: this version of the code is different form the one provide in the lecture note.
    For your exam please use the one provided in the lecture notes.

    A stack approach was used here to get over the limitation in Python.
    """
    stack = [(0, n - 1)]

    while stack:
        low, high = stack.pop()
        if low < high:
            pivot_idx = partition(a, low, high)
            if pivot_idx - low < high - pivot_idx:
                stack.append((low, pivot_idx - 1))
                stack.append((pivot_idx + 1, high))
            else:
                stack.append((pivot_idx + 1, high))
                stack.append((low, pivot_idx - 1))

def partition(a, low, high):
    pivot = a[high]
    i = low - 1
    for j in range(low, high):
        if a[j] < pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[high] = a[high], a[i + 1]
    return i + 1


def merge_sort(a, n: int) -> None:
    """Sort the first n elements of a into ascending order using merge sort.
    """
    def merge(left, right):
        result = []
        left_idx, right_idx = 0, 0

        while left_idx < len(left) and right_idx < len(right):
            if left[left_idx] < right[right_idx]:
                result.append(left[left_idx])
                left_idx += 1
            else:
                result.append(right[right_idx])
                right_idx += 1

        result.extend(left[left_idx:])
        result.extend(right[right_idx:])
        return result

    if n > 1:
        mid = n // 2
        left_half = a[:mid]
        right_half = a[mid:]

        merge_sort(left_half, len(left_half))
        merge_sort(right_half, len(right_half))

        a[:] = merge(left_half, right_half)

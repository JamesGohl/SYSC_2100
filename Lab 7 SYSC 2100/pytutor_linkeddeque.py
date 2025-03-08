class LinkedDeque:
    
    class _Node:
        def __init__(self, item: any) -> None:
            self.item = item
            self.prev = None
            self.next = None

    def __init__(self, iterable=[]) -> None:
        # A LinkedDeque always has one "dummy" node that never contains any of
        # the items that are stored in the deque. The dummy node's next
        # attribute points to the node at the head of the linked list,
        # and the prev attribute points to the node at the tail of the
        # linked list.

        # _dummy always points to the dummy node.
        self._dummy = LinkedDeque._Node(None)
        self._dummy.prev = self._dummy
        self._dummy.next = self._dummy

        self._num_items = 0  # of items stored in the LinkedDeque

        for elem in iterable:
            self.append(elem)
            # append() updates self._num_items

    def __len__(self) -> int:
        return self._num_items

    def __iter__(self):
        cursor = self._dummy.next  # Skip over the dummy node.
        while cursor is not self._dummy:
            yield(cursor.item)
            cursor = cursor.next

    def _insert_before(self, node: 'LinkedDeque._Node', x: any) -> None:
        pass

    def _remove(self, node: 'LinkedDeque._Node') -> None:
        pass

    def append(self, x: any) -> None:
        pass

    def appendleft(self, x: any) -> None:
        pass

    def pop(self) -> any:
        pass

    def popleft(self) -> any:
        pass

dq = LinkedDeque()
dq.append(40)
dq.append(50)
dq.append(60)

dq = LinkedDeque()
dq.appendleft(30)
dq.appendleft(20)
dq.appendleft(10)

dq = LinkedDeque([10, 20, 30, 40])
x = dq.pop()
x = dq.pop()
x = dq.popleft()
x = dq.popleft()

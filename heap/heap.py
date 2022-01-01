class Heap:
    """
    An implementation of an array-based min heap.

    Attributes:
        _data: the data stored in the heap.

    Methods:
        __init__
        __len__
        __repr__
        add
        peek
        poll
        _parent_index
        _left_child_index
        _right_child_index
        _has_parent
        _has_left_child
        _has_right_child
        _parent
        _left_child
        _right_child
        _swap
        _heap_down
        _heap_up
    """

    def __init__(self) -> None:
        """Initialise an empty heap."""
        self._data = []

    def __len__(self) -> int:
        """Calculate the number of elements in the heap."""
        return len(self._data)

    def __repr__(self) -> str:
        """Return a string representation of the heap object."""
        values = ", ".join(repr(value) for value in self._data)
        return f"{self.__class__.__name__}({values})"

    def add(self, item: int) -> None:
        """
        Add a value to the heap and then restore the heap condition.

        Arguments:
            item: the value to add to the heap.
        """
        self._data.append(item)
        self._heap_up()

    def peek(self) -> int:
        """Return the value at the root of the heap (minimum)."""
        if self:
            return self._data[0]
        else:
            raise IndexError("Heap is empty")

    def poll(self):
        """
        Remove and return the value at the root of the heap (minimum)
        and then restore the heap condition.
        """
        if self._data:
            self._swap(0, len(self._data) - 1)
            result = self._data.pop()
            self._heap_down()
            return result
        else:
            raise IndexError("Heap is empty")

    def _parent_index(self, index: int) -> int:
        """Return the index of the parent of a value in the heap."""
        return int((index - 1) / 2)

    def _left_child_index(self, index: int) -> int:
        """Return the index of the left child of a value in the heap."""
        return index * 2 + 1

    def _right_child_index(self, index: int) -> int:
        """Return the index of the right child of a value in the heap."""
        return index * 2 + 2

    def _has_parent(self, index: int) -> bool:
        """
        Returns a bool indicating whether value in heap has a parent.

        Arguments:
            index: index of the value to test.
        """
        return False if index == 0 else True

    def _has_left_child(self, index: int):
        """
        Returns a bool indicating whether value in heap has a left child.

        Arguments:
            index: index of the value to test.
        """
        try:
            self._data[self._left_child_index(index)]
            return True
        except IndexError:
            return False

    def _has_right_child(self, index: int):
        """
        Returns a bool indicating whether value in heap has a left child.

        Arguments:
            index: index of the value to test.
        """
        try:
            self._data[self._right_child_index(index)]
            return True
        except IndexError:
            return False

    def _parent(self, index: int):
        """
        Return the value of the parent of the value at the given index.

        Arguments:
            index: the index of the value whose parent to return.
        """
        return self._data[self._parent_index(index)]

    def _left_child(self, index: int):
        """
        Return the value of the right child of the value at the given index.

        Arguments:
            index: the index of the value whose right child to return.
        """
        return self._data[self._left_child_index(index)]

    def _right_child(self, index: int):
        """
        Return the value of the right child of the value at the given index.

        Arguments:
            index: the index of the value whose right child to return.
        """
        return self._data[self._right_child_index(index)]

    def _swap(self, i: int, j: int):
        """
        Swaps the values at the specified two indexes in the heap.

        Arguments:
            i: one of the indexes to swap values between.
            j: the other index to swap values between.
        """
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _heap_down(self) -> None:
        """
        Swap min (root) value in heap with children until
        the heap condition is restored
        """
        index = 0
        while self._has_left_child(index):
            child_index = self._left_child_index(index)
            if self._has_right_child(index):
                if self._left_child(index) > self._right_child(index):
                    child_index = self._right_child_index(index)
            if self._data[index] < self._data[child_index]:
                break
            else:
                self._swap(index, child_index)
            index = child_index

    def _heap_up(self) -> None:
        """
        Swap min (root) value in heap with parents until
        the heap condition is restored
        """
        index = len(self) - 1
        while self._has_parent(index):
            if self._data[index] < self._parent(index):
                self._swap(index, self._parent_index(index))
                index = self._parent_index(index)
            else:
                break

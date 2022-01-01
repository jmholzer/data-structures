from typing import Any

class Stack:
    """
    Implementation of an array-based stack.

    Attributes:
        _items: the data stored in the stack.

    Methods:
        __init__
        __repr__
        __len__
        push
        pop
    """

    def __init__(self) -> None:
        """Initialise an empty stack."""
        self._items = []

    def __repr__(self) -> str:
        """Return a string representation of the stack."""
        values = ", ".join(repr(value) for value in self._items)
        return f"{self.__class__.__name__}({values})"

    def __len__(self) -> int:
        """Calculate the length of the stack."""
        return len(self._items)

    def push(self, item: Any) -> None:
        """
        Add data to the stack (end of array).
        
        Arguments:
            item: the data to add to the stack.
        """
        self._items.append(item)

    def pop(self) -> Any:
        """Remove the top-most item (at end of array) from the stack."""
        return self._items.pop()


    def top(self) -> Any:
        """Return the value at the top of the stack (end of array)."""
        return self._items[-1]

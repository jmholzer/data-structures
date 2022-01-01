from __future__ import annotations
from typing import Any
from typing import Optional
from typing import Generator


class Queue:
    """
    An implementation of an array-based queue.

    Attributes:
        _items: a list (array) containing the data in the queue.
    
    Methods:
        __init__
        __repr__
        __iter__
        __getitem__
        enqueue
        dequeue
        front
    """

    def __init__(self) -> None:
        """Initialise an empty queue."""
        self._items = []

    def __repr__(self) -> str:
        """Return a string representation of the queue object."""
        items_repr = ", ".join(repr(item) for item in self._items)
        return f"{self.__class__.__name__}({items_repr})"

    def __iter__(self) -> Generator[Any, None, None]:
        """Return an generator for the queue object."""
        for x in self._items:
            yield x
    
    def __getitem__(self, key) -> Any:
        """
        Return the data at a specified index in the queue.
        
        Arguments:
            key: the index from which to return data.
        """
        return self._items[key]

    def enqueue(self, data) -> None:
        """
        Enqueue data at the back of the queue (head has index 0).
        
        Arguments:
            key: the data to store in the queue
        """
        self._items.append(data)

    def dequeue(self) -> Any:
        """
        Dequeue data from the front of the queue and return it.
        Head has index 0.
        """
        if self._items:
            return(self._items.pop(0))

    def front(self) -> Optional[Any]:
        """Return data at the front of the queue (head has index 0)."""
        if self._items:
            return self._items[0]
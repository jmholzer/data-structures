from __future__ import annotations
from typing import Any
from typing import Optional
from typing import Generator
from copy import deepcopy


class Node:
    """
    A structure containing data, and (optionally) a pointer to another node.

    Attributes:
        key: the key associated with the data stored in the node.
        data: the data stored in the node.
        next: a pointer to another node.

    Methods:
        __init__
        __repr__
    """

    def __init__(
        self,
        key: Optional[Any] = None,
        data: Optional[Any] = None,
        next: Optional[Node] = None,
    ) -> Node:
        """Initialise a node with the supplied data and next pointer."""
        self.key = key
        self.data = data
        self.next = next

    def __repr__(self) -> str:
        """
        Return a string representation of the node.
        eval() will not construct an object if self.next points to another node.
        """
        # Stop very long recursions for repr of nodes in linked lists
        if self.next.__class__.__name__ == "Node":
            next_repr = "Node"
        else:
            next_repr = self.next
        return f"{self.__class__.__name__}({self.key}: {self.data}, {next_repr})"


class HashTable:
    """
    An implementation of a hash table.

    Attributes:
        _load: the number of stored key, data pairs in the hash map.
        _array: a list storing the head node of a linked list.

    Methods:
        __init__
        __repr__
    """

    def __init__(self):
        """Initialise an empty hash map."""
        self._load = 0
        self._array = [Node() for _ in range(16)]

    def __getitem__(self, key: Any) -> Any:
        """
        Return the data associated with the given key.

        Arguments:
            key: the key used to store the data.
        """
        key_hash = hash(key) % len(self._array)
        cursor = self._array[key_hash]
        while cursor and cursor.key != key:
            cursor = cursor.next
        if cursor:
            return cursor.data
        else:
            raise KeyError(f"{key}")

    def __setitem__(self, key: Any, value: Any) -> None:
        """
        Insert a key and associated data into the hash table.

        Arguments:
            key: the key used to store the data.
            value: the data to store in the hash table
        """
        if not key:
            raise TypeError("Invalid key")
        key_hash = hash(key) % len(self._array)
        cursor = self._array[key_hash]
        while cursor.key and cursor.next:
            cursor = cursor.next
        if cursor.key:
            cursor.next = Node(key, value, None)
        else:
            cursor.key, cursor.data = key, value
        self._load += 1
        if self._rehash_needed():
            self._rehash()

    def __delitem__(self, key: Any) -> None:
        """
        Remove a key, item pair from the hash table.

        Arguments:
            key: the key for which to delete the (key, item) pair.
        """
        key_hash = hash(key) % len(self._array)
        prev = cursor = self._array[key_hash]
        index = 0
        while cursor and cursor.key != key:
            prev, cursor = cursor, cursor.next
            index += 1
        if cursor:
            if index == 0:
                self._array[key_hash] = (
                    self._array[key_hash].next if cursor.next else Node()
                )
            else:
                prev.next = cursor.next if cursor else None
        else:
            raise KeyError(f"{key}")

    def _rehash_needed(self) -> None:
        """Check if the load factor of the hash table is above 0.75."""
        if self._load / len(self._array) > 0.75:
            return True
        else:
            return False

    def _rehash(self) -> None:
        """Double the size of the hash table array to reduce the load factor."""
        old_array = deepcopy(self._array)
        self._array = [Node() for _ in range(2 * len(self._array))]
        self._load = 0

        for cursor in old_array:
            while cursor and cursor.key:
                self[cursor.key] = cursor.data
                cursor = cursor.next

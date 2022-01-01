from __future__ import annotations
from typing import Any
from typing import Optional
from typing import Generator


class Node:
    def __init__(self, data, next: Optional[Node] = None) -> Node:
        """Initialise a node with the supplied data and next pointer."""
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
        return f"{self.__class__.__name__}({self.data}, {next_repr})"


class LinkedList:
    def __init__(self) -> LinkedList:
        """Initialise an empty linked list object."""
        self.head = None

    def __repr__(self) -> str:
        """
        Return a String representation of the linked list.
        eval() will NOT construct an object.
        """
        return (
            "LinkedList(" + ", ".join((str(node.data) for node in self)) + ")"
        )

    def __iter__(self) -> Generator[Node, None, None]:
        """Turns the object into an iterable."""
        cursor = self.head
        while cursor:
            yield cursor
            cursor = cursor.next

    def __getitem__(self, key: int) -> Node:
        """
        Allows index-based access to the object (i.e linked_list[0]).

        Arguments:
            key: the 0-based position of the node to return.
        """
        if key < 0:
            key = len(self) + key
        for idx, cursor in enumerate(self):
            if idx == key:
                return cursor
        raise IndexError

    def __setitem__(self, key: int, data: Any) -> None:
        """
        Set the data contained in a node at a given position.

        Arguments:
            key: the 0-based position of the node to change.
            data: the data to set in the given node.
        """
        self[key].data = data

    def __len__(self) -> int:
        """Calculate the length of the linked list."""
        return sum(1 for _ in self)

    def __eq__(self, other: LinkedList) -> bool:
        """
        Determine whether the linked list is equivalent to another
        ('equivalent' => same data value in each node).

        Arguments:
            other: the linked list being compared to.
        """
        if type(self) != type(other):
            return False
        if len(self) != len(other):
            return False
        for node_self, node_other in zip(self, other):
            if node_self.data != node_other.data:
                return False
        return True

    def insert(self, key: int, data: Any) -> None:
        """
        Insert a new node containing the given data into the list after
        a specified node.

        Arguments:
            key: the index of the node after which to insert the new node.
            data: the data the new node will contain.
        """
        if not self.head:
            self.head = Node(data)
        # If key is out of range, __getitem__ raises IndexError.
        elif self[key]:
            left_node = self[key]
            new_node = Node(data, left_node.next)
            left_node.next = new_node

    def remove(self, key: int) -> None:
        """
        Remove the element with the specified index from the linked list.

        Arguments:
            key: the index of the element to remove.
        """
        # If keys are out of range, __getitem__ raises IndexError.
        self[key]
        if key == 0:
            self.head = self[key].next
        else:
            left_node = self[key - 1]
            left_node.next = self[key].next

    def append(self, data: Any) -> None:
        """
        Add a new node containing the given data to the foot-side
        of the linked list.

        Arguments:
            data: the data the new node will contain.
        """
        length = len(self)
        key = 0 if length == 0 else length - 1
        self.insert(key, data)

    def prepend(self, data: Any) -> None:
        """
        Add a new node containing the given data to the head-side
        of the linked list.

        Arguments:
            data: the data the new node will contain.
        """
        self.head = Node(data, self.head)

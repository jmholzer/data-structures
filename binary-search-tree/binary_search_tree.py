from __future__ import annotations
from typing import Any
from typing import Optional
from typing import Union


class Node:
    """
    A binary tree node, containing a key and two pointers to child nodes.

    Attributes:
        key: the key stored in the node.
        left: the left child of the node.
        right: the right child of the node.

    Methods:
        __init__
        __repr__
    """

    def __init__(
        self,
        key: Any,
        parent: Union[Node, None],
        left: Optional[Node] = None,
        right: Optional[Node] = None,
    ) -> None:
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent

    def __repr__(self) -> str:
        """
        Return a string representation of the node.
        eval() will not construct an object if self.next points to another node.
        """

        # Stop very long recursions for repr of nodes in trees.
        parent_repr = "Node" if self.parent else None
        left_repr = "Node" if self.left else None
        right_repr = "Node" if self.right else None

        return f"{self.__class__.__name__}({self.key}, {parent_repr}, {left_repr}, {right_repr})"


class BinarySearchTree:
    """
    An implementation of a binary search tree that allows storing duplicates.

    Attributes:
        root: the root node in the binary search tree.

    Methods:
        __init__
        insert
        _insert
    """

    def __init__(self) -> None:
        """Initialise the binary search tree with no nodes."""
        self.root = None

    def insert(self, key: Any) -> None:
        """
        Public insert method -- the interface used to insert key
        into the binary search tree. Assigns the result of _insert
        to the root attribute and avoids the consumer having to
        specify a node.

        Arguments:
            key: the key to insert.
        """
        self.root = self._insert(key, None, self.root)

    def _insert(
        self, key: Any, parent: Union[Node, None], cursor: Union[Node, None]
    ) -> Node:
        """
        Private insert method -- used by self.insert to insert nodes.

        Arguments:
            key: the key to insert.
            cursor: the node to consider as the root for recursive insertion.
        """
        if cursor is None:
            return Node(key, parent=parent)
        else:
            if key == cursor.key:
                pass
            elif key < cursor.key:
                cursor.left = self._insert(key, cursor, cursor.left)
            else:
                cursor.right = self._insert(key, cursor, cursor.right)
        return cursor

    def search(self, key: Any) -> Any:
        """
        Public search method -- searches the tree for a given key
        and returns the node that contains it. Avoids the consumer
        having to specify a start-node for recursive search.

        Arguments:
            key: the key to search the tree for.
        """
        return self._search(key, self.root)

    def _search(self, key: Any, cursor: Union[Node, None]) -> Any:
        """
        Private search method -- recursively searches the tree starting
        at a given node.

        Arguments:
            key: the key to search the tree for
            cursor: the node to consider as the root for recursive search.
        """
        if not cursor or cursor.key == key:
            return cursor

        if key < cursor.key:
            return self._search(key, cursor.left)
        else:
            return self._search(key, cursor.right)

    def delete(self, key: Any) -> None:
        pass

    def _successor(self, cursor: Node) -> Node:
        """
        Returns the node in the tree with the smallest key that is
        greater than the key of the given node.

        Arguments:
            cursor: the node to find the successor of.
        """
        if cursor.right:
            return self._minimum(cursor.right)
        
        parent = cursor.parent
        while parent and cursor == parent.right:
            cursor = parent
            parent = cursor.parent
        return parent

    def _minimum(self, cursor: Node) -> Node:
        """
        Returns the minimum node in the tree that has cursor as its root.

        Arguments:
            cursor: the node to use as the root of the tree.
        """
        while cursor.left:
            cursor = cursor.left
        return cursor

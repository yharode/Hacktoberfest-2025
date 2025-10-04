from collections import deque

class Node:
    """Represents a single node in a Binary Tree.

    Attributes:
        val (any): The value stored in the node.
        left (Node): Reference to the left child node.
        right (Node): Reference to the right child node.
    """
    def __init__(self, val):
        """Initialize a node with a value.

        Args:
            val (any): The value to be stored in the node.
        """
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    """A general Binary Tree (not necessarily a Binary Search Tree).

    Supports insertion (level-order), traversal (inorder, preorder, postorder, level-order),
    finding, deleting, computing height, and counting nodes.
    """

    def __init__(self):
        """Initialize an empty Binary Tree."""
        self.root = None

    def insert(self, val):
        """Insert a new node in level-order (left-to-right).

        This keeps the tree as complete as possible.

        Args:
            val (any): The value to insert into the tree.
        """
        new_node = Node(val)
        if not self.root:
            self.root = new_node
            return

        q = deque([self.root])
        while q:
            node = q.popleft()
            if not node.left:
                node.left = new_node
                return
            else:
                q.append(node.left)

            if not node.right:
                node.right = new_node
                return
            else:
                q.append(node.right)

    def inorder(self, node):
        """Perform inorder traversal (Left → Root → Right).

        Args:
            node (Node): The starting node (usually self.root).
        """
        if node:
            self.inorder(node.left)
            print(node.val, end=" ")
            self.inorder(node.right)

    def preorder(self, node):
        """Perform preorder traversal (Root → Left → Right).

        Args:
            node (Node): The starting node (usually self.root).
        """
        if node:
            print(node.val, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        """Perform postorder traversal (Left → Right → Root).

        Args:
            node (Node): The starting node (usually self.root).
        """
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.val, end=" ")

    def level_order(self):
        """Perform level-order traversal (Breadth-First Search).

        Prints all node values from top to bottom, left to right.
        """
        if not self.root:
            return
        q = deque([self.root])
        while q:
            node = q.popleft()
            print(node.val, end=" ")
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    def size(self, node):
        """Return the total number of nodes in the tree.

        Args:
            node (Node): The starting node.

        Returns:
            int: The number of nodes in the subtree rooted at 'node'.
        """
        if not node:
            return 0
        return 1 + self.size(node.left) + self.size(node.right)

    def height(self, node):
        """Compute the height of the tree (in terms of edges).

        To get height in terms of number of nodes, change base case to 0.

        Args:
            node (Node): The starting node.

        Returns:
            int: Height of the tree (edge count).
        """
        if not node:
            return -1
        return 1 + max(self.height(node.left), self.height(node.right))

    def find(self, val):
        """Find and return the node containing a given value.

        Args:
            val (any): Value to search for.

        Returns:
            Node or None: The node containing 'val', or None if not found.
        """
        if not self.root:
            return None
        q = deque([self.root])
        while q:
            node = q.popleft()
            if node.val == val:
                return node
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return None

    def delete(self, val):
        """Delete a node by replacing it with the deepest node.

        Steps:
            1. Find the node with the given value.
            2. Find the deepest-rightmost node in the tree.
            3. Replace the value of the target node with the deepest node's value.
            4. Remove the deepest node from the tree.

        Args:
            val (any): The value of the node to delete.

        Returns:
            bool: True if deletion was successful, False otherwise.
        """
        if not self.root:
            return False

        # Case: single root node
        if not self.root.left and not self.root.right:
            if self.root.val == val:
                self.root = None
                return True
            return False

        q = deque([self.root])
        node_to_delete = None
        last_node = None

        while q:
            last_node = q.popleft()
            if last_node.val == val:
                node_to_delete = last_node
            if last_node.left:
                q.append(last_node.left)
            if last_node.right:
                q.append(last_node.right)

        if node_to_delete:
            node_to_delete.val = last_node.val
            self._delete_deepest(last_node)
            return True
        return False

    def _delete_deepest(self, deepest):
        """Helper to remove the deepest node in the tree.

        Args:
            deepest (Node): The deepest node to be deleted.
        """
        q = deque([self.root])
        while q:
            node = q.popleft()
            if node.left:
                if node.left == deepest:
                    node.left = None
                    return
                else:
                    q.append(node.left)
            if node.right:
                if node.right == deepest:
                    node.right = None
                    return
                else:
                    q.append(node.right)


# Example usage
if __name__ == "__main__":
    bt = BinaryTree()
    for val in [10, 20, 30, 40, 50, 60, 70]:
        bt.insert(val)

    print("Level-order: ", end="")
    bt.level_order()
    print("\nInorder: ", end="")
    bt.inorder(bt.root)
    print("\nPreorder: ", end="")
    bt.preorder(bt.root)
    print("\nPostorder: ", end="")
    bt.postorder(bt.root)
    print()

    print("Size:", bt.size(bt.root))
    print("Height (edges):", bt.height(bt.root))
    print("Find 50:", bt.find(50) is not None)
    print("Delete 30:", bt.delete(30))
    print("Level-order after delete:", end=" ")
    bt.level_order()
    print()

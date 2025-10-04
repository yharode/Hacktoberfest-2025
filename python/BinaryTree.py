from collections import deque

class Node:
    """Node structure for Binary Tree"""
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    """A general Binary Tree (not BST) implementation"""
    def __init__(self):
        self.root = None

    def insert(self, val):
        """Insert node in level order (keeps tree complete)"""
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
        if node:
            self.inorder(node.left)
            print(node.val, end=" ")
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.val, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.val, end=" ")

    def level_order(self):
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
        if not node:
            return 0
        return 1 + self.size(node.left) + self.size(node.right)

    def height(self, node):
        """Height in terms of edges. For nodes count, change base case to 0."""
        if not node:
            return -1
        return 1 + max(self.height(node.left), self.height(node.right))

    def find(self, val):
        """Find node with specific value (BFS search)"""
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
        """Delete node by replacing with deepest node value"""
        if not self.root:
            return False

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
        """Helper to remove the deepest node"""
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

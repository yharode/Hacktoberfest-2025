from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Node({self.val})"

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
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
            q.append(node.left)
            if not node.right:
                node.right = new_node
                return
            q.append(node.right)

    # Traversals return lists instead of printing
    def inorder(self, node):
        return self.inorder(node.left) + [node.val] + self.inorder(node.right) if node else []

    def preorder(self, node):
        return [node.val] + self.preorder(node.left) + self.preorder(node.right) if node else []

    def postorder(self, node):
        return self.postorder(node.left) + self.postorder(node.right) + [node.val] if node else []

    def level_order(self):
        if not self.root:
            return []
        result = []
        q = deque([self.root])
        while q:
            node = q.popleft()
            result.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        return result

    def size(self, node):
        return 1 + self.size(node.left) + self.size(node.right) if node else 0

    def height(self, node):
        return 1 + max(self.height(node.left), self.height(node.right)) if node else -1

    def find(self, val):
        if not self.root:
            return None
        q = deque([self.root])
        while q:
            node = q.popleft()
            if node.val == val:
                return node
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        return None

    def delete(self, val):
        if not self.root:
            return False
        if self.root.val == val and not self.root.left and not self.root.right:
            self.root = None
            return True

        q = deque([self.root])
        node_to_delete = None
        last_node = None

        while q:
            last_node = q.popleft()
            if last_node.val == val:
                node_to_delete = last_node
            if last_node.left: q.append(last_node.left)
            if last_node.right: q.append(last_node.right)

        if node_to_delete:
            node_to_delete.val = last_node.val
            self._delete_deepest(last_node)
            return True
        return False

    def _delete_deepest(self, deepest):
        q = deque([self.root])
        while q:
            node = q.popleft()
            if node.left:
                if node.left == deepest:
                    node.left = None
                    return
                q.append(node.left)
            if node.right:
                if node.right == deepest:
                    node.right = None
                    return
                q.append(node.right)

# Example usage
if __name__ == "__main__":
    bt = BinaryTree()
    for val in [10, 20, 30, 40, 50, 60, 70]:
        bt.insert(val)

    print("Level-order:", bt.level_order())
    print("Inorder:", bt.inorder(bt.root))
    print("Preorder:", bt.preorder(bt.root))
    print("Postorder:", bt.postorder(bt.root))
    print("Size:", bt.size(bt.root))
    print("Height (edges):", bt.height(bt.root))
    print("Find 50:", bt.find(50) is not None)
    print("Delete 30:", bt.delete(30))
    print("Level-order after delete:", bt.level_order())

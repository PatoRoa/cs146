# Given the root of a binary tree, invert the tree, and return its root.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_tree():
    root = TreeNode(1)

    # Left subtree
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)

    # Right subtree
    root.right = TreeNode(8)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)

    return root


def invertTree(root):
    if root is None:
        return None

    if root:
        # Swap subtree roots
        root.left, root.right = root.right, root.left

        # Swap subtree leaves recursively
        invertTree(root.left)
        invertTree(root.right)

    return root


def print_tree(root):
    if root:
        # Print root
        print(root.val)

        # Print subtrees recursively
        print_tree(root.left)
        print_tree(root.right)


tree = create_tree()
print_tree(tree)
print("\n")

inverted_tree = invertTree(tree)
print_tree(inverted_tree)

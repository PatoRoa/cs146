# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_tree():
    root = TreeNode(4)

    # Left subtree
    root.left = TreeNode(3)
    root.left.left = TreeNode(1)

    # Right subtree
    root.right = TreeNode(8)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(9)

    return root


def isValidBST(root):
    # Utilizing a secondary function that traverses the tree recursively, returning a boolean value
    def validifier(root, lower_bound, upper_bound):
        # Base case where the traversal runs its course and doesn't run into a reason to flag the BST as invalid
        if root is None:
            return True

        # The deciding comparison; checks if any of the children don't fit the rule of thumb of a BST
        if root.val <= lower_bound or root.val >= upper_bound:
            return False

        # Runs the function recursively, using the comparative statement and the resulting boolean value from the
        # checker, while using the root's value as an upper bound or lower bound for comparisons in case it's a
        # duplicate
        return validifier(root.left, lower_bound, root.val) and \
            validifier(root.right, root.val, upper_bound)

    # Kicks off the function
    return validifier(root, float('-inf'), float('inf'))


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

print(isValidBST(tree))

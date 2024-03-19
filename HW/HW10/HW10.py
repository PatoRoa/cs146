# Given the root of a binary tree, return the level order traversal of its nodes' values.
# (i.e., from left to right, level by level).
#
# Constraints:
#   • The number of nodes in the tree is in the range [0, 2000].
#   • -1000 <= TreeNode value <= 1000
from typing import List
from typing import Optional
import collections
import queue


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


def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    # List of lists to be returned
    level_order_list = []

    # Obligatory test case 2 prevention
    if root is None:
        return None

    # Queue time babey, getting it started with the trees root
    que = queue.Queue()
    que.put(root)

    # Since the queue starts with one, it'll only finish looping when it reaches 0, which is supposed to happen when
    # it's done its thing with all the nodes in the tree
    while que.qsize() != 0:
        # Amount of nodes at the current level
        cu_nodes = que.qsize()

        # List of nodes at the current level to be added to the main list
        cu_nodes_list = []

        # "For as many nodes in the level, remove the node in the queue, check the node's validity and add it to the
        # list and put its children in the queue
        for i in range(cu_nodes):
            # Take node out of the queue
            node = que.get()

            # Check node validity
            if node:
                # Add node to a list
                cu_nodes_list.append(node.val)

                # Put its children in the queue for later processing
                que.put(node.left)
                que.put(node.right)

        # If the list ends up not being empty, append it to the main list
        if cu_nodes_list:
            level_order_list.append(cu_nodes_list)

    return level_order_list


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

print(levelOrder(tree))

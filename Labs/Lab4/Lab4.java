public class Lab4 {
    public static void main (String[] args) {
        TreeNode tree = new TreeNode();
        tree = createTree();

        printTree(tree);
        System.out.println("\n");

        TreeNode invertedTree = new TreeNode();
        invertedTree = invertTree(tree);

        printTree(invertedTree);
    }

    public static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode() {}
        TreeNode(int val) { this.val = val; }
        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    public static TreeNode createTree() {
        TreeNode root = new TreeNode(1);

        // Left subtree
        root.left = new TreeNode(2);
        root.left.left = new TreeNode(3);
        root.left.right = new TreeNode(4);

        // Right subtree
        root.right = new TreeNode(8);
        root.right.left = new TreeNode(5);
        root.right.right = new TreeNode(6);

        return root;
    }

    public static TreeNode invertTree(TreeNode root) {
        if (root == null) {
            return null;
        }
        else {
            // Swap subtree roots
            TreeNode temp = new TreeNode();
            temp = root.left;
            root.left = root.right;
            root.right = temp;

            // Swap subtree leaves recursively
            invertTree(root.left);
            invertTree(root.right);
        }

        return root;
    }

    public static void printTree(TreeNode root) {
        if (root != null) {
            // Print root
            System.out.println(root.val);

            // Print subtrees recursively
            printTree(root.left);
            printTree(root.right);
        }
    }
}

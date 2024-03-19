import java.util.*;

public class HW10 {
    public static void main (String[] args) {
        TreeNode tree = new TreeNode();
        tree = createTree();

        printTree(tree);
        System.out.println("\n");

        System.out.print(levelOrder(tree));
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
        TreeNode root = new TreeNode(4);

        // Left subtree
        root.left = new TreeNode(3);
        root.left.left = new TreeNode(1);

        // Right subtree
        root.right = new TreeNode(8);
        root.right.left = new TreeNode(5);
        root.right.right = new TreeNode(9);

        return root;
    }

    public static List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> levelOrderList = new ArrayList<>();

        if (root == null) {
            return null;
        }

        Queue<TreeNode> que = new LinkedList<>();
        que.add(root);

        while (!que.isEmpty()) {
            int cUNodes = que.size();

            List<Integer> cUNodesList = new ArrayList<>();

            for (int i = 0; i < cUNodes; i++) {
                TreeNode node = que.remove();

                if (node != null) {
                    cUNodesList.add(node.val);

                    que.add(node.left);
                    que.add(node.right);
                }
            }

            if (!cUNodesList.isEmpty()) {
                levelOrderList.add(cUNodesList);
            }
        }

        return levelOrderList;
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

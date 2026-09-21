/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
        /*
        #########################################################################
        #                                                                       #
        #  =============================================                        #
        #                  SIDDARDHA CHILUVERU                                  #
        #  =============================================                        #
        #                                                                       #
        #  Author      : Siddardha Chiluveru                                    #
        #  Description : Solution / Code / Project                              #
        #  Date        : 2026-12-08                                             #
        #                                                                       #
        #########################################################################
        */
    List<Integer> ans = new ArrayList<>();
    public List<Integer> rightSideView(TreeNode root) {
        // dfs(root ,0);



        //BFS
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        while (!q.isEmpty()) {
            TreeNode r = null;
            int n = q.size();
            for (int i = 0; i < n; i++) {
                TreeNode node = q.poll();
                if (node != null) {
                    r = node; // atlast the last right elemnt comes
                    q.add(node.left);
                    q.add(node.right);
                }
            }
            if (r != null)
                ans.add(r.val);
        }
        return ans;
    }
    // public void dfs(TreeNode node, int d) {
    //     if (node == null)
    //         return;
    //     if (d == ans.size())
    //         ans.add(node.val);
    //     d += 1;
    //     dfs(node.right, d);
    //     dfs(node.left, d);
    // }
}
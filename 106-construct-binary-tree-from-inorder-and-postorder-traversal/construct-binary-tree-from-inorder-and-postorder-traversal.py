# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None

        def get_childs(stop, parent_stop):
            nonlocal in_idx, post_idx
            left, right = None, None

            if in_idx >= 0 and post_idx >= 0 and inorder[in_idx] != stop:
                root_val = postorder[post_idx]
                post_idx -= 1
                right = TreeNode(*get_childs(root_val, stop))

            if in_idx >= 0 and inorder[in_idx] == stop:
                in_idx -= 1

            if in_idx >= 0 and post_idx >= 0 and inorder[in_idx] != parent_stop:
                root_val = postorder[post_idx]
                post_idx -= 1
                left = TreeNode(*get_childs(root_val, parent_stop))
            return stop, left, right

        n = len(postorder)

        in_idx = n - 1
        post_idx = n - 2

        root_val = postorder[n - 1]
        return TreeNode(*get_childs(root_val, None))
        
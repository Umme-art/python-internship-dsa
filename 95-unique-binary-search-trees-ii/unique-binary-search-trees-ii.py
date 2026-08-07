# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[Optional[TreeNode]]
        """
        # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


        if n == 0:
            return []

        def build(start, end):
            trees = []

            if start > end:
                trees.append(None)
                return trees

            for i in range(start, end + 1):
                leftTrees = build(start, i - 1)
                rightTrees = build(i + 1, end)

                for left in leftTrees:
                    for right in rightTrees:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        trees.append(root)

            return trees

        return build(1, n)
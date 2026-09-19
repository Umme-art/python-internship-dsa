class Solution:
    def kthSmallest(self, root, k):
        self.count = 0
        self.ans = 0

        def helper(root):
            if root is None:
                return

            helper(root.left)

            self.count += 1

            if self.count == k:
                self.ans = root.val
                return

            if self.count < k:
                helper(root.right)

        helper(root)

        return self.ans
        
class SegmentTree:
    def __init__(self, s):
        self.n = len(s)
        self.s = list(s)
        self.left = [0] * (4 * self.n)
        self.right = [0] * (4 * self.n)
        self.best = [0] * (4 * self.n)

        self.build(1, 0, self.n - 1)

    def build(self, node, l, r):
        if l == r:
            self.left[node] = 1
            self.right[node] = 1
            self.best[node] = 1
            return

        mid = (l + r) // 2

        self.build(node * 2, l, mid)
        self.build(node * 2 + 1, mid + 1, r)

        self.merge(node, l, r)

    def merge(self, node, l, r):
        left_node = node * 2
        right_node = node * 2 + 1

        mid = (l + r) // 2

        self.left[node] = self.left[left_node]
        self.right[node] = self.right[right_node]

        self.best[node] = max(
            self.best[left_node],
            self.best[right_node]
        )

        if self.s[mid] == self.s[mid + 1]:
            self.best[node] = max(
                self.best[node],
                self.right[left_node] + self.left[right_node]
            )

            if self.right[left_node] == mid - l + 1:
                self.left[node] += self.left[right_node]

            if self.left[right_node] == r - mid:
                self.right[node] += self.right[left_node]

    def update(self, node, l, r, pos, char):
        if l == r:
            self.s[pos] = char
            self.left[node] = 1
            self.right[node] = 1
            self.best[node] = 1
            return

        mid = (l + r) // 2

        if pos <= mid:
            self.update(node * 2, l, mid, pos, char)
        else:
            self.update(node * 2 + 1, mid + 1, r, pos, char)

        self.merge(node, l, r)


class Solution:
    def longestRepeating(self, s, queryCharacters, queryIndices):
        tree = SegmentTree(s)

        answer = []

        for i in range(len(queryIndices)):
            tree.update(
                1,
                0,
                len(s) - 1,
                queryIndices[i],
                queryCharacters[i]
            )

            answer.append(tree.best[1])

        return answer
        
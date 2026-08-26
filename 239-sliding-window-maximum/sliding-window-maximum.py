class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que = deque()
        ans = []
        n = len(nums)

        # First window handling
        for i in range(k):
            while que and nums[que[-1]] < nums[i]:
                que.pop()
            que.append(i)

        # Maximum of the first window
        ans.append(nums[que[0]])

        # Process remaining windows
        for i in range(k, n):

            # Remove indices that are outside the current window
            if que and que[0] <= i - k:
                que.popleft()

            # Remove smaller elements from the right
            while que and nums[que[-1]] < nums[i]:
                que.pop()

            # Add current index
            que.append(i)

            # Front contains the maximum element
            ans.append(nums[que[0]])

        return ans
        
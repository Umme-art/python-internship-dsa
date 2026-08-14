class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash = set(nums)
        longest = 0

        for num in hash:
            if (num - 1) not in hash:
                current_streak = 1
                current = num
        
                while current+1 in hash:
                    current_streak+=1
                    current+=1
                longest = max(longest,current_streak)
        return longest
        
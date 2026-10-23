class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        n=len(nums)
        maxi=-1
        for i in range(n):
            if i!=nums[i]:
                maxi&=nums[i]
        return 0 if maxi==-1 else maxi
        
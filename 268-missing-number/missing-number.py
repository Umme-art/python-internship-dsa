class Solution:
    def missingNumber(self, nums):
        """
        APPROACH:
        We will calculate the sum of numbers from 0 to n
        and subtract the sum of elements present in the array.

        STEP 1 -> Sum of first n natural numbers:
                  n * (n + 1) / 2
                  Say this is SUM1

        STEP 2 -> Find the sum of all elements in the array
                  Say this is SUM2

        STEP 3 -> Subtract:
                  SUM1 - SUM2

                  *** MISSING NUMBER = SUM1 - SUM2 ***
        """

        
        n = len(nums)
        sum1 = n * (n + 1) // 2
        sum2 = 0

        for i in range(n):
            sum2 += nums[i]

        return sum1 - sum2
        
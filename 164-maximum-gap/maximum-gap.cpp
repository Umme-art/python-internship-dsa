class Solution {
public:
    int maximumGap(vector<int>& nums) {

        if (nums.size() < 2)
            return 0;

        int maxGap = 0;

        // Step 1: Sort the array.
        sort(nums.begin(), nums.end());

        // Step 2: Compare adjacent elements and track the maximum gap.
        for (int i = 0; i < nums.size() - 1; i++) {

            int newDiff = nums[i + 1] - nums[i];

            if (newDiff > maxGap)
                maxGap = newDiff;
        }

        return maxGap;
    }
};

/*
📝 Quick Dry Run

Input:
nums = [3, 6, 9, 1]

After Sorting:
[1, 3, 6, 9]

Adjacent Gaps:
3 - 1 = 2
6 - 3 = 3
9 - 6 = 3

Maximum Gap = 3

Return 3.
*/
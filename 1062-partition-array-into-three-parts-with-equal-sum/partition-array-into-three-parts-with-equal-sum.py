class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)

        if total % 3 != 0:
            return False

        target = total // 3
        count = 0
        s = 0

        for num in arr:
            s += num

            if s == target:
                count += 1
                s = 0

        return count >= 3
        
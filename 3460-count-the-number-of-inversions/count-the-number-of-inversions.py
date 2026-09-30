# class Solution:
#     def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
#         MOD = 10 ** 9 + 7
#         # return len(requirements)
        
#         dp = [[0] * (n * (n - 1) // 2 + 1) for _ in range(n + 1)]
#         dp[0][0] = 1

#         for i in range(1, n + 1):
#             for j in range(n * (n - 1) // 2 + 1):
#                 dp[i][j] = 0
#                 for k in range(i):
#                     if j >= k:
#                         dp[i][j] = (dp[i][j] + dp[i - 1][j - k]) % MOD

#         result = 0
#         def isValidPermutation(permutation):
#             inversions = 0
#             for endi, cnti in requirements:
#                 inversions = sum(1 for i in range(endi + 1) for j in range(i + 1, endi + 1) if permutation[i] > permutation[j])
#                 if inversions != cnti:
#                     return False
#             return True

#         from itertools import permutations
#         for perm in permutations(range(n)):
#             if isValidPermutation(perm):
#                 result = (result + 1) % MOD

#         return result
from typing import List
class Solution:
    def numberOfPermutations(self, n: int, reqs: List[List[int]]) -> int:
        MOD = 10**9 + 7
        MAX_INV = 400
        
        r = {}
        for req in reqs:
            r[req[0] + 1] = req[1]
        
        pc = [[0] * (MAX_INV + 1) for _ in range(n + 1)]
        pc[0][0] = 1
        
        # Fill the DP table
        for length in range(1, n + 1):
            for inv in range(MAX_INV + 1):
                for pos in range(length):
                    prev_inv = inv - pos
                    if prev_inv >= 0:
                        pc[length][inv] = (pc[length][inv] + pc[length - 1][prev_inv]) % MOD
            
            if length in r:
                target_inv = r[length]
                for inv in range(MAX_INV + 1):
                    if inv != target_inv:
                        pc[length][inv] = 0
        
        res = sum(pc[n]) % MOD
        return res
        

# https://leetcode.com/problems/arithmetic-slices/

class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        cumu = 0
        total = 0
        for i in range(2, len(A)):
            if A[i] + A[i - 2] != A[i - 1] << 1:
                cumu = 0
            else:
                cumu += 1
                total += cumu
        return total

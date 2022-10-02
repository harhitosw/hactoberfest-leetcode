# https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = []
        ct = 0
        i = 0
        n = len(nums)
        if n==0:
            return 0
        while(i<n):
            if nums[i]!=val:
                ct += 1
                l.append(nums[i])
            i += 1
        i=0
        while(i<ct):
            nums[i] = l[i]
            i += 1
        return ct
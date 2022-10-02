# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            diff= target-nums[i]
            if diff in nums[i+1:]:
                ind= nums[i+1:].index(diff)
                return [i,ind+i+1]
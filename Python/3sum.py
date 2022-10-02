# https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        l = []
        for i in range(n-2):
            k = n-1
            j = i+1
            while(j < k):
                sm = nums[i] + nums[j] + nums[k]
                if sm==0:
                    l.append([nums[i],nums[j],nums[k]])
                    k -= 1
                    j += 1
                elif sm < 0:
                    j += 1
                else:
                    k -= 1
        return [list(item) for item in set(tuple(row) for row in l)]
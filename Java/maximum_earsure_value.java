// 1695. Maximum Erasure Value

// https://leetcode.com/problems/maximum-erasure-value/

class Solution {
    public int maximumUniqueSubarray(int[] nums) {
        int ans = 0, winsum = 0, end = 0, st = -1;
        Map<Integer, Integer> map = new HashMap<>();
        while (end < nums.length) {
            winsum += nums[end];
            if (map.containsKey(nums[end])) {
                if (st < map.get(nums[end])) {
                    while (map.get(nums[end]) != st) {
                        st++;
                        winsum -= nums[st];
                    }
                }
            }
            map.put(nums[end], end);
            end++;

            ans = Math.max(ans, winsum);
        }
        return ans;
    }
}
// https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

// Sol1 - Space (O(n)), Time (O(n))

class Solution {
    public int minOperations(int[] nums, int x) {
        int target = -x;
        for (int i : nums)
            target += i;
        if (target == 0)
            return nums.length;
        Map<Integer, Integer> map = new HashMap<>();
        map.put(0, -1);
        int result = -1, sum = 0;

        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
            if (map.containsKey(sum - target)) {
                result = Math.max(result, i - map.get(sum - target));
            }
            map.put(sum, i);
        }

        return result == -1 ? -1 : nums.length - result;
    }
}

// Sol2 Space (O(1)), Time (O(n))

class Solution {
    public int minOperations(int[] nums, int x) {
        int target = -x;
        for (int i : nums)
            target += i;
        if (target == 0)
            return nums.length;
        if (target < 0)
            return -1;
        int sum = 0, left = 0, result = -1;

        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
            while (sum > target) {
                sum -= nums[left++];
            }
            if (sum == target) {
                result = Math.max(result, i - left + 1);
            }
        }

        return result == -1 ? -1 : nums.length - result;
    }
}
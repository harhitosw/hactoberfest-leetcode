// 167. Two Sum II - Input Array Is Sorted

// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/submissions/

class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int left = 0, right = numbers.length - 1;

        while (numbers[left] + numbers[right] != target) {
            if (numbers[left] + numbers[right] < target)
                left++;
            else
                right--;
        }
        return new int[] { left + 1, right + 1 };
    }
}
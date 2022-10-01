// Two Sum problem from Leetcode

// https://leetcode.com/problems/two-sum/

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
 const twoSum = function(nums, target) {
    const map = new Map();

    for (let i = 0; i < nums.length; i++) {
        const difference = target - nums[i];

        if (map.has(difference)) return [nums.indexOf(difference), i];

        map.set(nums[i], nums[i]);
    }

    return [-1, -1];
};
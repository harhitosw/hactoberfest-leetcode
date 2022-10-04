package Go

// Two Sum problem from Leetcode

// https://leetcode.com/problems/two-sum/

func twoSum(nums []int, target int) []int {
	history := map[int]int{}
	result := []int{}

	for i, n := range nums {

		temp := target - n

		if j, ok := history[temp]; ok {
			result = append(result, j)
			result = append(result, i)

			return result
		}

		history[n] = i
	}

	return result
}

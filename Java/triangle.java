// https://leetcode.com/problems/triangle/

class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        int[] dp = new int[triangle.size() + 1];

        for (int i = triangle.size() - 1; i >= 0; i--) {
            // System.out.println(triangle.get(i));
            for (int j = 0; j < triangle.get(i).size(); j++) {
                // System.out.println(j+" "+triangle.get(i).get(j));
                dp[j] = triangle.get(i).get(j) + Math.min(dp[j], dp[j + 1]);
            }
        }

        return dp[0];
    }
}
# https://leetcode.com/problems/unique-binary-search-trees/

class Solution:
    def numTrees(self, n: int) -> int:
	    if n==0 or n==1:
	        return 1
	    dp = [0]*20
	    dp[0] = dp[1] = 1
	    for i in range(2,n+1):
	        for j in range(i):
	            dp[i] += dp[abs(i-1-j)]*dp[j]
	    return dp[n]

# Top-down DP (Memoization)
# Implementation with a 2-D array (i as row & j as column)

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        M = len(word1)
        N = len(word2)
        dp = [[float('inf') for j in range(N)] for i in range(M)]
        
        def recursion(i, j):
            if i == M and j == N:
                return 0
            
            if i == M:
                return N - j
            
            if j == N:
                return M - i
            
            if dp[i][j] != float('inf'):
                return dp[i][j]
            
            if word1[i] == word2[j]:
                return recursion(i + 1, j + 1)
            
            replace = recursion(i + 1, j + 1) + 1
            delete = recursion(i + 1, j) + 1
            add = recursion(i, j + 1) + 1
            dp[i][j] = min(replace, delete, add)
            
            return dp[i][j]
        
        return recursion(0, 0)
class Solution:
	def numDecodings(self, s: str) -> int:
		if s[0] == "0": return 0
		if len(s) == 1: return 1

		i = 2
		if int(s[0]+s[1]) <= 26: 
			if s[1] == "0": 
				i = 3
				result = 1
				prev1, prev2 = 1, 1 # prev1 = dp[i-1], prev2 = dp[i-2]
			else:
				result = 2
				prev1, prev2 = 2, 1 # prev1 = dp[i-1], prev2 = dp[i-2]
		else: 
			if s[1] == "0": return 0
			result = 1
			prev1, prev2 = 1, 1 # prev1 = dp[i-1], prev2 = dp[i-2]

		while i < len(s):
			if s[i] == "0": 
				if s[i-1] == "0": return 0
				if int(s[i-1] + s[i]) <= 26:
					result = prev2
					prev2 = result
					prev1 = result
					i+=2
				else: return 0
				continue

			if s[i-1] == "0": return 0
			if int(s[i-1] + s[i]) <= 26:
				result = prev1 + prev2
				prev2 = prev1
				prev1 = result

			else:
				prev2 = prev1
				prev1 = result

			i+=1

		return result if s[-1] + s[-2] != "00" else 0

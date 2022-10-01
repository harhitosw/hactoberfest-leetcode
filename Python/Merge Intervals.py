# Merge Intervals

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
# and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

intervals = [[1,3],[2,6],[8,10],[15,18]]

def f(x):                                       # Custom Sort Function
    return x[0]
intervals = sorted (intervals, key = f)

output = []
curr = intervals[0]

for i in range (1, len(intervals)):
    interval = intervals[i]
    if (curr[1] < interval[0]):             # if CASE was [[1,2], [3,4]], 
        output.append(curr)                 # then it would directly append [1,2] to the empty array
        curr = interval                     # replacing curr with the next value in sequence
    else:
        curr = [curr[0], max(curr[1], interval[1])]
        
        
output.append(curr)
    
print(output)
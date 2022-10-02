# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            nm = (-1)*x
            nm = str(nm)
            nm = nm[::-1]
            nm = int('-'+nm)
            if nm > -2**31:
                return nm
            return 0
        else:
            nm = str(x)
            nm = nm[::-1]
            nm = int(nm)
            if nm < 2**31-1:
                return nm
            return 0
# https://leetcode.com/problems/asteroid-collision/

class Solution:
    def asteroidCollision(self, lis: List[int]) -> List[int]:
        n = len(lis)
        st = []
        i=0
        while i<n:
            if len(st)==0 or st[-1]*lis[i] > 0 or (st[-1]<0 and lis[i]>0):
                st.append(lis[i])
            elif abs(lis[i])==st[-1]:
                st.pop()
            elif abs(lis[i])>st[-1]:
                st.pop()
                continue
                        
            i+=1
        return st
//https://leetcode.com/problems/trapping-rain-water/
class Solution {
public:
    int trap(vector<int>& height) {
        int n=height.size(),ans=0;
        // the problem can solved by precomputing the left and the right maximum anb subtracting from that the current bar 
        vector<int>left(n,0),right(n,0);
        for(int i=1;i<n;++i){
            left[i]=max(left[i-1],height[i-1]);   
        }
        for(int i=n-2;i>=0;--i) {
            right[i]=max(right[i+1],height[i+1]);
        }
        for(int i=1;i<n-1;++i)
        {
            ans+=max(0,min(left[i],right[i])-height[i]);
            
        }
         return ans;
    }
};
// https://leetcode.com/problems/pascals-triangle/
class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>>gen(numRows);
        for(int i=0;  i< numRows; i++){
        if(numRows == 1 || i ==0){
            gen[i].push_back(1);
        }
        else if(i == 1 || numRows == 2){
            gen[i].push_back(1);gen[i].push_back(1);

        }
        else if(i>1){
            vector<int>temp(i+1, 1);
                for(int j=0; j<i-1; j++)
                    temp[j+1] = gen[i-1][j]+gen[i-1][j+1];
                gen[i] = temp;

            }
        };
    
        return gen;
    }
};
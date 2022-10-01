import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class merge_intervals {
    
    class Solution {
        public int[][] merge(int[][] intervals) {
            
            if(intervals.length <= 1)
                return intervals;
            
            Arrays.sort(intervals, (arr1, arr2) -> arr1[0] - arr2[0]);
            
            List<int[]> output_arr = new ArrayList();
            
            int[] current_interval = intervals[0];
            output_arr.add(current_interval);
            
            for(int[] intrvl : intervals) {
                int current_begin = current_interval[0];
                int current_end = current_interval[1];
                int next_begin = intrvl[0];
                int next_end = intrvl[1];
                
                if(current_end >= next_begin) {
                    current_interval[1] = Math.max(current_end, next_end);
                }
                else {
                    current_interval = intrvl;
                    output_arr.add(current_interval);
                }
            }
            
            return output_arr.toArray(new int[output_arr.size()][]);
            
        }
    }

}

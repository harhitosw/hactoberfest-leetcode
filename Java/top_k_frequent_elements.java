// https://leetcode.com/problems/top-k-frequent-elements/

import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

class top_k_frequent_elements {
    public int[] topKFrequent(int[] nums, int k) {
        
        //counting the number of occurences of each number
        Map<Integer, Integer> count = new HashMap<>();
        for(int n : nums)
            count.put(n, count.getOrDefault(n, 0) + 1);
        
        //max heap
        PriorityQueue<int[]> priorityQueue = new PriorityQueue<>((a, b) -> b[1] - a[1]);
        for(int key : count.keySet())
            priorityQueue.add(new int[]{key, count.get(key)});
        
        //take the largest k elements in the heap
        int[] res = new int[k];
        for(int i = 0; i < k; i++)
            res[i] = priorityQueue.poll()[0];
        
        return res;
        
    }
}
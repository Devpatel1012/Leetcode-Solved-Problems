from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])

        merged_intervals = []
        
        current_merged_interval = intervals[0] 

        for i in range(1, len(intervals)):
            next_interval = intervals[i] 
            if current_merged_interval[1] >= next_interval[0]:

                current_merged_interval[1] = max(current_merged_interval[1], next_interval[1])
            else:
                merged_intervals.append(current_merged_interval)
                current_merged_interval = next_interval 
        merged_intervals.append(current_merged_interval)
        
        return merged_intervals
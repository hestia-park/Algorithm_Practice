class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        merged= [intervals[0]]

        for start,end in intervals[1:]:
            last_end=merged[-1][1]
            if start <= last_end: #overlap
                merged[-1][1]=max(end,last_end)
            else:
                merged.append([start,end])
        return merged
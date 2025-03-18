class Solution:
    def findMinArrowShots(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        last_end=intervals[0][1]
        cnt=1
        for start,end in intervals[1:]:
            
            if start > last_end: #overlap
                last_end=end
                cnt+=1
            
        return cnt
         
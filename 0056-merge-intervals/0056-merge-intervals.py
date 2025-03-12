# def half_merge(interval: List[List[int]]) -> List[List[int]]:
#     if not interval:
#         return []
    
#     interval.sort(key=lambda x: x[0])  # 시작점을 기준으로 정렬
#     ans = [interval[0]]
    
#     for i in range(1, len(interval)):
#         last_start, last_end = ans[-1]
#         curr_start, curr_end = interval[i]
        
#         if curr_start <= last_end:
#             ans[-1][0] = min(last_start, curr_start)
#             ans[-1][1] = max(last_end, curr_end)
#         else:
#             ans.append(interval[i])
    
#     return ans

# class Solution:
#     def merge(self, interval: List[List[int]]) -> List[List[int]]:
#         if len(interval) < 3:
#             return half_merge(interval)
        
#         ans = interval
#         pivot = len(ans) // 2
        
#         while True:
#             a = half_merge(ans[:pivot])
#             b = half_merge(ans[pivot:])
#             merged = half_merge(a + b)
            
#             if merged == ans:
#                 break  # 변경이 없으면 종료
            
#             ans = merged
#             pivot = len(ans) // 2
        
#         return ans
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        # Step 1: 시작점을 기준으로 정렬
        intervals.sort()

        merged = [intervals[0]]

        # Step 2: 병합 진행
        for start, end in intervals[1:]:
            last_end = merged[-1][1]

            if start <= last_end:  # 겹치는 경우
                merged[-1][1] = max(last_end, end)  # 끝점을 더 큰 값으로 갱신
            else:
                merged.append([start, end])  # 겹치지 않으면 새로운 구간 추가

        return merged
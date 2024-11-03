class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m, n = len(moveTime) - 1, len(moveTime[0]) - 1
        heap = [(0, 0, 0)]
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visited = set()
        while heap:
            time, r, c = heapq.heappop(heap)
            if (r, c) == (m, n): return time
            for x, y in directions:
                row, col = x + r, y + c
                if row <= m and col <= n and col >= 0 and row >= 0 and (row, col) not in visited:
                    heapq.heappush(heap, (max(time, moveTime[row][col]) + 1, row, col))
                    visited.add((row, col))
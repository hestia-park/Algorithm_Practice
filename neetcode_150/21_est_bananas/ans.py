class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinish(piles, k, h):
            hours = 0
            for pile in piles:
                hours += -(-pile // k)  # Equivalent to math.ceil(pile / k)
            return hours <= h
        
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            if canFinish(piles, mid, h):
                right = mid
            else:
                left = mid + 1
        
        return left

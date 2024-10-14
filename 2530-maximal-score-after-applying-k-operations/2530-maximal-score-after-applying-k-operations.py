class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        # score=0
        # for i in range(k):
        #     max_i=nums.index(max(nums))
        #     score+=nums[max_i]
        #     nums[max_i]=ceil(nums[max_i] / 3)
        # return score
        max_heap = [-x for x in nums]
        heapq.heapify(max_heap)
        
        score = 0
        for i in range(k):
            max_i= -heapq.heappop(max_heap)
            score+=max_i
            heapq.heappush(max_heap, -math.ceil(max_i / 3))
        return score

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hit=[0]*(len(nums)+1)
        # print(hit)
        for i in nums:
            hit[i] +=1 
        return hit.index(max(hit))
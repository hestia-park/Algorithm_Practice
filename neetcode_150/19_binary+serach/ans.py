class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            pvot = left + (right - left) // 2  
            if nums[pvot] == target:
                return pvot
            elif nums[pvot] < target:
                left = pvot + 1  
            else:
                right = pvot - 1  
        
        return -1

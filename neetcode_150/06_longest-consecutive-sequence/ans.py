class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:       
        # optima
        # if not nums:
        #     return 0
        
        # nums_set = set(nums)
        # max_length = 0
        
        # for num in nums_set:
        #     if num - 1 not in nums_set:
        #         current_num = num
        #         current_length = 1
                
        #         while current_num + 1 in nums_set:
        #             current_num += 1
        #             current_length += 1
                
        #         max_length = max(max_length, current_length)
        
        # return max_length
        nums = list(sorted(set(nums)))  
        if len(nums) < 2:
            return len(nums)
        
        cnt = 1
        max_len = 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:  
                cnt += 1
            else:
                max_len = max(max_len, cnt)
                cnt = 1
        
        return max(max_len, cnt)

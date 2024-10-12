class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hit_array=[]
        i=0
        while i <len(nums):
            if nums[i] in hit_array:
                nums.pop(i)
            else:
                hit_array.append(nums[i])
                i+=1
        return len(nums)
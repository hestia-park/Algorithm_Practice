class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # first method it took 153 ms, bests 14%
        # using "sorted" array feastures, the algrithms can be more effienct.
        # hit_array=[]
        # i=0
        # while i <len(nums):
        #     if nums[i] in hit_array:
        #         nums.pop(i)
        #     else:
        #         hit_array.append(nums[i])
        #         i+=1
        # return len(nums)
        # second method it took 80ms, best 30% 
        # i guess the reason is for loop.
        # s = set(nums)
        # nums.clear()
        # for i in s:
        #     nums.append(i)
        # nums.sort()
        # return len(nums)
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j
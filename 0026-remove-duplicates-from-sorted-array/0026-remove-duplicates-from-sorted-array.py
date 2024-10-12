class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # First method took 153 ms, best is 14%. O(n^3)
        # Using "sorted" array features, the algorithms can be more efficient.
        # If the array is sorted, the previous value must be smaller than the next one.

        # hit_array=[]
        # i=0
        # while i <len(nums):
        #     if nums[i] in hit_array:
        #         nums.pop(i)
        #     else:
        #         hit_array.append(nums[i])
        #         i+=1
        # return len(nums)
        # second method it took 80ms, best 30% .  O(n log n) time
        # i guess the reason is for loop.
        # s = set(nums)
        # nums.clear()
        # for i in s:
        #     nums.append(i)
        # nums.sort()
        # return len(nums)
        # the last code is O(n) time
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j
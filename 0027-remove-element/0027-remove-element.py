class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # first code
        # it will take a O(n^2) because of pop()
        i=0
        while i <len(nums) :
            if nums[i]==val:
                nums.pop(i)
            else:
                i+=1
        return len(nums)

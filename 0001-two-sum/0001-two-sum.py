class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable = {}
        for i in range(len(nums)):
            if nums[i] in hashTable:
                return [hashTable[nums[i]], i]
            hashTable[target - nums[i]] = i
        return [-1, -1]
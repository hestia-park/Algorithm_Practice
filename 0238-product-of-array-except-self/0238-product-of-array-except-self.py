class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [1] * length

        # Calculate prefix products
        prefix = 1
        for i in range(length):
            answer[i] = prefix
            prefix *= nums[i]

        # Calculate suffix products and multiply with prefix products
        suffix = 1
        for i in range(length - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer

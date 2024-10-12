class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #165 ms,Beats 34.86%
        # but it use memory space o(n)
        # print(len(nums))
        # k=k%len(nums)
        # j=k-1
        # output=nums.copy()
        # for i in range(k):
        #     nums[j-i]=output[len(nums)-1-i]
        #     # print(i,j-i,nums,output)
        #     # j+=1
        # for i in range(k,len(nums)):
        #     # print(i,i-j,nums,output)
        #     nums[i]=output[i-j-1]
        # it don't use additinal space
        k = k % len(nums)
        def reverse(l, r, nums):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l + 1, r - 1

        reverse(0, len(nums) - 1, nums)
        reverse(0, k - 1, nums)
        reverse(k, len(nums) - 1, nums)


        
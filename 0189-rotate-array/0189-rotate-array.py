class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # print(len(nums))
        k=k%len(nums)
        j=k-1
        output=nums.copy()
        for i in range(k):
            nums[j-i]=output[len(nums)-1-i]
            # print(i,j-i,nums,output)
            # j+=1
        for i in range(k,len(nums)):
            # print(i,i-j,nums,output)
            nums[i]=output[i-j-1]


        
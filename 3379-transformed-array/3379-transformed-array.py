class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        re=[0] * len(nums)
        N=len(nums)
        for i in range(N):
            if nums[i] > 0:
                idx=i+(nums[i]%N)
                
            elif nums[i]<0:
                idx=i+(nums[i]%N)
            else:
                idx=i
            if idx >= N:
                idx=idx%(N)
            if idx < 0:
                idx=(idx+N)

            print(nums[i],i,idx)
            re[i]=nums[idx]
        return re
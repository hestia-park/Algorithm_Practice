class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums)<1:
            return nums
        if len(nums)<2:
            return [str(nums[0])]
        ans=[]
        st=0
        for j in range(1,len(nums)):
            if (j-st)!=abs(nums[j]-nums[st] ):
                if abs(j-st)==1:

                    ans.append(str(nums[j-1]))
                    st=j
                else:

                    ans.append(str(nums[st])+"->"+str(nums[j-1]))

                    st=j
        if st==j:
            ans.append(str(nums[st]))
        else:
            ans.append(str(nums[st])+"->"+str(nums[j]))

        return ans

            


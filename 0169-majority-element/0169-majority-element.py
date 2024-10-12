class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hit={}
        # print(hit)
        for i in nums:
            if not i in hit:
                hit[i]=1
            else:
                hit[i]+=1

        return max(hit, key=hit.get)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # #o(n)
        # hit={}
        # # print(hit)
        # for i in nums:
        #     if not i in hit:
        #         hit[i]=1
        #     else:
        #         hit[i]+=1

        # return max(hit, key=hit.get)
        hit = {}
        for i in nums:
            hit[i] = hit.get(i, 0) + 1

        return max(hit, key=hit.get)
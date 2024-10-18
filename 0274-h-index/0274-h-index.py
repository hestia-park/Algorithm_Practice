class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if len(citations)==1:
            if citations[0]==0:
                return 0
            return 1

        citations=sorted(citations,reverse=True)

        ans=0
        while ans < citations[ans] :
            ans+=1
            if ans > len(citations)-1:
                break
        return ans
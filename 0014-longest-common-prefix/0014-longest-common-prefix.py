class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lens=[len(i) for i in strs]
        min_len=min(lens)
        ans=[]
        idx=-1
        for i in range(min_len):
            sets=set([c[i] for c in strs])
            if len(sets)==1 and idx==i-1:
                ans.append(strs[0][i])
                idx=i
            
        return "".join(ans)
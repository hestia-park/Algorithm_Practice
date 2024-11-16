class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        for i in set(s):
            count[i]=0
        max_=0
        left=0
        max_len=0
        for i in range(len(s)):
            count[s[i]] +=1
            max_=max(max_,count[s[i]])
            if (i -left+1) - max_ >k:
                count[s[i]]-=1
                left+=1
            max_len=max(max_len,(i -left+1))
        return max_len

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) ==0:
            return True
        j=0
        if len(s) > len(t):
            return False
        
        cnt=0
        for i in range(len(t)):

           if t[i]==s[j]:
            j+=1
            cnt+=1
            if j > len(s)-1:
                break
        # print(cnt, len(s))
        if cnt==len(s):
            return True
        else:
            return False



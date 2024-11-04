class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1st, tc: o(nlogn) sc O(n)
        # if len(s) != len(t):
        #     return False
        # s=sorted(list(s))
        # t=sorted(list(t))
        # for i in range(len(s)):
        #     if s[i]!=t[i]:
        #         return False
        # return True
        #2nd  O(n), o(1)
        if len(s) != len(t):
            return False
        
        return Counter(s) == Counter(t)

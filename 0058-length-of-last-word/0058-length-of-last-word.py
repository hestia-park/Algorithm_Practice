class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # lists=s.sstrip().split(" ")
        return len(s.strip().split(" ")[-1])
        
class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = "".join(c for c in s if c.isalnum()).lower()
        return n==n[::-1]

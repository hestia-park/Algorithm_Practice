class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_count = Counter(ransomNote)
        magazine_count = Counter(magazine)

        # Check if each character in ransomNote can be satisfied by magazine
        for char, count in ransom_count.items():
            if magazine_count[char] < count:
                return False

        return True
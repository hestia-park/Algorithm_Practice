class Solution:
    def reverseWords(self, s: str) -> str:
        works = re.sub(' +', ' ', s.strip())  # 연속된 공백을 하나의 공백으로 줄임
        works = works.split(" ")[::-1]
        return " ".join(works)

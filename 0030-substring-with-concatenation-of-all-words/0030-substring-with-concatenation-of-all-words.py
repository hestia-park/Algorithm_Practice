class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words or not s:
            return []
        
        word_length = len(words[0])
        total_length = word_length * len(words)
        word_count = Counter(words)
        
        results = []
        
        # 주어진 문자열 s에서 가능한 모든 시작점에 대해 확인
        for i in range(word_length):
            left = i
            right = i
            current_count = Counter()
            
            # 슬라이딩 윈도우를 오른쪽으로 이동
            while right + word_length <= len(s):
                word = s[right:right + word_length]
                right += word_length
                if word in word_count:
                    current_count[word] += 1
                    
                    # 해당 단어의 수가 너무 많아지면, 왼쪽 포인터를 조정
                    while current_count[word] > word_count[word]:
                        left_word = s[left:left + word_length]
                        current_count[left_word] -= 1
                        left += word_length
                    
                    # 윈도우 크기가 모든 단어를 포함하는 크기와 같아지면 결과에 추가
                    if right - left == total_length:
                        results.append(left)
                else:
                    # 현재 단어가 words 배열에 없으면, 윈도우 초기화
                    current_count = Counter()
                    left = right
        
        return results
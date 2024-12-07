class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        # t 문자열의 각 문자의 빈도를 사전 형태로 저장
        dict_t = Counter(t)
        
        # 필요한 문자의 개수
        required = len(dict_t)
        
        # 필터링된 s 문자열의 인덱스와 해당 문자를 리스트에 저장
        filtered_s = [(i, char) for i, char in enumerate(s) if char in dict_t]
        
        l, r = 0, 0
        formed = 0
        window_counts = {}
        
        # (윈도우 길이, 왼쪽, 오른쪽)
        ans = float("inf"), None, None
        
        # 슬라이딩 윈도우 시작
        while r < len(filtered_s):
            character = filtered_s[r][1]
            window_counts[character] = window_counts.get(character, 0) + 1
            
            if window_counts[character] == dict_t[character]:
                formed += 1
                
            # 윈도우를 줄일 수 있는 경우
            while l <= r and formed == required:
                character = filtered_s[l][1]
                
                # 현재 찾은 윈도우가 이전 윈도우보다 작은 경우 갱신
                end = filtered_s[r][0]
                start = filtered_s[l][0]
                if end - start + 1 < ans[0]:
                    ans = (end - start + 1, start, end)
                    
                window_counts[character] -= 1
                if window_counts[character] < dict_t[character]:
                    formed -= 1
                    
                l += 1    
            
            r += 1

        return "" if ans[1] is None else s[ans[1]: ans[2] + 1]
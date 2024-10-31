class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans=[[[],0]]
        i=0
        print(maxWidth)
        for word in words:
            if ans[i][1]+len(word) + len(ans[i][0]) <= maxWidth:
                ans[i][0].extend([word])
                ans[i][1]+=len(word)
            else:
                i+=1
                ans.append([[word],len(word)])
        result = []
        for line, length in ans[:-1]:  # 마지막 줄 제외
            if len(line) == 1:  # 단어가 한 개일 때
                result.append(line[0].ljust(maxWidth))
            else:
                total_spaces = maxWidth - length
                spaces_between_words = total_spaces // (len(line) - 1)
                extra_spaces = total_spaces % (len(line) - 1)
                
                justified_line = ""
                for j in range(len(line) - 1):
                    justified_line += line[j]
                    justified_line += ' ' * (spaces_between_words + (1 if j < extra_spaces else 0))
                justified_line += line[-1]
                result.append(justified_line)

        # 마지막 줄은 왼쪽 정렬
        last_line = ' '.join(ans[-1][0])
        result.append(last_line.ljust(maxWidth))
        
        return result

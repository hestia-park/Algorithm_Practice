class Solution:
    def isValid(self, s: str) -> bool:
        pair_dict = {")": "(", "}": "{", "]": "["}
        stack = []

        for i in s:
            if i in pair_dict:  # 닫는 괄호일 때
                if not stack or pair_dict[i] != stack.pop():  # 스택이 비어있거나 짝이 맞지 않으면 False
                    return False
            else:  # 여는 괄호일 때
                stack.append(i)

        return not stack  # 스택이 비어있으면 True, 아니면 False
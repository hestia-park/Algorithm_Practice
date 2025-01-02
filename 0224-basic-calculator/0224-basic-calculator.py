class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current_number = 0
        current_result = 0
        sign = 1  # 1 for positive, -1 for negative

        for char in s:
            if char.isdigit():  # 숫자인 경우
                current_number = current_number * 10 + int(char)
            elif char == '+':  # 더하기 연산
                current_result += sign * current_number
                current_number = 0
                sign = 1
            elif char == '-':  # 빼기 연산
                current_result += sign * current_number
                current_number = 0
                sign = -1
            elif char == '(':  # 괄호 시작
                # 현재 상태를 스택에 저장
                stack.append(current_result)
                stack.append(sign)
                current_result = 0
                sign = 1
            elif char == ')':  # 괄호 닫힘
                # 괄호 내부 결과를 계산
                current_result += sign * current_number
                current_number = 0
                current_result *= stack.pop()  # 스택에서 sign 꺼내기
                current_result += stack.pop()  # 스택에서 이전 결과 꺼내기

        # 남은 숫자를 결과에 더하기
        current_result += sign * current_number

        return current_result

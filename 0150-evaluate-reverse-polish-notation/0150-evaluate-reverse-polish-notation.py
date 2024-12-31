class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # stack=[]
        # for token in tokens:
        #     if token in "+-*/":
        #         b=int(stack.pop())
        #         a=int(stack.pop())
        #         if token == "+":
        #             stack.append(str(a+b))
        #             # print("+",a+b,a,b)
        #         elif token == "-":
        #             stack.append(str(a-b))
        #             # print("-",a-b,a,b)
        #         elif token == "*":
        #             stack.append(str(a*b))
        #             # print("*",a*b,a,b)
        #         else:
        #             stack.append(str(int(a/b)))
        #             # print("/",a/b,a,b)
        #     else:
        #         stack.append(token)
        # return int(stack.pop())
        stack = []
        # 연산자와 함수 매핑
        operators = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b),  # Python에서 정수 나눗셈
        }

        for token in tokens:
            if token in operators:
                b = stack.pop()
                a = stack.pop()
                # 해당 연산 수행 후 결과를 스택에 추가
                stack.append(operators[token](a, b))
            else:
                # 숫자는 int로 변환하여 스택에 추가
                stack.append(int(token))
        
        # 마지막 결과 반환
        return stack[0]

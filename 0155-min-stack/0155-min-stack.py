class MinStack:
    def __init__(self):
        self.stack = []       # 기본 스택
        self.min_stack = []   # 최소값 스택

    def push(self, val: int) -> None:
        self.stack.append(val)
        # 최소값 스택에 현재 최소값 추가
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        # 스택에서 제거
        if self.stack:
            val = self.stack.pop()
            # 최소값 스택에서도 제거
            if val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        return self.min_stack[-1] if self.min_stack else None

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def backtrack(stack: List[str], current: str, open_count: int, close_count: int):
            if open_count == n and close_count == n:
                result.append(current)
                return
            
            if open_count < n:
                stack.append("(")
                backtrack(stack, current + "(", open_count + 1, close_count)
                stack.pop()
            
            if close_count < open_count:
                stack.append(")")
                backtrack(stack, current + ")", open_count, close_count + 1)
                stack.pop()
        
        backtrack([], "", 0, 0)
        return result

    
        

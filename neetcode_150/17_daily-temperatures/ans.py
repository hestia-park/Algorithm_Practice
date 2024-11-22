class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        result=[0 for i in range(len(temperatures))]
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                idx = stack.pop()
                result[idx] = i - idx
            stack.append(i)
        
        return result


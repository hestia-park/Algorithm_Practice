class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i in "[{(" :
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                d=stack.pop()
                if i == "]" and d =="[":
                    continue
                elif i == "}" and d =="{":
                    continue
                elif i == ")" and d =="(":
                    continue
                else:
                    return False
        return len(stack)==0
                
                    


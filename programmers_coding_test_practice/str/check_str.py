import sys
sys.stdin = open("check_str_input.txt", "r")
for i in range(3):
    info=input()
    in_stack=[]
    out_stack = []
    ans=1
    for j in info:
        if j == "{" or j=="[" or j == "(":
            in_stack.append(j)
        elif j == "}" or j=="]" or j == ")":
            in_=in_stack.pop()
            if  (in_ =="{" and j !="}") :
                ans = 0
                break
            if  (in_ =="[" and j !="]") :
                ans = 0
                break
            if  (in_ =="(" and j !=")"):
                ans=0
                break
    if in_stack:
        ans=0
    print(f"#{t}", ans)

            # out_stack.append(j)
    # if len(in_stack) != len(out_stack):
    #     ans = 0
    # else:
    #     while in_stack:
    #         in_=in_stack.pop()
    #         out_=out_stack.pop()
    #         if  (in_ =="{" and out_ !="}") :
    #             ans = 0
    #             break
    #         if  (in_ =="[" and out_ !="]") :
    #             ans = 0
    #             break
    #         if  (in_ =="(" and out_ !=")"):
    #             ans=0
    #             break
    print(ans)
#1 0
#2 0
#3 1
#4 1
#5 1
#6 0
#7 0
#8 1
#9 0
#10 1
import sys
sys.stdin = open("1218input.txt", "r")
for t in range(10):
    lens_=int(input())
    info=input()
    stack=[]
    ans=0
    for i in info:
        if i in "[{(<":
            stack.append(i)
        else:
            j=stack.pop()
            if j=="[" and i=="]":
                ans=1

            elif j=="(" and i==")":
                ans=1

            elif j=="{" and i=="}":
                ans=1

            elif j=="<" and i==">":
                ans=1

            else:
                break
    if len(stack) >0:
        ans=0
    print(f"#{t+1}", ans)

import sys
sys.stdin = open("remove_repeat.txt", "r")
T=int(input())
#1 1
#2 4
#3 11
for t in range(1,T+1):
    stack=[]
    check=[]
    info=input()
    for i in info:
        stack.append(i)
    i=0

    while True:
        # print(i,stack[i])
        if stack[i] == stack[i+1]:
            del stack[i]
            del stack[i]
            if i==0:
                i=0
            else:
                i-=1
        else:
            i+=1
        if 1 >= len(stack) or i+1>=len(stack):
            break

    print(f"#{t}", len(stack))
import sys
#https://swexpertacademy.com/main/solvingProblem/solvingProblem.do

sys.stdin = open("1233_input.txt", "r")
for test_case in range(1, 11):
    N=int(input())
    ans=1
    for i in range(N):
        info=list(map(str,input().split()))
        if len(info)==4:
            if not (info[1] in ["-","/","*","+"] and info[1] in ["-","/","*","+"] and int(info[3])):
                # print(info,int(info[2]))
                ans=0
    print('#{} {}'.format(test_case, ans))
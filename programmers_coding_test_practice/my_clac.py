

import sys
sys.stdin = open("/done/sample_sample_input_smartphone.txt", "r")
import os
Testcase = int(input())
for i in range(Testcase):
    N,O,M= map(int, input().split())
    touchNum = list(map(int, input().split()))
    operations = list(map(int, input().split()))
    targetNum = int(input())
    targetchar=str(targetNum)
    ans=0
    theotheral=False
    for j in range(len(targetchar)):
        if not int(targetchar[j]) in touchNum:
            # print(targetchar[j]," is not in ",touchNum)
            theotheral=True
            break
        else:
            ans+=1
    if not theotheral:
        print("#",i+1,ans)



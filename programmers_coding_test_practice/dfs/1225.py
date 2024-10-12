#1 6 2 2 9 4 1 3 0
#2 9 7 9 5 4 3 8 0
#3 8 7 1 6 4 3 5 0
#4 7 5 8 4 8 1 3 0
#5 3 8 7 4 4 7 4 0
#6 6 7 5 9 6 8 5 0
#7 7 6 8 3 2 5 6 0
#8 9 2 1 7 3 6 3 0
#9 4 7 8 1 2 8 4 0
#10 6 8 9 5 8 5 2 0
import sys
sys.stdin = open("1225input.txt", "r")
from collections import deque
for ts in range(10):
    ans=0
    length=int(input())
    # info=list(map(str,input().split()))
    info=list(map(int,input().split()))
    while True:
        for j in range(1,6):
            s=info.pop(0)
            if s-j>0:
                info.append(s-j)
            else:
                info.append(0)
                break
        if info[-1]==0:
            break

    ans =list(map(str, info))
    # print(" ".join(ans))
    print("#{} {}".format(ts + 1, " ".join(ans)))
#1 18
#2 96
#3 16
#4 5
#5 99
#6 0
#7 97
#8 0
#9 62
#10 3

import sys
sys.stdin = open("1211.txt", "r")

for t in range(1, 11):
    dumps=int(input())
    bul=[[0 for _ in range(102)] for _ in range(102)]
    x=y=0
    for i in range(1,101):
        bul[i] = list(map(int, input().split()))
        bul[i].insert(0,0)
        bul[i].append(0)
    end=([i for i, value in enumerate(bul[100]) if value == 1])
    ans=0
    # print(end)
    min_arr=[0 for _ in range(len(end))]
    stack=[]
    for j in range(len(end)):
        sx,sy=100,end[j]
        lens=0
        min_x=10000
        x=sx
        y=sy
        while x !=1:
            if bul[x][y-1] == 1 :
                while bul[x][y-1] != 0:
                    lens+=1
                    y-=1
                x-=1
                lens += 1
            elif bul[x][y+1] == 1 :
                while bul[x][y+1] != 0:
                    lens += 1
                    y+=1
                x-=1
                lens += 1
            else:
                lens += 1
                x-=1
        stack.append(y-1)
        # print(y-1)
        min_arr[j]=lens
    # print(end)
    # print(stack,)
    # print(min_arr, min(min_arr))
    # print(min_arr,min(min_arr))

    print("#{} {}".format(t,stack[min_arr.index(min(min_arr))]))
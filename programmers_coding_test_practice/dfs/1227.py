#1 1
#2 1
#3 1
#4 0
#5 0
#6 1
#7 1
#8 0
#9 1
#10 0

import sys
sys.stdin = open("1227input.txt", "r")


def check(x,y):
    global stack_x,stack_y
    if graph[x ][y] != 1 and visi[x][y] == False:
        stack_x.append(x)
        stack_y.append(y)

for _ in range(10):
    stack_x = []
    stack_y = []
    graph = []
    lens=100
    visi = [[False for _ in range(lens)] for _ in range(lens) ]
    ts=input()
    sx=sy=ex=ey=0
    for i in range(lens):
        info=input()
        arr=[int(a) for a in info]
        graph.append(arr)
        if 2 in arr:
            sx=i
            sy=arr.index(2)
        if 3 in arr:
            ex=i
            ey=arr.index(3)
    stack_x=[sx]
    stack_y=[sy]
    ans=0
    while stack_x and stack_y:
        x=stack_x.pop(0)
        y=stack_y.pop(0)
        visi[x][y] = True
        if graph[x][y]==3:
            ans=1
            break

        check(x-1,y)
        check(x+1, y)
        check(x, y - 1)
        check(x, y+1)
    print(ans)


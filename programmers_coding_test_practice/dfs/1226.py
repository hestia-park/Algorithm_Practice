#1 1
#2 1
#3 1
#4 0
#5 1
#6 1
#7 0
#8 1
#9 1
#10 1
import sys
sys.stdin = open("1226input.txt", "r")
lens=16
def check(x,y):
    global stack_x,stack_y
    if miro[x ][y] != 1 and visi[x][y] == False:
        stack_x.append(x)
        stack_y.append(y)
for _ in range(10):
    ans=0
    ts=int(input())
    miro=[]
    sx=sy=ex=ey=0
    for i in range(lens):
        a=input()
        miro.append([int(j) for j in a])
        if 2 in miro[i]:
            sx=i
            sy=miro[i].index(2)
        if 3 in miro[i]:
            ex=i
            ey=miro[i].index(3)
    visi=[[False for _ in range(lens)] for _ in range(lens)]
    # print(visi[sx][sy])
    stack_x=[sx]
    stack_y=[sy]

    while stack_x and stack_y:
        x=stack_x.pop(0)
        y=stack_y.pop(0)
        visi[x][y] = True
        # print(x,y,ex,ey)
        if miro[x][y]==3:
            ans=1
            break
        check(x-1,y)
        check(x+1, y)
        check(x, y - 1)
        check(x, y+1)
        # if miro[x-1][y]!=1 and visi[x-1][y]== False:
        #     stack_x.append(x-1)
        #     stack_y.append(y)
        # if miro[x+1][y]!=1 and visi[x+1][y]== False:
        #     stack_x.append(x+1)
        #     stack_y.append(y)
        # if miro[x][y-1]!=1 and visi[x][y-1]== False:
        #     stack_x.append(x )
        #     stack_y.append(y- 1)
        # if miro[x][y+1]!=1 and visi[x][y+1]== False:
        #     stack_x.append(x)
        #     stack_y.append(y + 1)

    print(ans)



#1 67
#2 45
#3 39
#4 24
#5 91
#6 93
#7 90
#8 4
#9 99
#10 35
import sys
sys.stdin = open("1210input.txt", "r")

for t in range(1, 11):
    dumps=int(input())
    bul=[[0 for _ in range(102)] for _ in range(102)]
    for i in range(1,101):
        bul[i] = list(map(int, input().split()))
        bul[i].insert(0,0)
        bul[i].append(0)
        if 2 in bul[i]:
            x=i
            y=bul[i].index(2)

    while x !=1:
        if bul[x][y-1] == 1 :
            while bul[x][y-1] != 0:
                y-=1
            x-=1
        elif bul[x][y+1] == 1 :
            while bul[x][y+1] != 0:
                y+=1
            x-=1
        else:
            x-=1
    # print(x)

    print("#{} {}".format(t,y-1))
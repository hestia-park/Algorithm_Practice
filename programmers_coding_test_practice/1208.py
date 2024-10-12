#1 13
#2 32
#3 54
#4 25
#5 87
#6 14
#7 39
#8 26
#9 13
#10 29
import sys
sys.stdin = open("1208input.txt", "r")
for t in range(10):
    dumps=int(input())
    bul=list(map(int,input().split()))
    for i in range(dumps):
        max_val=max(bul)
        max_index=bul.index(max_val)
        min_val=min(bul)

        min_index=bul.index(min_val)
        bul[max_index]-=1
        bul[min_index]+=1
    print("#{} {}".format(t,max(bul)-min(bul)))
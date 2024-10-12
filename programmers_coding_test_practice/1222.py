#1 267
#2 197
#3 345
#4 149
#5 149
#6 213
#7 180
#8 221
#9 158
#10 205
import sys
sys.stdin = open("1222input.txt", "r")
for ts in range(10):
    length=int(input())
    info=list(map(int,input().split("+")))
    # print(info)
    print("#{} {}".format(ts+1, sum(info)))

#1 43046721
#2 256
#3 7776
#4 10000000
#5 279936
#6 49
#7 43046721
#8 9
#9 65536
#10 262144
import sys
sys.stdin = open("1217input.txt", "r")
for i in range(10):
    t=input()
    info=list(map(int,input().split()))
    ans=info[0]
    for j in range(1,info[1]):
        ans*=info[0]
    print("#{} {}".format(i+1,ans))
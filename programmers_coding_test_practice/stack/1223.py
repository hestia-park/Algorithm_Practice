#1 28134
#2 195767
#3 4293
#4 1592
#5 477326
#6 45647
#7 102951
#8 6548
#9 1394
#10 4285
import sys
sys.stdin = open("1223input.txt", "r")
for ts in range(10):
    ans=0
    length=int(input())
    info=list(map(str,input()))
    # info=input()
    while len(info) !=1:
        # print("b ",info)
        if "*" in info:
            index=info.index("*")
            a=int(info[index-1])
            b=int(info[index+1])
            c=a*b
            info[index-1:index+2]="F"
            index = info.index("F")
            info[index] = str(c)
        else:
            if "+" in info:
                index=info.index("+")
                a=int(info[index-1])
                b=int(info[index+1])
                c = a + b
                info[index - 1:index + 2] = "F"
                index = info.index("F")
                info[index] = str(c)
        # print("a ", info)
        # break
    # print(cnt)
    print("#{} {}".format(ts+1, info[0]))
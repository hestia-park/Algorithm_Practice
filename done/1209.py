#1 1712
#2 1743
#3 1713
#4 1682
#5 1715
#6 1730
#7 1703
#8 1714
#9 1727
#10 1731
import sys
sys.stdin = open("1209input.txt", "r")
for t in range(1, 11):
    dumps=int(input())
    bul=[[] for _ in range(100)]
    bul_sum_x=[0 for _ in range(100)]
    bul_sum_y = [0 for _ in range(100)]
    bul_sum =  [0,0]
    for i in range(100):
        bul[i] = list(map(int, input().split()))
        bul_sum_x[i]=sum(bul[i])
        for j in range(100):
            bul_sum_y[j]+=bul[i][j]
            if i==j:
                bul_sum[0]+=bul[i][j]
        bul_sum[1]+=bul[i][99-i]

    # print(max(df1))
    print("#{} {}".format(t,max(max(bul_sum_x),max(bul_sum_y),bul_sum[0],bul_sum[1])))
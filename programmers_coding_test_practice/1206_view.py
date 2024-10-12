import sys
sys.stdin = open("view_sample_input.txt", "r")
#1 111
#2 60
#3 165
#4 57
#5 72
#6 68
#7 16
#8 27
#9 691
#10 8757
for t in range(10):
    b_nums=int(input())
    bul=list(map(int,input().split()))
    ans=0
    for i in range(2,b_nums-2):
        # print(i,bul[i],max(bul[i-2:i]),bul[i+1:i+3],bul[i]-(max(max(bul[i-2:i]),max(bul[i+1:i+3]))))

        if bul[i]-(max(max(bul[i-2:i]),max(bul[i+1:i+3])))>0:
            ans+= bul[i]-(max(max(bul[i-2:i]),max(bul[i+1:i+3])))
    print('#{} {}'.format(t+1, ans))
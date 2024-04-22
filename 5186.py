#1 101
#2 overflow
#3 001
import sys
sys.stdin = open("5186sample_input.txt", "r")

T=int(input())
hex_c = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
for test_case in range(1,T+1):
    ans=''
    nam=float(input())
    # print(nam)
    ans=[]
    print(0.125*2)
    con_bit = []
    fi=nam
    while nam%1!=0 or fi==nam:
        if len(con_bit)==1:
            fi=nam

        con_bit.insert(0,str(int(nam*2)))
        if nam*2 >=1:
            nam= abs(nam*2-1)
        else:
            nam*=2
    ans.extend(con_bit)
    if len(ans) >12:
        print('#{} {}'.format(test_case, "overflow"))
    else:
        print('#{} {}'.format(test_case, "".join(ans)))
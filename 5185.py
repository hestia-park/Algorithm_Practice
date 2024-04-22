#1 0100011111111110
#2 01111001111000010010
#3 01000001110110100001011011001101
import sys
sys.stdin = open("5185sample_input.txt", "r")

T=int(input())
hex_c = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
for test_case in range(1,T+1):
    ans=''
    info=list(input().split())
    moc=int(info[0])
    bits=[]
    for i in info[1]:
        if i in hex_c.keys():
            bits.append(hex_c[i])
        else:
            bits.append(int(i))
    # print(bits)
    ans=[]
    for i in bits:
        nam=i
        con_bit = []
        for _ in range(4):
            con_bit.insert(0,str(nam%2))
            nam=nam//2
        ans.extend(con_bit)
    print('#{} {}'.format(test_case, "".join(ans)))
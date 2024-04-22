import sys
sys.stdin = open("5176_tree_input.txt", "r")

#5176. [파이썬 S/W 문제해결 기본] 8일차 - 이진탐색

#1 4 6
#2 5 2
#3 8 14

def maketree(idx):
    global num,tree
    if idx <= N:
        maketree(2*idx)
        tree[idx]=num
        num+=1
        maketree(2*idx+1)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    tree = [0] * (N + 1)

    num = 1
    maketree(1)
    print(f'#{tc} {tree[1]} {tree[N // 2]}')
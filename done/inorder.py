import sys
sys.stdin = open("inorder_input.txt", "r")
N=int(input())
tree = [['',0,0] for _ in range(N + 1)]


def inorder(v):
    global tree
    if tree[v][0] != "":
        inorder(tree[v][1])
        print(tree[v][0],end="")
        inorder(tree[v][2])

for i in range(N):
    info=list(map(str,input().split()))

    if len(info)== 2:
        tree[int(info[0])]=[info[1],0,0]
    elif len(info)== 3:
        tree[int(info[0])] = [info[1], int(info[2]), 0]
    else:
        tree[int(info[0])] = [info[1], int(info[2]), int(info[3])]

inorder(1)


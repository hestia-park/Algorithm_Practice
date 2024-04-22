# 5
# 28
# 24
# 45
# 30
# 60
# 52
# 98
# 50
# 트리를 전위 순회한 결과가 주어진다. 노드에 들어있는 키의 값은 106보다 작은 양의 정수이다. 모든 값은 한 줄에 하나씩 주어지며, 노드의 수는 10,000개 이하이다. 같은 키를 가지는 노드는 없다.
import sys
sys.stdin = open("bts_insert_input.txt", "r")
# node=input()
nodes=[]
for i in range(9):
    # print(node)
    node=input()
    nodes.append(node)
nodes.insert(0,'')
def inorder(v):
    global bts
    if bts[v][0] != "":
        inorder(bts[v][1])
        print(bts[v],end="")
        inorder(bts[v][2])
def maketree(idx):
    global bts,nodes
    if idx <=len(nodes)-1:
        maketree(2*idx)
        bts[idx]=[nodes[idx],2*idx,2*idx+1]

        maketree(2 * idx+1)
num=0
bts=[['',0,0] for _ in range(len(nodes)+1)]
bts[1] = nodes[1]
maketree(1)
inorder(1)
# for i in range(1,len(nodes)):
#     if bts[0][0] < i:
#             if bts[0][1] == False:
#                 bts[0][1]=i
#                 bts[0][1] == True:
#             else:


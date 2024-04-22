import calendar
import sys
sys.stdin = open("1232_input.txt", "r")
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV141J8KAIcCFAYD
# 총 10개의 테스트 케이스가 주어진다. (총 테스트 케이스의 개수는 입력으로 주어지지 않는다)
#
# 각 테스트 케이스의 첫 줄에는 정점의 개수 N(1≤N≤1000)이 주어진다. 그다음 N 줄에 걸쳐 각 정점의 정보가 주어진다.
#
# 정점이 정수면 정점 번호와 양의 정수가 주어지고, 정점이 연산자이면 정점 번호, 연산자, 해당 정점의 왼쪽 자식, 오른쪽 자식의 정점 번호가 차례대로 주어진다.
#
# 정점 번호는 1부터 N까지의 정수로 구분된고 루트 정점의 번호는 항상 1이다.
#
# 위의 예시에서, 숫자 4가 7번 정점에 해당하면 “7 4”으로 주어지고, 연산자 ‘/’가 2번 정점에 해당하면 두 자식이 각각 숫자 9인 4번 정점과 연산자 ‘-’인 5번 정점이므로 “2 / 4 5”로 주어진다.
#1 13
#2 20
#3 35
#4 107
#5 369
#6 76
#7 123
#8 313
#9 238
#10 2

def maketree(idx):
    global num,tree
    if idx<=N:
        maketree(2*idx)
        tree[idx]=num
        num+=1
        maketree(2 * idx+1)

def inorder(node):
    global int_,cal_
    if tree[node] !=0:

        inorder(tree_left[node])
        inorder(tree_right[node])
        if not tree[node] in ["/", "+", "-", "*"]:
            int_.append(int(tree[node]))
        else:
            cal_.append(tree[node])
        # print(tree[node], end=" ")
        node+=1
def recur(v):   # 후위 순회를 이용해 계산
    # print(v, tree[v])
    if not tree[v] in ["/", "+", "-", "*"]:    # 연산자가 아닌 경우
        # print("cale")
        return tree[v]
    else:                               # 연산자인 경우
        a = recur(tree_left[v])
        b = recur(tree_right[v])

        if tree[v] == '+':
            return a + b
        elif tree[v] == '-':
            return a - b
        elif tree[v] == '*':
            return a * b
        elif tree[v] == '/':
            return int(a / b)

for test_case in range(1, 11):
    N=int(input())
    tree=[0]*(N+1)
    tree_left = [0] * (N + 1)
    tree_right = [0] * (N + 1)
    int_=[]
    cal_ = []
    for i in range(N):
        info=list(map(str,input().split()))
        if len(info) == 4 :
            tree[int(info[0])]=info[1]
            tree_left[int(info[0])]=int(info[2])
            tree_right[int(info[0])]=int(info[3])
        else:
            tree[int(info[0])] = int(info[1])

    print(recur(1))

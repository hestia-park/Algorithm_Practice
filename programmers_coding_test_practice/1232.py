import sys

# 1 13
# 2 20
# 3 35
# 4 107
# 5 369
# 6 76
# 7 123
# 8 313
# 9 238
# 10 2

sys.stdin = open("1232_input.txt", "r")

icp={
    "+": 1,
    "-": 1,
    "/": 2,
    "*": 2,
    "(": 3,
    ")":-1
}
def cal(cal,a,b):
    if cal=="+":
        return int(a)+int(b)
    if cal == "-":
        return int(a) - int(b)
    if cal == "/":
        return int(int(a) / int(b))
    if cal == "*":
        return int(a) * int(b)

def order_(v):
    if not graph[v][0] in icp.keys():
        return int(graph[v][0])
    else:
        left = order_(graph[v][1])
        right = order_(graph[v][2])
        return cal(graph[v][0],left,right)

for test_case in range(1, 11):

    N = int(input())
    graph = [["", False, False] for _ in range(N + 1)]
    for i in range(N):
        info = list(map(str, input().split()))
        if len(info) == 4:
            graph[int(info[0])] = [info[1], int(info[2]), int(info[3])]

        # if len(info) == 3:
        #     oper[int(info[0])]=info[1]
        #     nums[int(info[0])]=[int(info[2]), 0]
            # graph[int(info[0])] = [info[1], int(info[2]), False]
        if len(info) == 2:
            graph[int(info[0])] = [info[1], False, False]

    ans=order_(1)
    print('#{} {}'.format(test_case, ans))
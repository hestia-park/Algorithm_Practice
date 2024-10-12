from collections import deque

t = int(input())
visited = [0] * 1000

touchNum = []
numQueue = deque()
visitedNum = []
m = 0


def allNum(cur, addNum):
    if len(str(addNum)) >= 3:
        return
    num = cur * 10 + addNum
    if num > 999 or num < 0:
        return
    if visited[num] < m + 1:
        return
    numQueue.append(num)
    visited[num] = len(str(num))
    visitedNum.append(num)

    for n in touchNum:
        allNum(num, n)


def calc(num1, num2, oper):
    if oper == 1:
        num1 += num2
    elif oper == 2:
        num1 -= num2
    elif oper == 3:
        num1 *= num2
    elif oper == 4:
        if num2 == 0:
            return -1
        num1 //= num2
    if 0 <= num1 < 1000:
        return num1
    else:
        return -1


for i in range(t):
    visitedNum.clear()
    n, o, m = map(int, input().split())
    visited = [m + 1] * 1000
    numQueue = deque()
    touchNum = list(map(int, input().split()))
    operations = list(map(int, input().split()))
    targetNum = int(input())

    for t in touchNum:
        allNum(0, t)

    if visited[targetNum] < m + 1:
        print(f'#{i + 1} {visited[targetNum]}')
        continue
    while numQueue:
        v = numQueue.popleft()

        for num in visitedNum:
            clickCount = visited[v] + len(str(num)) + 1
            if clickCount + 1 > m:
                continue
            for oper in operations:
                nxt = calc(v, num, oper)

                if nxt == -1:
                    continue
                if visited[nxt] <= clickCount:
                    continue
                visited[nxt] = clickCount
                numQueue.append(nxt)

    if 0 < visited[targetNum] < m + 1:
        print(f'#{i + 1} {visited[targetNum] + 1}')
    else:
        print(f'#{i + 1} -1')
def dfs(depth, bt):
    global cpus
    t, l = packets[depth]
    for i in range(cpu_num):
        cpus[i] = max(0, cpus[i] + bt - t)

    key = tuple([depth] + cpus)
    if key in visited:
        return False
    visited.add(key)

    for i in range(cpu_num):
        if cpus[i] + l <= 10:
            origin = list(cpus)
            cpus[i] += l
            if depth == N - 1:
                return True
            else:
                if dfs(depth + 1, t):
                    return True
            cpus = origin
    return False

import sys
sys.stdin = open("input.txt", "r")
for t in range(1, 1 + int(input())):
    N = int(input())
    packets = tuple(tuple(map(int, input().split())) for _ in range(N))
    ans = -1
    for cpu_num in range(1, 6):
        cpus = [0 for _ in range(cpu_num)]
        visited = set()
        if dfs(0, 0):
            ans = cpu_num
            break
    print(f"#{t}", ans)
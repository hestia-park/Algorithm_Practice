T = int(input())
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def dfs(r, c, d, dist):
    global ans
    if (r, c) == (tr, tc):
        ans = min(ans, dist)
        return

    if dist >= ans:
        return

    if 0 <= r < n and 0 <= c < n and arr[r][c]:
        if visted[r][c]:
            return
        if dp[r][c][d] < dist:
            return
        dp[r][c][d] = dist
        visted[r][c] = 1
        if arr[r][c] <= 2:
            dfs(r + dr[d], c + dc[d], d, dist + 1)
        else:
            for nd in [(d + 1) % 4, (d + 3) % 4]:
                dfs(r + dr[nd], c + dc[nd], nd, dist + 1)
        visted[r][c] = 0


for t in range(1, T + 1):
    n = int(int(input()))
    arr = [tuple(map(int, input().split())) for _ in range(n)]
    ans = 10 ** 9  # 10^9
    visted = [[0] * n for _ in range(n)]
    tr, tc = n - 1, n
    dp = [[[10 ** 9] * 4 for _ in range(n)] for _ in range(n)]
    dfs(0, 0, 0, 0)
    dp = [[[10 ** 9] * 4 for _ in range(n)] for _ in range(n)]
    tr, tc = 0, -1
    dfs(n - 1, n - 1, 2, 0)

    print(f'#{t} {ans}')
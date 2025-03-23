class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m, n = len(board), len(board[0])
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1), (1, 0),  (1, 1)]

        for i in range(m):
            for j in range(n):
                live = 0
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < m and 0 <= nj < n and abs(board[ni][nj]) == 1:
                        live += 1

                # 적용 규칙
                if board[i][j] == 1 and (live < 2 or live > 3):
                    board[i][j] = -1  # 죽을 셀
                if board[i][j] == 0 and live == 3:
                    board[i][j] = 2   # 새로 살아날 셀

        # 최종 업데이트
        for i in range(m):
            for j in range(n):
                if board[i][j] > 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0

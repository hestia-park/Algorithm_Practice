class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        first_row_has_zero = any(matrix[0][j] == 0 for j in range(cols))
        first_col_has_zero = any(matrix[i][0] == 0 for i in range(rows))

        # 1. 마킹: 첫 행과 첫 열을 사용해서 0이 있는 위치 표시
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # 2. 마킹된 행/열을 기준으로 나머지 셀 0으로 설정
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # 3. 첫 번째 행 처리
        if first_row_has_zero:
            for j in range(cols):
                matrix[0][j] = 0

        # 4. 첫 번째 열 처리
        if first_col_has_zero:
            for i in range(rows):
                matrix[i][0] = 0

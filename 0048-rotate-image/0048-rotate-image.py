class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        copy_array= [row[:] for row in matrix]
        N=len(matrix[0])
        for i in range(N):
            for j in range(N):
                idx_i=j
                idx_j=N-1-i
                # print(i,j,idx_i,idx_j)
                matrix[idx_i][idx_j]=copy_array[i][j]
        print(matrix)

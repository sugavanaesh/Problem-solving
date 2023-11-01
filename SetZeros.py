class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        r = len(matrix)
        c = len(matrix[0])
        res = []
        for i in range(0,r):
            for j in range(0,c):
                if matrix[i][j]==0:
                    res.append([i,j])

        for a,b in res:
            for row in range(c):
                matrix[a][row]=0
            for col in range(r):
                matrix[col][b]=0    
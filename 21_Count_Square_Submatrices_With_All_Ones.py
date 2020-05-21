class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        total = 0
        dp = [[0 for i in range(n)] for j in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    if matrix[i][j] == 1:
                        dp[i][j] = matrix[i][j]
                else:
                    if matrix[i][j] == 1:
                        dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
                total += dp[i][j]
        
        return total
class Solution:
  def minCost(self, grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])
    # dp[r][c] stores a set of all possible XOR path values to cell (r, c)
    dp = [[set() for _ in range(n)] for _ in range(m)]

    dp[0][0].add(grid[0][0])

    for r in range(m):
      for c in range(n):
        for val in dp[r][c]:
          # Move right
          if c + 1 < n:
            dp[r][c + 1].add(val ^ grid[r][c + 1])
          # Move down
          if r + 1 < m:
            dp[r + 1][c].add(val ^ grid[r + 1][c])

    return min(dp[m - 1][n - 1])

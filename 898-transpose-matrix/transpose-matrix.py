# class Solution:
#   def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
#     rows, cols = len(matrix), len(matrix[0])
#     # Create a new matrix with dimensions (cols x rows)
#     transposed = [[0] * rows for _ in range(cols)]

#     for r in range(rows):
#       for c in range(cols):
#         transposed[c][r] = matrix[r][c]

#     return transposed
class Solution:
    def transpose(self, matrix):
        return [list(row) for row in zip(*matrix)]

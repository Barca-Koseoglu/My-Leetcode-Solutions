class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        matrix = ['']*numRows
        curr_row = 0
        down = False

        for i in s:
            matrix[curr_row] += i
            if curr_row == 0 or curr_row == numRows-1:
                down = not down
            if down:
                curr_row += 1
            else:
                curr_row -= 1

        return ''.join(matrix)
  

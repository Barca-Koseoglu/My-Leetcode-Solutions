class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [[0,0,0],[0,0,0],[0,0,0]]
        num_moves = 0
        for i, j in moves:
            num_moves += 1
            if num_moves%2 == 1:
                board[i][j] = 1
            else:
                board[i][j] = -1
        
        if board[0][0] == board[1][1] == board[2][2]:
            if board[0][0] == 1:
                return "A"
            elif board[0][0] == -1:
                return "B"
        if board[2][0] == board[1][1] == board[0][2]:
            if board[2][0] == 1:
                return "A"
            elif board[2][0] == -1:
                return "B"
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2]:
                if board[i][0] == 1:
                    return "A"
                elif board[i][0] == -1:
                    return "B"
            if board[0][i] == board[1][i] == board[2][i]:
                if board[0][i] == 1:
                    return "A"
                elif board[0][i] == -1:
                    return "B"
        if num_moves == 9:
            return "Draw"
        return "Pending"
        

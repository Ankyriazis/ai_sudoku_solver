class SudokuSolver:
    def __init__(self, board):
        self.board = board

    def is_valid(self, row, col, num):
        for i in range(9):
            if self.board[row][i] == num or self.board[i][col] == num:
                return False

        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.board[start_row + i][start_col + j] == num:
                    return False

        return True

    def solve(self):
        empty = self.find_empty()
        if not empty:
            return True
        row, col = empty

        for num in range(1, 10):
            if self.is_valid(row, col, num):
                self.board[row][col] = num

                if self.solve():
                    return True

                self.board[row][col] = 0

        return False

    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return (i, j)
        return None

    def get_board(self):
        return self.board
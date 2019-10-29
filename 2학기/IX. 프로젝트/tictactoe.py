class TicTacToe:
    def __init__(self):
        self.board = [".", ".", ".", ".", ".", ".", ".", ".", "."]
        self.current_turn = "O"

    def set(self, row, col):
        if self.get(row, col) == ".": #버튼이 빈칸일 때
        #if self.current_turn == "O":
        #    self.current_turn = "X"
        #else:
        #    self.current_turn = "O"
        self.current_turn = "X" if self.current_turn == "O" else "O"
        self.board[(row * 3) + col] = self.current_turn

    def get(self, row, col):
        return self.board[(row * 3) + col]

    def check_winner(self):
        check = self.current_turn
        #-
        if self.get(0, 0) == self.get(0, 1) == self.get(0, 2) == check:
            return check
        if self.get(1, 0) == self.get(1, 1) == self.get(1, 2) == check:
            return check
        if self.get(2, 0) == self.get(2, 1) == self.get(2, 2) == check:
            return check

        #-
        if self.get(0, 0) == self.get(1, 0) == self.get(2, 0) = check:






        #\
        if self.get(0, 0) == self.get(1, 1) == self.get(2, 2) == check:
            return check
        #/
        if self.get(0, 2) == self.get(1, 1) == self.get(2, 0) == check:
            return check

        #무승부
        if not "." in self.board:
            return "d"

    def __str__(self):
        s = ""
        for i, ch in self.board:
            s += ch
            if i % 3 == 2:
                s += "\n"
        return s


if __name__ == '__main__':
    ttt = TicTacToe()
    print(ttt)
    ttt.set(0, 0)
    ttt.set(0, 1)
    ttt.set(1, 1)
    print(ttt)
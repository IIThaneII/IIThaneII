class TicTacToe:

    def __init__(self):
        self.board = []

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('⬜️')
            self.board.append(row)

    def x_input(self):
        self.a = input("X enter row and column: ")
        x = self.a.split(" ")
        while self.board[int(x[0])-1][int(x[1])-1] != "⬜️":
            self.a = input("Enter blank row and column: ")
            x = self.a.split(" ")
        self.board[int(x[0])-1][int(x[1])-1] = ' X'
        
    def o_input(self):
        self.a = input("O enter row and column: ")
        x = self.a.split(" ")
        while self.board[int(x[0])-1][int(x[1])-1] != "⬜️":
            self.a = input("Enter blank row and column: ")
            x = self.a.split(" ")
        self.board[int(x[0])-1][int(x[1])-1] = ' O'

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == "⬜️":
                    return False
        return True

    def is_player_win(self):
        for row in self.board:
            if row[0] == row[1] and row[0] == row[2]:
                return row[0]
            for i in range(0, 3):
                if self.board[0][i] == self.board[1][i] and self.board[0][i] == self.board[2][i]:
                    return self.board[0][i]
        if self.board[0][0] == self.board[1][1] and self.board[0][0] == self.board[2][2]:
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] and self.board[0][2] == self.board[2][0]:
            return self.board[2][0]

    def game_is_on(self):
        self.create_board()
        while 1:
            print("Player X turn")
            self.x_input()
            if self.is_player_win() == " X":
                print(f"Player X win!")
                self.show_board()
                break
            self.show_board()
            if self.is_board_filled():
                print("It's a draw!")
                break
            print("Player O turn")
            self.o_input()
            if self.is_player_win() == " O":
                print(f"Player O win!")
                self.show_board()
                break
            self.show_board()
            if self.is_board_filled():
                print("It's a draw!")
                break
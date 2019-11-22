import tkinter
from tkinter import messagebox
import math
from tictactoe import TicTacToe

class GameManager:
    def __init__(self):
        self.ttt = TicTacToe()

    def play(self):
        #show_board()
        print(self.ttt)
        while True:
            #input()
            row = int(input("row: "))
            col = int(input("col: "))
            self.ttt.set(row, col)
            print(self.ttt)
            #check_winner()
            if self.ttt.check_winner() in ["O", "X", "d"]:
                break

        if self.ttt.check_winner() == "O":
            #  O:
            print("O가 이겼습니다.")
        elif self.ttt.check_winner() == "X":
            #  X:
            print("X가 이겼습니다.")
        elif self.ttt.check_winner() == "d":
            #  d:
            print("무승부입니다.")

class GameManager_GUI:
    def __init__(self):
        CANVAS_SIZE = 300
        self.TILE_SIZE = CANVAS_SIZE/3

        self.root = tkinter.Tk()
        self.root.title("틱택토")
        self.root.geometry(str(CANVAS_SIZE)+"x"+str(CANVAS_SIZE))
        self.root.resizable(width=False, height=False)
        self.canvas = tkinter.Canvas(self.root, bg="white", width=CANVAS_SIZE, height=CANVAS_SIZE)
        self.canvas.pack()
        self.images = dict()
        self.images["O"] = tkinter.PhotoImage(file="O.gif")
        self.images["X"] = tkinter.PhotoImage(file="X.gif")

        self.ttt = TicTacToe()
        self.canvas.bind("<Button-1>", self.click_handler)

    def click_handler(self, event):
        self.ttt.set(math.floor(event.y/self.TILE_SIZE), math.floor(event.x/self.TILE_SIZE))
        print(math.floor(event.y/self.TILE_SIZE), math.floor(event.x/self.TILE_SIZE))
        self.draw_board()
        #check_winner()
        if self.ttt.check_winner() == "O":
            #  O:
            messagebox.showinfo("Game Over", "O가 이겼습니다.")
            self.root.quit()
        elif self.ttt.check_winner() == "X":
            #  X:
            messagebox.showinfo("Game Over", "X가 이겼습니다.")
            self.root.quit()
        elif self.ttt.check_winner() == "d":
            #  d:
            messagebox.showinfo("Game Over", "무승부입니다.")
            self.root.quit()

    def draw_board(self):
        # clear
        self.canvas.delete("all")

        SIZE = 100
        x = 0
        y = 0
        for i, v in enumerate(self.ttt.board):
            if v == ".":
                pass
            elif v == "O":
                self.canvas.create_image(x, y, anchor="nw", image=self.images["O"])
            elif v == "X":
                self.canvas.create_image(x, y, anchor="nw",image=self.images["X"])
            x += SIZE
            if i % 3 == 2:
                x = 0
                y += SIZE

    def play(self):
        self.root.mainloop()


if __name__ == '__main__':
    # gm = GameManager()
    gm = GameManager_GUI()
    gm.play()
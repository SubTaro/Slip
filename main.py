import numpy as np


# ボードの状態
# 何もない: 0
# 白: 1
# 白親: 2
# 黒: -1
# 黒親: -2
class Board:
    def __init__(self):
        self.board = np.zeros([5, 5])
        self.board[0, :] = -1
        self.board[4, :] = 1
        self.board[0, 2] = -2
        self.board[4, 2] = 2

    def print_board(self):
        print(self.board)

    # 動かすコマンドを実装
    # "動かすものの座標 + 向き"でコマンドは構成されるものとする
    # 向きは上下左右(t, b, l, r)とする
    def move(self, command):
        pos = [int(s) for s in command[:2]]
        direction = command[2]
        piece = self.board[pos[0], pos[1]]

        # どこかに当たるまで繰り返す
        while (True):
            if self.is_move(pos, direction):
                if direction == 't':
                    self.board[pos[0]-1, pos[1]] = piece
                    # 元のマスの値を初期化
                    self.board[pos[0], pos[1]] = 0
                    pos[0] = pos[0]-1
                elif direction == 'b':
                    self.board[pos[0]+1, pos[1]] = piece
                    # 元のマスの値を初期化
                    self.board[pos[0], pos[1]] = 0
                    # 自分の位置を更新
                    pos[0] = pos[0]+1
                elif direction == 'l':
                    self.board[pos[0], pos[1]-1] = piece
                    # 元のマスの値を初期化
                    self.board[pos[0], pos[1]] = 0
                    # 自分の位置を更新
                    pos[1] = pos[1]-1
                elif direction == 'r':
                    self.board[pos[0], pos[1]+1] = piece
                    # 元のマスの値を初期化
                    self.board[pos[0], pos[1]] = 0
                    # 自分の位置を更新
                    pos[1] = pos[1]+1
                else:
                    print("Direction error")
            else:
                break

    # 上下左右に動けるかのチェックを行う
    def is_move(self, pos, direction):
        check = True
        if direction == 't':
            if pos[0] == 0 or self.board[pos[0]-1, pos[1]] != 0:
                check = False
        if direction == 'b':
            if pos[0] == 4 or self.board[pos[0]+1, pos[1]] != 0:
                check = False
        if direction == 'l':
            if pos[1] == 0 or self.board[pos[0], pos[1]-1] != 0:
                check = False
        if direction == 'r':
            if pos[1] == 4 or self.board[pos[0], pos[1]+1] != 0:
                check = False

        return check

    # 誰かが勝ったかどうかの判定用
    def is_end(self):
        end = False
        if self.board[2, 2] == -2:
            print("black win")
            end = True

        if self.board[2, 2] == 2:
            print("white win")
            end = True

        return end


if __name__ == "__main__":
    board = Board()
    while (not board.is_end()):
        board.print_board()
        command = input()
        board.move(command)

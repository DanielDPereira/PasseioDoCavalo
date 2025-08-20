import tkinter as tk
import time

N = 8
delay = 0.3

moves = [
    (2, 1), (1, 2), (-1, 2), (-2, 1),
    (-2, -1), (-1, -2), (1, -2), (2, -1)
]

def is_valid(x, y, board):
    return 0 <= x < N and 0 <= y < N and board[y][x] == -1

def count_onward_moves(x, y, board):
    count = 0
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny, board):
            count += 1
    return count

def next_move(x, y, board):
    candidates = []
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny, board):
            c = count_onward_moves(nx, ny, board)
            candidates.append((c, nx, ny))
    candidates.sort()
    return [(nx, ny) for c, nx, ny in candidates]

def knight_tour(x, y, move_count, board, path):
    board[y][x] = move_count
    path.append((x, y))

    if move_count == N * N - 1:
        return True

    for nx, ny in next_move(x, y, board):
        if knight_tour(nx, ny, move_count + 1, board, path):
            return True

    board[y][x] = -1
    path.pop()
    return False

class ChessGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Passeio do Cavalo")
        self.canvas = tk.Canvas(self.master, width=480, height=480)
        self.canvas.pack()
        self.square_size = 60
        self.board = [[-1 for _ in range(N)] for _ in range(N)]
        self.path = []

        start_x, start_y = 0, 0
        knight_tour(start_x, start_y, 0, self.board, self.path)

        self.draw_board()
        self.master.after(1000, self.animate_knight)

    def draw_board(self):
        for y in range(N):
            for x in range(N):
                color = "white" if (x + y) % 2 == 0 else "gray"
                self.canvas.create_rectangle(
                    x * self.square_size,
                    y * self.square_size,
                    (x + 1) * self.square_size,
                    (y + 1) * self.square_size,
                    fill=color
                )

    def animate_knight(self):
        for i, (x, y) in enumerate(self.path):
            self.canvas.create_oval(
                x * self.square_size + 15,
                y * self.square_size + 15,
                x * self.square_size + 45,
                y * self.square_size + 45,
                fill="blue"
            )
            self.canvas.create_text(
                x * self.square_size + 30,
                y * self.square_size + 30,
                text=str(i+1),
                fill="white",
                font=("Arial", 10, "bold")
            )
            self.master.update()
            time.sleep(delay)

if __name__ == "__main__":
    root = tk.Tk()
    gui = ChessGUI(root)
    root.mainloop()

import tkinter as tk
import random

# GameBoard Class
class GameBoard:
    def __init__(self, root):
        self.root = root
        self.grid_size = 10
        self.cell_size = 40
        self.board = [[None for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.colors = ["red", "blue", "green", "yellow", "purple"]
        self.draw_board()

    def draw_board(self):
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                cell = tk.Frame(
                    self.root,
                    width=self.cell_size,
                    height=self.cell_size,
                    bg="white",
                    relief=tk.RAISED,
                    borderwidth=1,
                )
                cell.grid(row=row, column=col)
    
    def clear_matches(self):
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                if self.board[row][col]:
                    color = self.board[row][col]["bg"]
                    # Check horizontal match
                    if col <= self.grid_size - 3 and all(self.board[row][c] and self.board[row][c]["bg"] == color for c in range(col, col + 3)):
                        for c in range(col, col + 3):
                            self.board[row][c].destroy()
                            self.board[row][c] = None
                    # Check vertical match
                    if row <= self.grid_size - 3 and all(self.board[r][col] and self.board[r][col]["bg"] == color for r in range(row, row + 3)):
                        for r in range(row, row + 3):
                            self.board[r][col].destroy()
                            self.board[r][col] = None
    
    def place_block(self, block, x, y):
        grid_x = x // self.cell_size
        grid_y = y // self.cell_size
        if 0 <= grid_x < self.grid_size and 0 <= grid_y < self.grid_size and self.board[grid_y][grid_x] is None:
            block.place(x=grid_x * self.cell_size, y=grid_y * self.cell_size)
            self.board[grid_y][grid_x] = block
            self.clear_matches()

# Function to Handle Drag-and-Drop
def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x, y=y)

def drag_release(event, game_board):
    widget = event.widget
    x = widget.winfo_x()
    y = widget.winfo_y()
    game_board.place_block(widget, x, y)

# Initialize Tkinter
root = tk.Tk()
root.title("Color Match Block Puzzle")

# Create GameBoard
game_board = GameBoard(root)

# Generate Blocks Dynamically
for _ in range(5):  # 5 blocks to start with
    color = random.choice(game_board.colors)
    block = tk.Label(root, bg=color, width=3, height=2)
    block.place(x=random.randint(0, 200), y=random.randint(0, 200))
    block.bind("<Button-1>", drag_start)
    block.bind("<B1-Motion>", drag_motion)
    block.bind("<ButtonRelease-1>", lambda event, gb=game_board: drag_release(event, gb))

root.mainloop()
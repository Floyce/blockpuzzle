import tkinter as tk

# PuzzlePieces Class for Shapes and Drag-and-Drop Logic
class PuzzlePieces:
    @staticmethod
    def get_pieces():
        return {
            "L": [[1, 0], [1, 0], [1, 1]],
            "T": [[1, 1, 1], [0, 1, 0]],
            "Square": [[1, 1], [1, 1]],
        }

    @staticmethod
    def drag_start(event):
        widget = event.widget
        widget.startX = event.x
        widget.startY = event.y

    @staticmethod
    def drag_motion(event):
        widget = event.widget
        x = widget.winfo_x() - widget.startX + event.x
        y = widget.winfo_y() - widget.startY + event.y
        
        # Snap position to the closest grid cell
        snapped_x = round(x / 40) * 40  # 40 is the cell size
        snapped_y = round(y / 40) * 40
        widget.place(x=snapped_x, y=snapped_y)

        # Update the grid after placing the piece (you can expand the logic here)
        update_grid(widget, snapped_x, snapped_y)

# GameBoard Class for Drawing the Grid
class GameBoard:
    def __init__(self, root):
        self.root = root
        self.grid_size = 10
        self.cell_size = 40
        self.board = [[0 for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.draw_board()

    def draw_board(self):
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                cell = tk.Frame(
                    self.root,
                    width=self.cell_size,
                    height=self.cell_size,
                    bg='white',
                    relief=tk.RAISED,
                    borderwidth=1
                )
                cell.grid(row=row, column=col)

# Function to Update the Game Board Grid
def update_grid(piece, x, y):
    # Translate x, y positions into grid indices
    grid_x = x // 40  # 40 is the cell size
    grid_y = y // 40
    
    # Example logic to place the piece onto the board grid (expand this logic)
    for row_index, row in enumerate(PuzzlePieces.get_pieces()["L"]):  # Replace "L" with the actual piece
        for col_index, cell in enumerate(row):
            if cell == 1:  # If it's part of the piece
                game_board.board[grid_y + row_index][grid_x + col_index] = 1

# Function to Clear Filled Rows and Columns
def clear_rows_and_columns():
    for i in range(len(game_board.board)):
        # Check for filled rows
        if all(game_board.board[i]):
            game_board.board[i] = [0] * len(game_board.board[i])  # Clear the row
    
    # Check for filled columns
    for j in range(len(game_board.board[0])):
        if all(row[j] for row in game_board.board):
            for row in game_board.board:
                row[j] = 0  # Clear the column

# Initialize Tkinter and Create the GUI
root = tk.Tk()
root.title("Black")

game_board = GameBoard(root)

# Create a Draggable Puzzle Piece (Example: "L" Shape)
piece = tk.Label(root, text="Puzzle Piece", bg="blue", width=5, height=2)
piece.place(x=50, y=50)

piece.bind("<Button-1>", PuzzlePieces.drag_start)
piece.bind("<B1-Motion>", PuzzlePieces.drag_motion)

# Start the Tkinter main loop
root.mainloop()
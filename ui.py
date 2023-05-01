import tkinter as tk

from board import Board

root = tk.Tk()
root.title("TicTacToe!")

# we'll want some kind of game board widget
# top: current player
game = Board()

def player_to_text(player: int) -> str:
    if player == Board.CROSS:
        return "crosses"
    if player == Board.NOUGHT:
        return "noughts"
    return " "

current_player = tk.Label(root, text=f"Current player: {player_to_text(game.turn)}")
current_player.pack()

# middle: grid of cells
#   - each cell is a button
#   - when clicked, it calls a function
#   - the function updates the board
#   - the function updates the current player (ui registers a callback for this?)
#   - the function checks for a win or draw
#   - the function updates the ui
#   - invalid location buttons are disabled

CELL_SPACING = 2

board_ui = tk.Frame(root, bg="black")
board_ui.pack()

def draw_tile(row, col, tile):
    if tile == game.EMPTY: 
        tile_label = "  "
    elif tile == game.NOUGHT:
        tile_label = "O"
    elif tile == game.CROSS:
        tile_label = "X"
    
    cell = tk.Button(board_ui, text=tile_label)
    cell.grid(row=row, column=col, padx=CELL_SPACING, pady=CELL_SPACING)


from random import choice
for row in range(3):
    for col in range(3):
        draw_tile(row, col, game.get_tile(row, col))

# bottom: status message
status_message = tk.Label(root, text="Status: Playing")
status_message.pack()


root.lift()  # bring the window to the front
root.attributes('-topmost',True)
root.after_idle(root.attributes,'-topmost',False)

root.mainloop()

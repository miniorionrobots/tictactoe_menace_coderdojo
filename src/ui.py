import tkinter as tk

root = tk.Tk()
root.title("TicTacToe!")

# we'll want some kind of game board widget
# top: current player

current_player = tk.Label(root, text="Current player: Noughts")
current_player.pack()

# middle: grid of cells
#   - each cell is a button
#   - when clicked, it calls a function
#   - the function updates the board
#   - the function updates the current player (ui registers a callback for this?)
#   - the function checks for a win or draw
#   - the function updates the ui
#   - invalid location buttons are disabled

CELL_SPACING = 4

board = tk.Frame(root, bg="black")
board.pack()
from random import choice
for row in range(3):
    for col in range(3):
        cell = tk.Button(board, text=choice(["X", "O", "  "]))
        cell.grid(row=row, column=col, padx=CELL_SPACING, pady=CELL_SPACING)


# bottom: status message
status_message = tk.Label(root, text="Status: Playing")
status_message.pack()


root.lift()  # bring the window to the front
root.attributes('-topmost',True)
root.after_idle(root.attributes,'-topmost',False)

root.mainloop()

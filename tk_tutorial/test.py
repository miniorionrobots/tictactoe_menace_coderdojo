import tkinter as tk

root = tk.Tk()
root.title("TicTacToe!")

HEIGHT = 600
WIDTH = 600

# todo - centre
root.geometry(f"{HEIGHT}x{WIDTH}")

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

# bottom: status message
status_message = tk.Label(root, text="Status: Playing")
status_message.pack()


root.lift()  # bring the window to the front
root.attributes('-topmost',True)
root.after_idle(root.attributes,'-topmost',False)

root.mainloop()

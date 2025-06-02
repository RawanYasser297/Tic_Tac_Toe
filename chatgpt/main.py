import tkinter as tk
# from tkinter import messagebox
import logic
from sound import play_sound
# Initialize main window
root = tk.Tk()
root.title("Tic-Tac-Toe")
root.geometry("600x650")
root.configure(bg="lightgray")

# Global state
player_symbol = None
buttons = {}

# UI Fonts and Styles
FONT = ("Arial", 24, "bold")

#difficulty levels
difficulty = tk.StringVar(value="Medium")
difficulty_frame = tk.Frame(root, bg="lightgray")
tk.Label(difficulty_frame, text="Difficulty:", font=FONT, bg="lightgray").pack(side="left")
tk.OptionMenu(difficulty_frame, difficulty, "Easy", "Medium", "Hard").pack(side="left")
difficulty_frame.pack(pady=5)

def choose_symbol(symbol):
    global player_symbol
    player_symbol = symbol
    logic.set_player_symbol(symbol)
    logic.set_difficulty(difficulty.get())  # Pass difficulty to logic.py
    update_message(f"You chose {symbol}. Game started!")
    symbol_frame.pack_forget()
    reset_board()
    update_scores()




















# Label for messages
msg = tk.Label(root, text="Choose X or O", font=FONT, bg="lightgray")
msg.pack(pady=10)

# Score display
score_frame = tk.Frame(root, bg="lightgray")
player_score_lbl = tk.Label(score_frame, text="You: 0", font=FONT, bg="lightgray")
ai_score_lbl = tk.Label(score_frame, text="AI: 0", font=FONT, bg="lightgray")
player_score_lbl.pack(side="left", padx=20)
ai_score_lbl.pack(side="right", padx=20)
score_frame.pack(pady=5)

def update_scores():
    player_score_lbl.config(text=f"You: {logic.user['winningTimes']}")
    ai_score_lbl.config(text=f"AI: {logic.computer['winningTimes']}")

# Choose X or O
def choose_symbol(symbol):
    global player_symbol
    player_symbol = symbol
    logic.set_player_symbol(symbol)
    update_message(f"You chose {symbol}. Game started!")
    symbol_frame.pack_forget()
    reset_board()
    update_scores()

symbol_frame = tk.Frame(root, bg="lightgray")
tk.Button(symbol_frame, text="X", font=FONT, width=5, command=lambda: choose_symbol("X")).pack(side="left", padx=10)
tk.Button(symbol_frame, text="O", font=FONT, width=5, command=lambda: choose_symbol("O")).pack(side="left", padx=10)
symbol_frame.pack(pady=10)

# Game Board
board_frame = tk.Frame(root)
board_frame.pack()

def on_click(row, col):
    if not player_symbol:
        return
    if logic.board[row][col] == "":
        logic.make_move(row, col, player_symbol)
        play_sound("click.wav")
        update_board()
        if logic.check_winner(player_symbol):
            play_sound("win.wav")
            update_message("🎉 You win!")
            logic.user["winningTimes"] += 1
            update_scores()
            disable_board()
            return
        elif logic.is_draw():
            play_sound("lose-sound.wav")
            update_message("😐 It's a draw!")
            return
        # AI turn
        ai_move = logic.best_move()
        if ai_move:
            logic.make_move(*ai_move, logic.ai_symbol)
            update_board()
            if logic.check_winner(logic.ai_symbol):
                play_sound("lose-sound.wav")
                update_message("💻 AI wins!")
                logic.computer["winningTimes"] += 1
                update_scores()
                disable_board()
            elif logic.is_draw():
                play_sound("lose-sound.wav")
                update_message("😐 It's a draw!")

def update_board():
    for row in range(3):
        for col in range(3):
            buttons[(row, col)].config(text=logic.board[row][col])

def disable_board():
    for btn in buttons.values():
        btn.config(state="disabled")

def reset_board():
    logic.reset_board()
    for row in range(3):
        for col in range(3):
            btn = buttons.get((row, col))
            if not btn:
                btn = tk.Button(board_frame, text="", font=FONT, width=5, height=2,
                                command=lambda r=row, c=col: on_click(r, c))
                btn.grid(row=row, column=col, padx=5, pady=5)
                buttons[(row, col)] = btn
            btn.config(text="", state="normal")
    update_message("Your move!")

def update_message(text):
    msg.config(text=text)

# Reset button
tk.Button(root, text="Restart Game", font=FONT, command=reset_board).pack(pady=10)




root.mainloop()

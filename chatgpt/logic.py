import random

# Player data
user = {
    "choice": "",
    "winningTimes": 0
}

computer = {
    "choice": "",
    "winningTimes": 0
}

# Game state
board = [["" for _ in range(3)] for _ in range(3)]
player_symbol = ""
ai_symbol = ""

# Difficulty setting
current_difficulty = "Medium"

def set_difficulty(level):
    global current_difficulty
    current_difficulty = level

def set_player_symbol(symbol):
    global player_symbol, ai_symbol
    player_symbol = symbol
    ai_symbol = "O" if symbol == "X" else "X"

def make_move(row, col, symbol):
    board[row][col] = symbol

def reset_board():
    for row in range(3):
        for col in range(3):
            board[row][col] = ""

def is_draw():
    return all(cell != "" for row in board for cell in row) and not check_winner(player_symbol) and not check_winner(ai_symbol)

def check_winner(symbol):
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == symbol for j in range(3)) or all(board[j][i] == symbol for j in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == symbol for i in range(3)) or all(board[i][2 - i] == symbol for i in range(3)):
        return True
    return False

def best_move():
    if current_difficulty == "Easy":
        return random_easy_move()
    elif current_difficulty == "Medium":
        return random.choices(
            [minimax_move(), random_easy_move()],
            weights=[0.7, 0.3]
        )[0]
    else:  # Hard
        return minimax_move()

def random_easy_move():
    empty = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ""]
    return random.choice(empty) if empty else None

def minimax_move():
    best_score = -float('inf')
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                board[i][j] = ai_symbol
                score = minimax(False)
                board[i][j] = ""
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def minimax(is_maximizing):
    if check_winner(ai_symbol):
        return 1
    if check_winner(player_symbol):
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == "":
                    board[i][j] = ai_symbol
                    score = minimax(False)
                    board[i][j] = ""
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == "":
                    board[i][j] = player_symbol
                    score = minimax(True)
                    board[i][j] = ""
                    best_score = min(score, best_score)
        return best_score

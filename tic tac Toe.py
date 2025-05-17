import math

board = [" " for _ in range(9)]

def print_board(brd):
    print("\nCurrent board:")
    for i in range(3):
        print(f"| {brd[i*3]} | {brd[i*3+1]} | {brd[i*3+2]} |")
    print()

def get_available_moves(brd):
    return [i for i, spot in enumerate(brd) if spot == " "]

def check_winner(brd, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    return any(all(brd[i] == player for i in combo) for combo in win_conditions)

def is_draw(brd):
    return " " not in brd

def minimax(brd, depth, is_maximizing):
    if check_winner(brd, "O"):
        return {"score": 1 * (10 - depth)}
    elif check_winner(brd, "X"):
        return {"score": -1 * (10 - depth)}
    elif is_draw(brd):
        return {"score": 0}

    if is_maximizing:
        best = {"score": -math.inf}
        for move in get_available_moves(brd):
            brd[move] = "O"
            sim_score = minimax(brd, depth + 1, False)
            brd[move] = " "
            if sim_score["score"] > best["score"]:
                best = {"score": sim_score["score"], "move": move}
        return best
    else:
        best = {"score": math.inf}
        for move in get_available_moves(brd):
            brd[move] = "X"
            sim_score = minimax(brd, depth + 1, True)
            brd[move] = " "
            if sim_score["score"] < best["score"]:
                best = {"score": sim_score["score"], "move": move}
        return best

def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print("You are 'X'. The computer is 'O'.")
    print("Board positions are numbered as follows:")
    print("| 0 | 1 | 2 |\n| 3 | 4 | 5 |\n| 6 | 7 | 8 |")

    while True:
        print_board(board)

        while True:
            try:
                move = int(input("Your move (0-8): "))
                if move < 0 or move > 8 or board[move] != " ":
                    print("Invalid move. Try again.")
                else:
                    board[move] = "X"
                    break
            except ValueError:
                print("Please enter a valid number between 0 and 8.")

        if check_winner(board, "X"):
            print_board(board)
            print("🎉 You win! Great job.")
            break
        elif is_draw(board):
            print_board(board)
            print("It's a tie!")
            break

        print("Computer is thinking...")
        ai_move = minimax(board, 0, True)["move"]
        board[ai_move] = "O"

        if check_winner(board, "O"):
            print_board(board)
            print("😢 The computer wins! Better luck next time.")
            break
        elif is_draw(board):
            print_board(board)
            print("It's a tie!")
            break

if __name__ == "__main__":
    play_game()
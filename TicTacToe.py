def print_board(board):
    """Displays the current 3x3 board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    """Checks all win conditions and returns the winner or None."""
    # Check rows, columns, and diagonals
    lines = []
    lines.extend(board) # Rows
    lines.extend([[board[r][c] for r in range(3)] for c in range(3)]) # Cols
    lines.append([board[i][i] for i in range(3)]) # Diagonal 1
    lines.append([board[i][2-i] for i in range(3)]) # Diagonal 2

    for line in lines:
        if line[0] == line[1] == line[2] and line[0] != " ":
            return line[0]
    return None

def is_full(board):
    """Checks if the board is full (a draw)."""
    return all(cell != " " for row in board for cell in row)

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Welcome to Tic Tac Toe!")
    
    while True:
        print_board(board)
        try:
            move = input(f"Player {current_player}, enter row and col (0-2) separated by space: ")
            row, col = map(int, move.split())
            
            if board[row][col] != " ":
                print("That spot is taken! Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Enter two numbers between 0 and 2.")
            continue

        board[row][col] = current_player
        
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Congratulations! Player {winner} wins!")
            break
        
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break
            
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game()

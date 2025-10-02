from check import check_winner, get_opponent

# WIN: x = +1 / o = -1
# DRAW: 0
def minimax(board, player):
    if check_winner(board, 'X') == True:
        return 1  # 'X' (AI) wins
    elif check_winner(board, 'O') == True:
        return -1  # 'O' (Human) wins
    elif not any(None in row for row in board):
        return 0  # Draw
    
    opponent = get_opponent(player)

    if player == 'X':
        best_score = float("-inf") #worst score
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == None:
                    board[row][col] = player

                    score = minimax(board, opponent)
                    best_score = max(best_score, score)
                    board[row][col] = None
        return best_score
    else:
        best_score = float("inf") #worst score 
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == None:
                    board[row][col] = player

                    score = minimax(board, opponent)
                    best_score = min(best_score, score)
                    board[row][col] = None
        return best_score
                    

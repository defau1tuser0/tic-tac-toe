from minimax import minimax

def best_move(board, player):
    if player == 'X':
        opponent = 'O'
        best_score = float("-inf")
    else:
        opponent = 'X'
        best_score = float("inf")
    best_move = None

    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] is None:
                board[row][col] = player#make a ghost move

                score = minimax(board, opponent)
                
                if player == 'X': 
                    if score > best_score:
                        best_score = score
                        best_move = [row, col]
                else:
                    if score < best_score:
                        best_score = score
                        best_move = [row, col]
                board[row][col] = None #reset the board
                
    
    return best_move

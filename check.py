def check_winner(board, player):

    #ROW CHECK
    for row in board:
        if check_list(row, player):
            return True
    
    #COL CHECK
    for row in range(len(board)):
        col_list = []
        for col in range(len(board)):
            col_list.append(board[col][row])
        if check_list(col_list, player):
            return True
    
    #DIAGONAL CHECK
    left_diagonal_index = [(0, 0), (1, 1), (2, 2)]
    right_diagonal_index = [(0, 2), (1,1), (2, 0)]

    left_diagonal_list = []
    right_diagonal_list = []

    for row in range(len(board)):
        for col in range(len(board)):
            if (row, col) in left_diagonal_index:
                left_diagonal_list.append(board[row][col])
            if (row, col) in right_diagonal_index:
                right_diagonal_list.append(board[row][col])
            
    if check_list(left_diagonal_list, player) or check_list(right_diagonal_list, player):
        return True
    
    #On-Going
    for row in board:
        if None in row:
            return None
    #Draw
    return 0 


def check_list(arr, player):
    if None in arr:
        return False
    
    for element in arr:
        if element != player:
            return False

    return True

def get_opponent(player):
    if player == 'X':
        return 'O'
    else:
        return 'X'

def get_position(position):
    positional_board = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    for row in range(len(positional_board)):
        for col in range(len(positional_board)):
            if positional_board[row][col] == position:
                return row, col
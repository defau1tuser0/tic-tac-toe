board = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]

def display_board(board):
    count = 0
    print("----------------")
    for row in range(len(board)):
        for col in range(len(board)):
            count += 1
            print(f"| {board[row][col] or count} |", end='')
        print()
        print("----------------")

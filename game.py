import os
from display import board, display_board
from move import best_move
from check import check_winner, get_position

def clear_screen():
    #windows
    if os.name == "nt":
        _ = os.system("cls") # _ = ... so that return code doesn't get printed on console
    else: #mac/linux
        _ = os.system("clear")
    

def engine_vs_engine(board, engine_x, engine_o):
    current_player = engine_x

    while True:
        display_board(board)

        previous_player = engine_o if current_player is engine_x else engine_x
        winner_status = check_winner(board, previous_player)

        if winner_status == True:
            print(f"Player {previous_player} has WON!!!")
            break
        elif winner_status == 0:
            print("Draw...")
            break

        if current_player == engine_x:
            print("X AI's turn")
            move = best_move(board, current_player)
            if move:
                board[move[0]][move[1]] = current_player
            current_player = engine_o
        else:
            print("X AI's turn")
            move = best_move(board, current_player)
            if move:
                board[move[0]][move[1]] = current_player
            current_player = engine_x
        
        clear_screen()


def game(board, human_player, engine):
    current_player = human_player

    while True:
        display_board(board)

        previous_player = engine if current_player is human_player else human_player
        winner_status = check_winner(board, previous_player)

        if winner_status == True:
            print(f"Player {previous_player} has WON!!!")
            break
        elif winner_status == 0:
            print("Draw...")
            break
        
        if human_player == 'AI':
            return engine_vs_engine(board, 'X', 'O')
        else:
            if current_player == human_player:
                print("Your turn")
                while True: 
                    position = int(input("Enter your position: "))
                    if 0 < position < 10:
                        row, col = get_position(position)
                        if board[row][col] == None:
                            board[row][col] = current_player
                            break
                    print("Invalid position, try again")
                current_player = engine
            else:
                print("AI's turn")
                move = best_move(board, current_player)
                if move:
                    board[move[0]][move[1]] = current_player
                current_player = human_player
            
        clear_screen()
                
def main(board):
    role = ['X', 'O', 'AI']
    while True:
        human_player = input("Choose your role(X, O, AI): ").upper()
        if human_player in role:
            break
        else:
            print("Invalid role, try again")
    
    if human_player == 'O':
        opponent = 'X'
    else:
        opponent = 'O'

    clear_screen()
    game(board, human_player, opponent)

    

if __name__ == "__main__":
    main(board)
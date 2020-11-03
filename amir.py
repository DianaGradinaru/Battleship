# ships_for_player1 = [2, 1]
# ships_for_player2 = [2, 1]
#representation_water_on_map = 0
#representation_miss_on_map = 3
#representation_intact_ship_on_map = 1
#representation_hit_ship_on_map = 2
def clear():
    print ("\x1B[2J\x1B[0;H", end = "")
clear ()

def create_map():
    board = [[],[],[],[],[]]
    board_size = 5
    for i in range(board_size):
        board[i] = ["0"] * 5

    print ("Let's play Battleship!")
    print ("Here's the 5x5 board to begin:")

    print (board)

create_map()



# # create_map()
#   def display_current_player_turn(current_player_map, player_one_map):
#     if current_player_map == player_one_map:
#         print("=== PLAYER 1 IS SHOOTING NOW ===")
#     else:
#         print("=== PLAYER 2 IS SHOOTING NOW ===")



# create_map()
# display_current_player_turn()
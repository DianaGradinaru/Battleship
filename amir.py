

def create_map():
    board = []
    for i in range(0,5):
      board.append(["0"] * 5)
    return board


def display_current_player_turn(current_player_map, player_one_map):
    if current_player_map == player_one_map:
        print("=== PLAYER 1 IS SHOOTING NOW ===")
    else:
        print("=== PLAYER 2 IS SHOOTING NOW ===")

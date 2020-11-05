from diana import mark_ship_on_map
from amir import create_map
from iulia import read_coordinates

ships_for_player1 = [2, 1]
ships_for_player2 = [2, 1]
representation_water_on_map = "0"
representation_miss_on_map = "3"
representation_ship_on_map = "1"
representation_hit_ship_on_map = "2"
representation_sunk_ship_on_map = "4"


def display_game_map(game_map):
    print(" ", end="")
    for x in range(65, 70):
        print("  " + chr(x) + "  ", end="")
    print()
    for row in range(5):
        print((row + 1), end=" ")
        for col in range(5):
            print(f" {game_map[row][col]}" + " | ", end="")
        print("\n " + "----+" * 5)


def place_ships_on_map(ships):
    game_map = create_map()
    for ship in ships:
        [x_axis, y_axis] = read_coordinates()

        mark_ship_on_map(game_map, ship, x_axis, y_axis)
        display_game_map(game_map)
    return game_map


def has_lost(enemy_map):
    for sub_list in enemy_map:
        for item in sub_list:
            if item == representation_ship_on_map:
                return False
    return True

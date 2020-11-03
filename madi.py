from amir import create_map
from iulia import read_coordinates


def display_game_map(game_map):
    for x in range(65, 70):
        print("  " + chr(x) + " ", end="")
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


def has_lost(map):
    pass

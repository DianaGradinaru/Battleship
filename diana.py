from iulia import read_coordinates
representation_water_on_map = "0"
representation_miss_on_map = "3"
representation_intact_ship_on_map = "1"
representation_hit_ship_on_map = "2"


def mark_ship_on_map(game_map, ship, x_axis, y_axis):
    if game_map[y_axis][x_axis] == representation_intact_ship_on_map:
        print("That spot already has a battleship in it!")
    else:
        game_map[y_axis][x_axis] = representation_intact_ship_on_map

    return game_map


def display_enemy_map(game_map):

    for x in range(65, 70):
        print("  " + chr(x) + "   ", end="")
    print()
    for row in range(5):
        print((row + 1), end=" ")
        for col in range(5):
            if game_map[row][col] == representation_miss_on_map:
                print(" M | ", end="")
            elif game_map[row][col] == representation_hit_ship_on_map:
                print(" H | ", end="")
            elif (
                game_map[row][col] == representation_intact_ship_on_map
                or game_map[row][col] == representation_water_on_map
            ):
                print(" 0 | ", end="")
        print("\n " + "----+" * 5)

    # for row in game_map:
    #     print("")
    #     for cell in row:
    #         if cell == representation_miss_on_map:
    #             print("M", end="")
    #         elif cell == representation_hit_ship_on_map:
    #             print("H", end="")
    #         elif cell == representation_intact_ship_on_map:
    #             print("0", end="")
    #         elif cell == representation_water_on_map:
    #             print("0", end="")
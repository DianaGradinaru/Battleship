def mark_ship_on_map(game_map, ship, x_axis, y_axis):
    for n in range(5):
        if game_map[y_axis][x_axis] == representation_intact_ship_on_map:
            print("That spot already has a battleship in it!")

        game_map[y_axis][x_axis] = representation_intact_ship_on_map
        return game_map


def display_enemy_map(game_map):
    for row in game_map:
        print("")
        for cell in row:
            if cell == representation_miss_on_map:
                print("M", end="")
            elif cell == representation_hit_ship_on_map:
                print("H", end="")
            elif cell == representation_intact_ship_on_map:
                print("0", end="")
            elif cell == representation_water_on_map:
                print("0", end="")
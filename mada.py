def shoot_at_coordinates(game_map, x_axis, y_axis):
    if game_map[y_axis][x_axis] == representation_water_on_map:
        game_map[y_axis][x_axis] = representation_miss_on_map
        print("YOU HAVE MISSED.")
        return
    if game_map[y_axis][x_axis] == representation_intact_ship_on_map:
        if ship_has_no_more_lives(game_map, x_axis, y_axis):
            mark_whole_ship_as_dead(game_map, x_axis, y_axis)
            print("YOU HAVE SUNK A SHIP")
        else:
            game_map[y_axis][x_axis] = representation_hit_ship_on_map
            print("YOU HAVE HIT A SHIP")
        return
    print("YOU HAVE HIT A PLACE THAT WAS ALREADY HIT")
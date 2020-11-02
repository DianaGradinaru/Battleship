ships_for_player1 = [2,1]
ships_for_player2 = [2,1]
representation_water_on_map = 0 
representation_miss_on_map = 3
representation_ship_on_map = 1
representation_hit_ship_on_map = 2





def mark_whole_ship_as_dead(game_map, x_axis, y_axis): 
    if game_map[x_axis][y_axis] == representation_hit_ship_on_map:
        return True
    else:
        return False 


def shoot_at_coordinates(game_map, x_axis, y_axis):  
    if game_map[x_axis][y_axis] == representation_water_on_map:
        game_map[x_axis][y_axis] == representation_miss_on_map
        print("You have missed")
        return
    if game_map[x_axis][y_axis] == representation_ship_on_map:
        if ship_has_no_more_lives(game_map, x_axis, y_axis):
            mark_whole_ship_as_dead(game_map, x_axis, y_axis)
            print("You have sunk a ship!")
        else:
            game_map[x_axis][y_axis] == representation_hit_ship_on_map
            print('You have hit a ship!')
        return
    print('You have made a hit at previous hit place!')
game_map = [
    [0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]
print("======")
shoot_at_coordinates(game_map, 1, 2 )



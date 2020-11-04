from madi import display_game_map
from diana import display_enemy_map
ships_for_player1 = [2,1]
ships_for_player2 = [2,1]
representation_water_on_map = "0"
representation_miss_on_map = "3"
representation_ship_on_map = "1"
representation_hit_ship_on_map = "2"


def ship_has_no_more_lives(game_map, x_axis, y_axis):
    if game_map[x_axis][y_axis-1] == representation_ship_on_map or game_map[x_axis][y_axis+1] == representation_ship_on_map:
        return False    
    else:
        return True


def mark_whole_ship_as_dead(game_map, x_axis, y_axis): 
    if game_map[x_axis][y_axis] == representation_hit_ship_on_map:
        return True
    else:
        return False 


def shoot_at_coordinates(game_map, x_axis, y_axis):  
    print(game_map[x_axis][y_axis])
    if game_map[x_axis][y_axis] == representation_water_on_map:
        game_map[x_axis][y_axis] = representation_miss_on_map
        print("You have missed")
        display_enemy_map(game_map)
        
    if game_map[x_axis][y_axis] == representation_ship_on_map:
        if ship_has_no_more_lives(game_map, x_axis, y_axis):
            mark_whole_ship_as_dead(game_map, x_axis, y_axis)
            print("You have sunk a ship!")
            #legatura cu functia has_lost
            
        else:
            game_map[x_axis][y_axis] == representation_hit_ship_on_map
            print('You have hit a ship!')
            display_enemy_map(game_map) 



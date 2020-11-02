from amir import create_map
from iulia import read_coordinates
from madi import display_game_map, place_ships_on_map, ship_has_no_more_lives, has_lost


ships_for_player1 = [2, 1]
ships_for_player2 = [2, 1]
representation_water_on_map = 0
representation_miss_on_map = 3
representation_intact_ship_on_map = 1
representation_hit_ship_on_map = 2


def mark_ship_on_map(game_map, ship, x_axis, y_axis):
    for n in range(5):
        if game_map[y_axis][x_axis] == representation_intact_ship_on_map:
            print("That spot already has a battleship in it!")

        game_map[y_axis][x_axis] = representation_intact_ship_on_map
        return game_map


def mark_whole_ship_as_dead(game_map, x_axis, y_axis):

    pass


def display_current_player_turn(current_player_map, player_one_map):
    if current_player_map == player_one_map:
        print("=== PLAYER 1 IS SHOOTING NOW ===")
    else:
        print("=== PLAYER 2 IS SHOOTING NOW ===")


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


def start():
    print("=== PLAYER 1 TURN TO PLACE SHIPS ON MAP ===")
    map1 = place_ships_on_map(ships_for_player1)
    print("=== PLAYER 2 TURN TO PLACE SHIPS ON MAP ===")
    map2 = place_ships_on_map(ships_for_player2)

    shooting_player_map = map1
    enemy_map = map2
    while True:
        display_current_player_turn(shooting_player_map, map1)
        [y_axis, x_axis] = read_coordinates()
        shoot_at_coordinates(enemy_map, x_axis, y_axis)
        display_enemy_map(enemy_map)
        if has_lost(enemy_map):
            display_winner(shooting_player_map, map1)
            return
        temp = shooting_player_map
        shooting_player_map = enemy_map
        enemy_map = temp


if __name__ == "__main__":
    start()

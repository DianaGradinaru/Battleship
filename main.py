from amir import create_map
from mada import shoot_at_coordinates
from diana import mark_ship_on_map, display_enemy_map
from iulia import read_coordinates
from madi import display_game_map


# generating random numbers to place the ship
# row = random.randint(0, 5)
# col = random.randint(0, 5)
# # generating random location point for horizental and vertical
# randomnumber = random.randint(0, 1)
# letters and numbers for the table
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

    # for sh in game_map:
    #     x_axis, y_axis = sh
    #     if sh:
    #         ch = "X"
    #     else:
    #         ch = "0"
    #     game_map[x_axis][y_axis] = ch

    # if board[row][col] == "0":
    #     if ship == 1:
    #         board[row][col] = "X"
    #     elif ship == 2:
    #         board[row][col] = "Y"
    # return


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


def display_winner(shooting_player_map, map1):

    pass


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

import random
from amir import create_map
from mada import shoot_at_coordinates

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


def read_coordinates():
    # verify if number is between 1 and 5 and letter between A and E
    coordinates = input(
        "Please enter coordinates in the form [letter][number]: "
    ).upper()
    rows = ["A", "B", "C", "D", "E"]
    cols = ["1", "2", "3", "4", "5"]

    inp = []
    for char in coordinates:
        if char != " ":
            inp.append(char)

    while inp[0] not in rows or inp[1] not in cols:
        inp = []
        print("Invalid input")
        user_text = input("Please enter coordinates ").upper()
        for char in user_text:
            if char != " ":
                inp.append(char)

    # while inp[0] not in rows or inp[1] not in cols:
    #     inp = []
    #     print("Ship already there")
    #     user_text = input("Please enter coordinates  ").upper()
    #     for char in user_text:
    #         if char != "X":
    #             inp.append(char)

    return [rows.index(inp[0]), cols.index(inp[1])]


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


def ship_has_no_more_lives(game_map, x_axis, y_axis):

    pass


def mark_whole_ship_as_dead(game_map, x_axis, y_axis):

    pass


def place_ships_on_map(ships):
    game_map = create_map()
    for ship in ships:
        [x_axis, y_axis] = read_coordinates()

        mark_ship_on_map(game_map, ship, x_axis, y_axis)
        display_game_map(game_map)
    return game_map


def display_current_player_turn(current_player_map, player_one_map):
    if current_player_map == player_one_map:
        print("=== PLAYER 1 IS SHOOTING NOW ===")
    else:
        print("=== PLAYER 2 IS SHOOTING NOW ===")





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


def has_lost(map):
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
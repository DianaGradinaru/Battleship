from diana import mark_ship_on_map
from amir import create_map
from iulia import read_coordinates
import os
import time

ships_for_player1 = [2, 1]
ships_for_player2 = [2, 1]
representation_water_on_map = "0"
representation_miss_on_map = "3"
representation_ship_on_map = "1"
representation_hit_ship_on_map = "2"
representation_sunk_ship_on_map = "4"


def loading():
    strings = []

    strings.append("""
    |=============================================|
    |#####                                        |
    |==================== 11% ====================|
                Loading Unreal Engine 4
    """)

    strings.append("""
    |=============================================|
    |################################             |
    |==================== 66% ====================|
                   Loading textures
    """)

    strings.append("""
    |=============================================|
    |#############################################|
    |==================== 100% ===================|
    """)

    os.system("clear")
    os.system("clear")
    for i in range(3):
        time.sleep(1.1)
        os.system("clear")
        print(strings[i])
        time.sleep(1.1)


def intro():
    """plays before starting the game"""
    l = []
    l.append(" ______     ______     ______   ______   __         ______     ______     __  __     __     ______  ")
    l.append("/\  == \   /\  __ \   /\__  _\ /\__  _\ /\ \       /\  ___\   /\  ___\   /\ \_\ \   /\ \   /\  == \ ")
    l.append("\ \  __<   \ \  __ \  \/_/\ \/ \/_/\ \/ \ \ \____  \ \  __\   \ \___  \  \ \  __ \  \ \ \  \ \  __/ ")
    l.append(" \ \_____\  \ \_\ \_\    \ \_\    \ \_\  \ \_____\  \ \_____\  \/\_____\  \ \_\ \_\  \ \_\  \ \_\   ")
    l.append("  \/_____/   \/_/\/_/     \/_/     \/_/   \/_____/   \/_____/   \/_____/   \/_/\/_/   \/_/   \/_/   ")
    l.append("                                                                                                    ")
    l.append("                                                  # #  ( )                                          ")
    l.append("                                               ___#_#___|__                                         ")
    l.append("                                           _  |____________|  _                                     ")
    l.append("                                    _=====| | |            | | |==== _                              ")
    l.append("                              =====| |.---------------------------. | |====                         ")
    l.append("                <--------------------'   .  .  .  .  .  .  .  .   '--------------/                  ")
    l.append("                  \                                                             /                   ")
    l.append("                   \___________________________________________________________/                    ")
    l.append("               wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww                ")
    l.append("             wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww               ")
    l.append("                wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww                 ")
    for i in range(1, len(l[0]) + 1):
        os.system("clear")
        for j in l:
            print(j[-i:])
            time.sleep(0.003)

    time.sleep(1)
    input("""
                           +-++-++-++-++-+ +-++-++-++-++-+ +-++--+++
                           |  P R E S S  E N T E R  T O  S T A R T  |
                           +-++-++-++-++-+ +-++-++-++-++-+ ++-++-+++""")

    for i in range(len(l[0])):
        os.system("clear")
        for j in l:
            print(j[i:])
            time.sleep(0.003)


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

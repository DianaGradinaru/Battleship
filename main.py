from amir import display_current_player_turn
from mada import shoot_at_coordinates
from iulia import read_coordinates
from madi import place_ships_on_map, has_lost, loading, intro
import os

ships_for_player1 = [2, 1]
ships_for_player2 = [2, 1]
representation_water_on_map = "0"
representation_miss_on_map = "3"
representation_intact_ship_on_map = "1"
representation_hit_ship_on_map = "2"
representation_sunk_ship_on_map = "4"


def start():
    loading()
    intro()
    print(" ")
    print("===== PLAYER 1 TURN TO PLACE SHIPS ON MAP =====")
    map1 = place_ships_on_map(ships_for_player1)
    print("===== PLAYER 2 TURN TO PLACE SHIPS ON MAP =====")
    map2 = place_ships_on_map(ships_for_player2)

    shooting_player_map = map1
    enemy_map = map2
    current_player_name = "Player 1"

    while True:
        display_current_player_turn(shooting_player_map, map1)
        [y_axis, x_axis] = read_coordinates()
        shoot_at_coordinates(enemy_map, x_axis, y_axis)

        if has_lost(enemy_map):
            print(f"{current_player_name} has won!")
        else:
            continue

        temp = shooting_player_map
        shooting_player_map = enemy_map
        enemy_map = temp
        if current_player_name == "Player 1":
            current_player_name = "Player 2"

        playagain = ""
        while playagain != "y" or playagain != "Y" or playagain != "n" or playagain != "N":
            playagain = input("Do you want to play again?  y/n:")
            if playagain == "y" or playagain == "Y":
                start()
            elif playagain == "n" or playagain == "N":
                os.system("clear")
                quit()


if __name__ == "__main__":
    start()

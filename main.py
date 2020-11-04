from amir import create_map
from mada import shoot_at_coordinates, mark_whole_ship_as_dead, ship_has_no_more_lives
from diana import mark_ship_on_map, display_enemy_map
from iulia import read_coordinates
from madi import display_game_map, place_ships_on_map, has_lost


ships_for_player1 = [2, 1]
ships_for_player2 = [2, 1]
representation_water_on_map = 0
representation_miss_on_map = 3
representation_intact_ship_on_map = 1
representation_hit_ship_on_map = 2


#   Ii dau functiei DISPLAY_CURRENT_PLAYER doi parametrii: care e jucatorul care trage acum -> acesta
# poate fi MAP1 sau MAP2. Desi incepe cu MAP1, se poate schimba in urmatoarea iteratie si poate sa devina
# MAP2 (din temp = ... , vezi liniile 64 - 66) unde se face swich maps. Daca variabila care se afla in
# SHOOTING_PLAYER_MAP este tot MAP1, atunci pot sa afisez din functia DISPLAY_CURRENT_PLAYER -> player 1
# is shooting! Daca atat in CURRENT_PLAYER_MAP cat si in PLAYER_ONE_MAP se afla MAP1 (vezi linia 52 !!!),
# atunci este harta jucatorului 1. Dar daca in CURRENT_PLAYER_MAP se afla harta celui de-al doilea
# jucator, asta inseamna ca nu e MAP1.


def display_current_player_turn(current_player_map, player_one_map):
    # daca in ambele "galeti" am aceiasi harta, atunci e randul jucatorului 1
    if current_player_map == player_one_map:
        print("=== PLAYER 1 IS SHOOTING NOW ===")
    else:
        print("=== PLAYER 2 IS SHOOTING NOW ===")


def display_winner(shooting_player_map, map1)


pass


def start():
    print("=== PLAYER 1 TURN TO PLACE SHIPS ON MAP ===")
    # aici avem harta cu navele primului jucator
    map1 = place_ships_on_map(ships_for_player1)
    print("=== PLAYER 2 TURN TO PLACE SHIPS ON MAP ===")
    # aici avem harta cu navele celui de-al doilea jucator
    map2 = place_ships_on_map(ships_for_player2)

    # pentru a sti care e primul jucator care trage, spunem ca e randul celui care are map1
    shooting_player_map = map1
    enemy_map = map2
    while True:  # iteram fiecare tura in care trage un jucator
        # spunem randul carui jucator este
        display_current_player_turn(shooting_player_map, map1)
        # citim coordonatele unde vrem sa tragem
        [y_axis, x_axis] = read_coordinates()
        # vrem sa tragem la aceste coordonate in harta inamicului
        shoot_at_coordinates(enemy_map, x_axis, y_axis)
        # dupa ce am tras, aratam harta inamicului
        display_enemy_map(enemy_map)
        # vrem sa vedem daca inamicul mai are nave intacte, daca nu -> display winner
        if has_lost(enemy_map):
            display_winner(shooting_player_map, map1)
            return
        # daca nu a castigat jucatorul curent, ii inversam prin metoda variabilei intermediare
        temp = shooting_player_map
        shooting_player_map = enemy_map
        enemy_map = temp


if __name__ == "__main__":
    start()

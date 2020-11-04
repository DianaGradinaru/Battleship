def read_coordinates(board_size = 5):
    coordinates = input("Please enter coordinates in the form [letter][number]: ").upper()
    char = ""

    if board_size == 5:
        rows = ["A", "B", "C", "D", "E"]
        cols = ["1", "2", "3", "4", "5"]
    elif board_size == 6:
        rows = ["A", "B", "C", "D", "E", "F"]
        cols = ["1", "2", "3", "4", "5", "6"]
    elif board_size == 7:
        rows = ["A", "B", "C", "D", "E", "F", "G"]
        cols = ["1", "2", "3", "4", "5", "6", "7"]
    elif board_size == 8:
        rows = ["A", "B", "C", "D", "E", "F", "G", "H"]
        cols = ["1", "2", "3", "4", "5", "6", "7", "8"]
    elif board_size == 9:
        rows = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
        cols = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    elif board_size == 10:
        rows = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        cols = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    inp = []

    if len(coordinates) > 2:
        for char in coordinates:
            inp.append(char)
        if inp[1] == "1" and inp[2] == "0":
            inp[1] = "10"
        else:
            inp = ["1","A"]
            print("Invalid input") 
            user_text = input("Please enter coordinates: ").upper()
    else:
        for char in coordinates:
            if char != " ":
                inp.append(char)
            else:
                inp = ["1","A"]

    while inp[0] not in rows or inp[1] not in cols: 
        inp = []  
        print("Invalid input") 
        user_text = input("Please enter coordinates: ").upper()
        if len(user_text) > 2:
            for char in user_text:
                inp.append(char)
            if inp[1] == "1" and inp[2] == "0":
                inp[1] = "10"
            else:
                inp = ["1","A"]
                print("Invalid input") 
                user_text = input("Please enter coordinates: ").upper()
        else:
            for char in user_text:
                if char == " ":
                    inp = ["1","A"]
                else:
                    inp.append(char)
    if inp[0] == "A": inp [0] = 0
    if inp[0] == "B": inp [0] = 1
    if inp[0] == "C": inp [0] = 2
    if inp[0] == "D": inp [0] = 3
    if inp[0] == "E": inp [0] = 4
    if inp[0] == "F": inp [0] = 5
    if inp[0] == "G": inp [0] = 6
    if inp[0] == "H": inp [0] = 7
    if inp[0] == "I": inp [0] = 8
    if inp[0] == "J": inp [0] = 9
    if inp[1] == 1: inp [0] = 0
    if inp[1] == 2: inp [0] = 1
    if inp[1] == 3: inp [0] = 2
    if inp[1] == 4: inp [0] = 3
    if inp[1] == 5: inp [0] = 4
    if inp[1] == 6: inp [0] = 5
    if inp[1] == 7: inp [0] = 6
    if inp[1] == 8: inp [0] = 7
    if inp[1] == 9: inp [0] = 8
    if inp[1] == 10: inp [0] = 9
    return inp[0], inp[1]

print (read_coordinates())

def display_winner():
    player1_ships = len(ships_for_player1)
    player2_ships = len(ships_for_player2)
    if player1_ships == 0:
        return "Player 2 wins. Game over. "
    if player2_ships == 0:
        return "Player 1 wins. Game over. "


def read_coordinates():
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
    return [rows.index(inp[0]), cols.index(inp[1])]

def display_winner(ships_for_player1, ships_for_player2):
    player1_ships = len(ships_for_player1)
    player2_ships = len(ships_for_player2)
    if player1_ships == 0:
        return "Player 2 wins. Game over. "
    if player2_ships == 0:
        return "Player 1 wins. Game over. "
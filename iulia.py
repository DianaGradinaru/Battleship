def read_coordinates():
    coordinates = input(
        "Please enter coordinates in the form [letter][number]: "
    ).upper()
    rows = ["A", "B", "C", "D", "E"]
    cols = ["1", "2", "3", "4", "5"]

    inp = []

    if len(coordinates) > 2:
        for char in coordinates:
            inp.append(char)
        else:
            inp = ["1", "A"]
            print("Invalid input")
            user_text = input("Please enter coordinates: ").upper()
    elif len(coordinates) == 1:
        inp = ["1", "A"]
    else:
        for char in coordinates:
            if char != " ":
                inp.append(char)
            else:
                inp = ["1", "A"]

    while inp[0] not in rows or inp[1] not in cols: 
        inp = []
        print("Invalid input")
        user_text = input("Please enter coordinates: ").upper()
        if len(user_text) > 2:
            for char in user_text:
                inp.append(char)
            else:
                inp = ["1", "A"]
                print("Invalid input")
                user_text = input("Please enter coordinates: ").upper()
        elif len(user_text) == 1:
            inp = ["1", "A"]
        else:
            for char in user_text:
                if char == " ":
                    inp = ["1", "A"]
                else:
                    inp.append(char)

    return [rows.index(inp[0]), cols.index(inp[1])]

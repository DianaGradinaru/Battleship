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
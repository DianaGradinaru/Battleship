def read_coordinates(board_size = 5):
    # verify if number is between 1 and 5 and letter between A and E
    coordinates = input(
        "Please enter coordinates in the form [letter][number]: "
    ).upper()
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
    if coordinates == "A10":
        inp = ["A","10"]
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
        if coordinates == "A10":
            inp = ["A","10"]
        else:
            for char in user_text: 
                if char == " ":    
                    inp = ["1","A"]
                else:
                    inp.append(char)   

    # while inp[0] not in rows or inp[1] not in cols:
    #     inp = []
    #     print("Ship already there")
    #     user_text = input("Please enter coordinates  ").upper()
    #     for char in user_text:
    #         if char != "X":
    #             inp.append(char)

    #return [rows.index(inp[0]), cols.index(inp[1])] 

    return inp[0], inp[1]

print(read_coordinates(10))
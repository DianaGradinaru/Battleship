def create_map():
    board = []
    for x in range(0, 5):
        board.append([representation_water_on_map] * 5)

    return board
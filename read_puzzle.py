
def read_puzzle(puzzle_file_name, puzzle_height):
    puzzle_board = []
    file = open(puzzle_file_name, "r")

    for row in file:
        for line in row.split():
            puzzle_board.append(line)
            puzzle_height[0] += 1

    return puzzle_board

def result_list_gen(puzzle, puzzle_length, puzzle_height):
    temp_list = [['_' for col in range(puzzle_length)] for row in range(puzzle_height)]

    for row in range(puzzle_height):
        for col in range(puzzle_length):
            if puzzle[row][col] == '#':
                temp_list[row][col] = '#'

    return temp_list


def combining_results(v_res, h_res, puzzle_length, puzzle_height):
    for row in range(puzzle_height):
        for col in range(puzzle_length):
            if h_res[row][col] == '_':
                h_res[row][col] = v_res[row][col]

    return True

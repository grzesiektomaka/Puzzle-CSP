def vertical_variables(puzzle, puzzle_length, puzzle_height, v_word_length):
    v_var = [['#' for row in range(0, puzzle_length)] for col in range(0, puzzle_height[0])]

    word_counter = 0
    word_length = 0

    for col in range(puzzle_length):
        for row in range(puzzle_height[0]):
            if puzzle[row][col] == '_':
                if word_length > 1:
                    v_var[row][col] = [word_counter, word_length]
                    word_length += 1
                elif word_length == 1:
                    v_var[row - 1][col] = [word_counter, word_length - 1]
                    v_var[row][col] = [word_counter, word_length]
                    word_length += 1
                else:
                    word_length += 1
            elif word_length > 1:
                word_counter += 1
                v_word_length.append(word_length)
                word_length = 0
            else:
                word_length = 0

        if word_length > 1:
            word_counter += 1
            v_word_length.append(word_length)
            word_length = 0

    return v_var

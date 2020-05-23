
def horizontal_variables(puzzle, puzzle_length, puzzle_height, h_word_length):

    h_var = [['#' for row in range(0, puzzle_length)] for col in range(0, puzzle_height[0])]

    word_counter = 0
    word_length = 0


    for row in range(puzzle_height[0]):
        for col in range(puzzle_length):
            if puzzle[row][col] == '_':
                if word_length > 1:
                    h_var[row][col] = [word_counter, word_length]
                    word_length += 1
                elif word_length == 1:
                    h_var[row][col - 1] = [word_counter, word_length - 1]
                    h_var[row][col] = [word_counter, word_length]
                    word_length += 1
                else:
                    word_length += 1
            elif word_length > 1:
                word_counter += 1
                h_word_length.append(word_length)
                word_length = 0
            else:
                word_length = 0
        if word_length > 1:
            word_counter += 1
            h_word_length.append(word_length)
            word_length = 0


    return h_var

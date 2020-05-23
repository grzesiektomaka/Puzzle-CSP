import copy


def domains(words, puzzle_length, puzzle_height, h_word_length, v_word_length, h_domains, v_domains):
    if puzzle_height > puzzle_length:
        max_word_length = puzzle_height
    else:
        max_word_length = puzzle_length

    # general domains for specific length
    dm_list = [[] for word in range(max_word_length)]

    for word in words:
        word_length = len(word) - 1
        if word_length <= max_word_length:
            dm_list[word_length].append(word)

    for length in h_word_length:
        h_domains.append(copy.deepcopy(dm_list[length - 1]))

    for length in v_word_length:
        v_domains.append(copy.deepcopy(dm_list[length - 1]))


def update_all_domains(word, h_domains, v_domains):
    for domain_nr in range(len(h_domains)):
        if word in h_domains[domain_nr]:
            h_domains[domain_nr].remove(word)

    for domain_nr in range(len(v_domains)):
        if word in v_domains[domain_nr]:
            v_domains[domain_nr].remove(word)


def update_v_domain(h_res, row, v_var, v_domains, puzzle_length):
    for col in range(puzzle_length):
        if h_res[row][col] != '_':
            if v_var[row][col] != '#':
                v_var_nr = v_var[row][col][0]
                letter_nr = v_var[row][col][1]
                words_to_delete = []
                for word in v_domains[v_var_nr]:
                    if word[letter_nr] != h_res[row][col]:
                        words_to_delete.append(word)
                for word in words_to_delete:
                    v_domains[v_var_nr].remove(word)


def update_h_domain(v_res, col, puzzle_height, h_var, h_domains):
    for row in range(puzzle_height):
        if v_res[row][col] != '_':
            if h_var[row][col] != '#':
                h_var_nr = h_var[row][col][0]
                letter_nr = h_var[row][col][1]
                words_to_delete = []
                for word in h_domains[h_var_nr]:
                    if word[letter_nr] != v_res[row][col]:
                        words_to_delete.append(word)
                for word in words_to_delete:
                    h_domains[h_var_nr].remove(word)


def filled_domain_list(r):
    fill_list = []
    for i in range(r):
        fill_list.append(i)

    return fill_list

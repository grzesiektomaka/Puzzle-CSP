from domains import *
from result_list_gen import combining_results
from forward_checking import forward_checking


def backtracking_s(h_res, v_res, h_var, v_var, h_domains, v_domains, puzzle_length, puzzle_height, expanded_nodes,
                   h_to_fill, v_to_fill, ver):
    position = [0, 0]
    switcher = [0]

    if not find_unassigned(h_res, v_res, h_var, v_var, position, puzzle_length, puzzle_height, switcher):
        print('SOLUTION')
        combining_results(v_res, h_res, puzzle_length, puzzle_height)
        for row in h_res:
            print(row)
        print('Expanded nodes: ')
        print(expanded_nodes[0])
        return True

    expanded_nodes[0] += 1
    u_row = position[0]
    u_col = position[1]

    if switcher[0] == 'h':

        word_nr = h_var[u_row][u_col][0]

        h_domains_cpy = copy.deepcopy(h_domains)
        v_domains_cpy = copy.deepcopy(v_domains)

        for word in h_domains_cpy[word_nr]:
            h_to_fill.remove(word_nr)
            for i in range(len(word)):
                h_res[u_row][u_col + i] = word[i]

            update_all_domains(word, h_domains, v_domains)
            update_v_domain(h_res, u_row, v_var, v_domains, puzzle_length)

            if ver == 'fc':
                if forward_checking(h_domains, v_domains, h_to_fill, v_to_fill):
                    if backtracking_s(h_res, v_res, h_var, v_var, h_domains, v_domains, puzzle_length, puzzle_height,
                                      expanded_nodes, h_to_fill, v_to_fill, ver):
                        return True
            else:
                if backtracking_s(h_res, v_res, h_var, v_var, h_domains, v_domains, puzzle_length, puzzle_height,
                                  expanded_nodes, h_to_fill, v_to_fill, ver):
                    return True


            h_domains = copy.deepcopy(h_domains_cpy)
            v_domains = copy.deepcopy(v_domains_cpy)
            h_to_fill.append(word_nr)
            for i in range(len(word)):
                h_res[u_row][u_col + i] = '_'

    if switcher[0] == 'v':

        word_nr = v_var[u_row][u_col][0]

        h_domains_cpy = copy.deepcopy(h_domains)
        v_domains_cpy = copy.deepcopy(v_domains)


        for word in v_domains_cpy[word_nr]:
            v_to_fill.remove(word_nr)
            for i in range(len(word)):
                v_res[u_row + i][u_col] = word[i]

            update_all_domains(word, h_domains, v_domains)
            update_h_domain(v_res, u_col, puzzle_height, h_var, h_domains)

            if ver == 'fc':
                if forward_checking(h_domains, v_domains, h_to_fill, v_to_fill):
                    if backtracking_s(h_res, v_res, h_var, v_var, h_domains, v_domains, puzzle_length, puzzle_height,
                                      expanded_nodes, h_to_fill, v_to_fill, ver):
                        return True
            else:
                if backtracking_s(h_res, v_res, h_var, v_var, h_domains, v_domains, puzzle_length, puzzle_height,
                                  expanded_nodes, h_to_fill, v_to_fill, ver):
                    return True

            h_domains = copy.deepcopy(h_domains_cpy)
            v_domains = copy.deepcopy(v_domains_cpy)
            v_to_fill.append(word_nr)
            for i in range(len(word)):
                v_res[u_row + i][u_col] = '_'

    return False


def find_unassigned(h_res, v_res, h_var, v_var, position, puzzle_length, puzzle_height, switcher):
    for row in range(puzzle_height):
        for col in range(puzzle_length):
            if h_res[row][col] == '_' and h_var[row][col] != '#':
                position[0] = row
                position[1] = col
                switcher[0] = 'h'
                return True

            if v_res[row][col] == '_' and v_var[row][col] != '#':
                position[0] = row
                position[1] = col
                switcher[0] = 'v'
                return True

    return False

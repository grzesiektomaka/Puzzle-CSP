import timeit
from read_puzzle import read_puzzle
from read_words import read_words
from horizontal_variables import horizontal_variables
from vertical_variables import vertical_variables
from domains import *
from result_list_gen import *
from backtracking_s import backtracking_s


def main():

    SETUP_CODE = '''
import copy
from read_puzzle import read_puzzle
from read_words import read_words
from horizontal_variables import horizontal_variables
from vertical_variables import vertical_variables
from domains import domains
from domains import filled_domain_list
from result_list_gen import result_list_gen
from backtracking_s import backtracking_s

puzzle_height = [0]
puzzle = read_puzzle('./data/puzzle4.txt', puzzle_height)
words = read_words('./data/words4.txt')

puzzle_length = len(puzzle[0])
h_word_length = []
v_word_length = []
h_domains = []
v_domains=[]
expanded_nodes=[0]

h_var = horizontal_variables(puzzle, puzzle_length, puzzle_height, h_word_length)
v_var = vertical_variables(puzzle, puzzle_length, puzzle_height, v_word_length)
domains(words, puzzle_length, puzzle_height[0], h_word_length, v_word_length, h_domains, v_domains)

h_to_fill = filled_domain_list(len(h_domains))
v_to_fill = filled_domain_list(len(v_domains))
h_res=copy.deepcopy(result_list_gen(puzzle, puzzle_length, puzzle_height[0]))
v_res=copy.deepcopy(h_res)

print('WORDS')
print(words)

print('PUZZLE')
for row in puzzle:
    print(row)
        '''

    BACKTRACKING = '''backtracking_s(h_res, v_res, h_var, v_var, h_domains, v_domains, puzzle_length, puzzle_height[
    0], expanded_nodes, h_to_fill, v_to_fill, 'fc') '''

    print('BACKTRACKING')
    backtracking = timeit.timeit(setup=SETUP_CODE, stmt=BACKTRACKING, number=1)
    print('Time: ')
    print(backtracking)

main()

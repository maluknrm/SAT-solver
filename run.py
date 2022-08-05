from copy import copy
from converter import Converter
from sat_solver import SAT
from functools import reduce
import copy


if __name__ == "__main__":

    # save files
    FILE_RULES = "sudoku-rules-4x4.txt"
    FILE_SUDOKU = "4x4.txt"
    DIM = 4

    # convert sudokus into readable form and rules into cnfs
    converter = Converter(dim=DIM)
    sudokus = converter.reading_sudoku(FILE_SUDOKU)
    rules = converter.reading_rules(f=FILE_RULES)

    # set one sudoku and put it and the rules into the sat solver
    sudoku = sudokus[0]
    solution = set(sudoku)
    sat = SAT(solution=solution, all_clauses=rules)


    # simplify => only unit clause because tautology and pure literal not applicable with sudokus
    sat.unit_clause()

    # set sudoku numbers to true
    for num in sudoku:
        sat.reduction(literal=num)
    # simplify again
    sat.unit_clause()

    # split first literal
    literal_to_split = sat.max_literal()

    # do the dpll algorithm, print sudoku solution
    if sat.dpll_alg(literal_to_split) == True:
        sol = [element for element in list(sat.solution) if element > 0]
        print(f"SAT solution: {sorted(sol)}")
    elif sat.dpll_alg(literal_to_split) == False:
        print(f"no SAT solution")




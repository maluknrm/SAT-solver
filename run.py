from converter import Sudoku_Converter
from converter import Rule_Converter
from sat_solver import SAT

FILE_RULES = "sudoku-rules-4x4.txt"
FILE_SUDOKU = "4x4.txt"
DIM = 4

sudoku_converter = Sudoku_Converter(dimension_sudoku=DIM)
rule_converter = Rule_Converter()


if __name__ == "__main__":

    # save files
    FILE_RULES = "sudoku-rules-4x4.txt"
    FILE_SUDOKU = "4x4.txt"
    DIM = 4

    # convert sudokus into readable form and rules into cnfs
    sudoku_converter = Sudoku_Converter(dimension_sudoku=DIM)
    rule_converter = Rule_Converter()
    sudokus = sudoku_converter.convert_sudokus(file_sudoku=FILE_SUDOKU)
    rules = rule_converter.convert_rules(file_rules=FILE_RULES)

    # set one sudoku and put it and the rules into the sat solver
    sudoku = sudokus[0]
    solution = set(sudoku)
    sat = SAT(solution=solution, all_clauses=rules)


    # simplify => only unit clause because tautology and pure literal not applicable with sudokus
    sat.simplify_with_unit_clause()

    # set sudoku numbers to true
    for solution_number in sudoku:
        sat.reduce_clauses(literal=solution_number)

    # simplify again
    sat.simplify_with_unit_clause()

    # split first literal
    to_split_literal = sat.most_frequent_literal()

    # do the dpll algorithm, print sudoku solution
    if sat.dpll_algorithm(to_split_literal=to_split_literal) == True:
        solution_sudoku = [element for element in list(sat.solution) if element > 0]
        print(f"SAT solution: {sorted(solution_sudoku)}")
    elif sat.dpll_algorithm(to_split_literal=to_split_literal) == False:
        print(f"no SAT solution")






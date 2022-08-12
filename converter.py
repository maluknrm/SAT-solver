class Sudoku_Converter:
    def __init__(self, dimension_sudoku:int):
        self.dimension_sudoku = dimension_sudoku

    def convert_sudokus(self, file_sudoku:str) -> list:
        with open(file_sudoku, "r") as file:
            several_sudokus = file.read().split("\n")
            final_sudokus = []
            for one_sudoku in several_sudokus:
                one_sudoku_formated = Sudoku_Converter.append_formated_sudoku(self, sudoku=one_sudoku)
                final_sudokus.append(one_sudoku_formated)
            return final_sudokus

    def append_formated_sudoku(self, sudoku):
        numbers_one_sudoku = []
        for i in range(len(sudoku)):
            if sudoku[i].isdigit():
                row_number = int(i/self.dimension_sudoku)+1
                column_number = int(i%self.dimension_sudoku+1)
                complete_formated_number = int(str(row_number) + str(column_number) + sudoku[i])
                numbers_one_sudoku.append(complete_formated_number)
        return numbers_one_sudoku

class Rule_Converter:
    def convert_rules(self, file_rules:str)->list:
        file_rules = open(file_rules,"r")
        lines_rules = file_rules.readlines()
        rules = Rule_Converter.append_formated_rules(self, lines_rules=lines_rules)
        return rules
        
    def append_formated_rules(self, lines_rules:list)->list:
        rules = []
        for i in range(1, len(lines_rules)):
            line = [int(number) for number in lines_rules[i].replace("0\n", "").split()]
            rules.append(line)
        return rules


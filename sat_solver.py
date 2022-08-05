from itertools import count
from functools import reduce


class SAT:
    def __init__(self, solution, all_clauses):
        self.solution = solution
        self.all_clauses = all_clauses

    # running the algorithm

    # solved clause => literal is true
    def solved_clause(self, literal):
        self.all_clauses = [element for element in self.all_clauses if literal not in element]
        #return self.all_clauses

    # literal is false
    def solved_literal(self, literal):
        solved_literals = []
        for clause in self.all_clauses:
            if literal in clause:
                clause.remove(literal)
            solved_literals.append(clause)
            self.all_clauses = solved_literals


    def reduction(self, literal):
        SAT.solved_clause(self, literal)
        if self.all_clauses == True:
            return True
        SAT.solved_literal(self, -literal)
        if self.all_clauses == False:
            return False

    # Simplification rules

    # returns list with potential unit clauses
    # if there is a unit clause the literal can be set to true
    def unit_clause(self):
        unit_clauses = [clause for clause in self.all_clauses if len(clause) == 1]
        if unit_clauses:
            unit_clauses = reduce(lambda x, y: x + y, unit_clauses)
            for literal in unit_clauses:
                self.solution.add(literal)
                SAT.solved_clause(self, literal)
                SAT.solved_literal(self, -literal)

    # loop reversed through whole list and check sublists with tautology => if True remove clause
    def check_tautology(sub_lst):
        for literal in sub_lst:
            if literal < 0 and abs(literal) in sub_lst:
                return True

    def remove_tautology(self):
        for clause in reversed(self.all_clauses):
            if SAT.check_tautology(clause) == True:
                self.all_clauses = self.all_clauses.remove(clause)

    def check_pure_literal(self):
        flat_all_clauses = list(set(reduce(lambda x, y: x + y, self.all_clauses)))
        pure_literals = [literal for literal in flat_all_clauses if -literal not in flat_all_clauses]
        return pure_literals

    def remove_pure_literal(self):
        pure_literals = SAT.check_pure_literal(self)
        if pure_literals:
            for literal in pure_literals:
                SAT.solved_clause(self, literal)
                SAT.solved_literal(self, -literal)

    # check if solved or not
    def check(self):
        if len(self.all_clauses) == 0:
            return True
        lengths = [len(sublist) for sublist in self.all_clauses]
        if 0 in lengths:
            return False

    # frequency heuristic for splitting
    def _most_common(lst):
        return max(set(lst), key=lst.count)

    def max_literal(self):
        frequent_literal = SAT._most_common(reduce(lambda x, y: x + y, self.all_clauses))
        return frequent_literal

    def dpll_alg(self, literal_to_split):

        self.solution.add(literal_to_split)
        SAT.unit_clause(self)
        SAT.reduction(self, literal=literal_to_split)

        if SAT.check(self) == True:
            return True
        if SAT.check(self) == False:
            return False

        SAT.unit_clause(self)

        if self.all_clauses:
            literal_to_split = SAT.max_literal(self)
        else:
            return True

        if SAT.dpll_alg(self, -literal_to_split) == True:
            return True

        return SAT.dpll_alg(self, literal_to_split)







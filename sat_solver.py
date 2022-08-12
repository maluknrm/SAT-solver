from functools import reduce

class SAT:
    def __init__(self, solution, all_clauses):
        self.solution = solution
        self.all_clauses = all_clauses

    # simplification rules tautology, pure literal, unit clause
    def simplify_with_tautology(self):
        for clause in reversed(self.all_clauses):
            if SAT.check_existence_tautology(clause=clause) == True:
                self.all_clauses = self.all_clauses.remove(clause)

    def check_existence_tautology(clause:list):
        for literal in clause:
            if literal < 0 and abs(literal) in clause:
                return True

    def simplify_with_pure_literal(self):
        pure_literals = SAT.check_existence_pure_literal(self)
        if pure_literals:
            for literal in pure_literals:
                SAT.reduce_clauses(self, literal)
        
    def check_existence_pure_literal(self):
        flat_all_clauses = list(reduce(lambda x, y: x + y, self.all_clauses))
        pure_literals = [literal for literal in flat_all_clauses if -literal not in flat_all_clauses]
        return pure_literals

    def simplify_with_unit_clause(self):
        unit_clauses = [clause for clause in self.all_clauses if len(clause) == 1]
        if unit_clauses:
            SAT.reduce_unit_clause_literals(self, unit_clauses=unit_clauses)
    
    def reduce_unit_clause_literals(self, unit_clauses:list):
        unit_clause_literals = reduce(lambda x, y: x + y, unit_clauses)
        for literal in unit_clause_literals:
            self.solution.add(literal)
            SAT.reduce_clauses(self, literal=literal)

    # reducing the clauses by setting literals to true and reducing the clauses and setting negative literal to false and delete negative literal out of clauses

    def reduce_clauses(self, literal:int):
        SAT.set_literal_true(self, literal)
        SAT.set_literal_false(self, -literal)

    def set_literal_true(self, true_literal:int):
        self.all_clauses = [element for element in self.all_clauses if true_literal not in element]

    def set_literal_false(self, false_literal:int):
        for clause in self.all_clauses:
            if false_literal in clause:
                clause.remove(false_literal)

    # running dpll algorithm
    def dpll_algorithm(self, to_split_literal:int):
        self.solution.add(to_split_literal)
        SAT.simplify_with_unit_clause(self)
        SAT.reduce_clauses(self, literal=to_split_literal)

        if SAT.check_if_solved(self) == True:
            return True
        if SAT.check_if_solved(self) == False:
            return False

        SAT.simplify_with_unit_clause(self)
        if self.all_clauses:
            to_split_literal = SAT.most_frequent_literal(self)
        else:
            return True

        if SAT.dpll_alg(self, to_split_literal=-to_split_literal) == True:
            return True

        return SAT.dpll_alg(self, to_split_literal=to_split_literal)

    # check if solved or not
    def check_if_solved(self):
        if len(self.all_clauses) == 0:
            return True
        lengths = [len(sublist) for sublist in self.all_clauses]
        if 0 in lengths:
            return False

# frequency heuristic for splitting
    def most_frequent_literal(self):
        frequent_literal = SAT._most_common(reduce(lambda x, y: x + y, self.all_clauses))
        return frequent_literal

    def _most_common(list_literals:list):
        return max(set(list_literals), key=list_literals.count)




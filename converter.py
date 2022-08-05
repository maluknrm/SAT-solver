class Converter:
    def __init__(self, dim):
        self.dim = dim


# helperfunctions to make each sudoku string into an integer list with the correct position
    def sudoku_formate(self, idx, element, lst):
        for i in range(1,self.dim+1):
            if (idx+1)/self.dim <= i:
                if (idx+1)%self.dim != 0:
                    lst.append(int(str(i) + str((idx+1)%self.dim) + element))
                else:
                    lst.append(int(str(i) + str(self.dim) + element))
                break
        return lst

    
    def reading_sudoku(self, f):
        f = open(f, "r")
        lines = []
        for line in f.readlines():
            lst = []
            line = line.replace("\n", "")
            for idx,element in enumerate(line):
                if element.isdigit():
                    line = Converter.sudoku_formate(self, idx, element, lst)
            lines.append(line)

        return lines

    def reading_rules(self, f):
        f = open(f,"r")
        rules = []
        lines = f.readlines()

        for i in range(1, len(lines)):
            line = [int(element) for element in lines[i].replace("0\n", "").split()]
            rules.append(line)
        
        return rules


    
class Grammar:
    def __init__(self, file_name):
        file = open(file_name, "r")

        self.start = file.readline().split()[0]
        self.terminals = file.readline().split()
        self.nonterminals = file.readline().split()

        self.production_rules = []
        
        for line in file.readlines():
            line = line.split()
            st = line[0]
            # jump over ->
            dr = line[2:]
            self.production_rules.append((st, dr))


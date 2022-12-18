from grammar import Grammar

EPSILON = "epsilon"

class FirstFollowTable:
    def __init__(self, grammar: Grammar):
        self.first = {}
        self.follow = {}
        self.grammar = grammar
        for el in grammar.nonterminals:
            self.first[el] = set()
            self.follow[el] = set()
        
        self.generate_first()
        self.generate_follow()

        # to do: beautify print
        print("FIRST1")
        for el in self.first:
            print(el + ":" + str(self.first[el]))
        print()
        # to do: beautify print
        print("FOLLOW1")
        for el in self.follow:
            print(el + ":" + str(self.follow[el]))

    def generate_follow(self):
        
        self.follow[self.grammar.start].add('$')

        ok = True
        while ok:
            ok = False
            for el in self.grammar.production_rules:
                for index, symbol in enumerate(el[1]):
                    if symbol in self.grammar.terminals or symbol == EPSILON:
                        continue
                    ok_epsilon = False
                    if index < len(el[1]) - 1: # Radu copyright

                        for terminal in self.first[el[1][index + 1]]:
                            if terminal == EPSILON:
                                ok_epsilon = True
                            else:
                                if terminal not in self.follow[symbol]:
                                    self.follow[symbol].add(terminal)
                                    ok = True
                    
                        if ok_epsilon == True:
                            for terminal in self.follow[el[0]]:
                                if terminal not in self.follow[symbol]:
                                    self.follow[symbol].add(terminal)
                                    ok = True
                    else:
                        # A -> B C, for C we have epsilon
                        for terminal in self.follow[el[0]]:
                            if terminal not in self.follow[symbol]:
                                self.follow[symbol].add(terminal)
                                ok = True

    
    def generate_first(self):
        for terminal in self.grammar.terminals:
            self.first[terminal] = set()
            self.first[terminal].add(terminal)

        ok = True
        while ok:
            ok = False
            for el in self.grammar.production_rules:
                ok_epsilon = False

                for symbol in el[1]:
                    ok_epsilon = False

                    if symbol in self.grammar.terminals:
                        if symbol not in self.first[el[0]]:
                            self.first[el[0]].add(symbol)
                            ok = True
                    elif symbol == EPSILON:
                        if symbol not in self.first[el[0]]:
                            self.first[el[0]].add(symbol)
                            ok = True
                    else:
                        # print(str(el[0]) + " " + symbol + " " + str(self.first[symbol]))
                        for t in self.first[symbol]:
                            if t == EPSILON:
                                ok_epsilon = True
                            elif t not in self.first[el[0]]:
                                self.first[el[0]].add(t)
                                ok = True             
                
                    if ok_epsilon == False:
                        break
                
                if ok_epsilon == True:
                    if EPSILON not in self.first[el[0]]:
                        self.first[el[0]].add(EPSILON)
                        ok = True

    def get_all_first(self, alpha):
        arr = set()
        for symbol in alpha:
            
            if EPSILON in arr:
                arr.remove(EPSILON)

            if symbol == EPSILON:
                arr.add(symbol)
            else:
                for el in self.first[symbol]:
                    arr.add(el)
                if EPSILON not in self.first[symbol]:
                    break


        return arr

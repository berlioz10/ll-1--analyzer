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
        self.generate_follow() # : D

    def generate_follow(self):
        ok = True
        while ok:
            break
    
    def generate_first(self):
        
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

g = Grammar("grammar.txt")
r = FirstFollowTable(g)
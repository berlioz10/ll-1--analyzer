from first_follow import FirstFollowTable
import pandas as pd

EPSILON = "epsilon"

class LL1:
    def __init__(self, fft: FirstFollowTable):
        self.fft = fft
        self.grammar = self.fft.grammar

    def verify(self):
        for index, prod1 in enumerate(self.grammar.production_rules):
            if index < len(self.grammar.production_rules) - 1:
                for prod2 in self.grammar.production_rules[index + 1:]:
                    if prod1[0] == prod2[0]:
                        first1 = self.fft.get_all_first(prod1[1])
                        first2 = self.fft.get_all_first(prod2[1])

                        if not first1.isdisjoint(first2):
                            # print(str(prod1) + " " + str(prod2) + " " + str(first1) + " " + str(first2))
                            return False

                        if EPSILON in first1:
                            first1 = self.fft.follow[prod1[0]]

                        if EPSILON in first2:
                            first2 = self.fft.follow[prod1[0]]

                        if not first1.isdisjoint(first2):
                            # print(str(prod1) + ":" + str(prod2) + ":" + str(first1) + ":" + str(first2))
                            return False

        return True

    def create_table(self):
        table = {}

        for symbol in self.grammar.nonterminals:
            for terminal in self.grammar.terminals + ["$"]:
                for index, prod in enumerate(self.grammar.production_rules):
                    if prod[0] == symbol:
                        firstalpha = self.fft.get_all_first(prod[1])
                        if terminal in firstalpha:
                            table[prod[0], terminal] = (prod[1], index)
                        else:
                            if EPSILON in firstalpha and terminal in self.fft.follow[symbol]:
                                table[prod[0], terminal] = (prod[1], index)

        for symbol in self.grammar.terminals:
            table[symbol, symbol] = "pop"

        table["$", "$"] = "acc"
        
        # a beautiful print :D
        new_table = {}
        for pair in table:
            new_table[pair[1]] = {}

        for pair in table:
            new_table[pair[1]][pair[0]] = table[pair]
        


        pd.DataFrame(new_table).fillna('err').to_csv("table_ll1.csv")
        return table

    def parse_string(self, string):
        # to do
        None


from first_follow import FirstFollowTable
from grammar import Grammar
from ll1 import LL1

if __name__ == '__main__':
    g = Grammar("grammar.txt")
    fft = FirstFollowTable(g)
    ll1 = LL1(fft)

    if ll1.verify():
        table = ll1.create_table()
    else:
        print("stoopid code")
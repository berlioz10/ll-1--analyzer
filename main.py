from first_follow import FirstFollowTable
from grammar import Grammar


if __name__ == '__main__':
    g = Grammar("grammar.txt")
    r = FirstFollowTable(g)
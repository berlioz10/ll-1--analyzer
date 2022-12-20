from first_follow import FirstFollowTable
from grammar import Grammar
from ll1 import LL1

if __name__ == '__main__':
    ok_ll1 = True
    
    g = Grammar("grammar.txt")
    fft = FirstFollowTable(g)
    ll1 = LL1(fft)
    ll1.create_table()
    while True:
        inp = input('''
        1. Put a new file grammar
        2. Put a string to parse
        >> ''')
        if inp == "1":
            g = Grammar("grammar.txt")
            fft = FirstFollowTable(g)
            ll1 = LL1(fft)

            ok_ll1 = ll1.verify()
            if ok_ll1 == True:
                table = ll1.create_table()
                print("The grammar is ok for ll1! Check table_ll1.csv to see the table")
            else:
                print("Error: looks like we have some conflicts there")
        else:
            if ok_ll1 == False:
                print("You did not put a valid grammar yet")
            else:
                inp = input("put a string: ")
                inp = ['var', 'identifier', ';', 'identifier', ';', 
                'begin', 
                'read', '(', 'identifier', ')', ';',
                'write', '(', 'identifier', ')', ';',
                'end']
                ok, output_band = ll1.parse_string(inp)
                print(ok)
                print(output_band)
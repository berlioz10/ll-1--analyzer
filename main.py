from first_follow import FirstFollowTable
from grammar import Grammar
from ll1 import LL1

def print_production_rules(indexes, g: Grammar):
    print('''
            You can obtain the input string by using the following rules:''')
    for idx, rule_index in enumerate(indexes):
        print(f'''        {idx + 1}. {g.rule_to_string(g.production_rules[rule_index])}''')

def run():
    ok_ll1 = True
    
    g = Grammar("grammar.txt")
    fft = FirstFollowTable(g)
    ll1 = LL1(fft)
    ll1.create_table()

    while True:
        inp = input('''
        1. Put a new file grammar
        2. Put a string to parse
        3. Put your funny fip file ( do not forget to load the language grammar file)
        4 or any letter. Exit
        >> ''')
        if inp == "1":
            grammar_file = input('''
        Please input a grammar file: 
        >> ''')

            g = Grammar(grammar_file)
            fft = FirstFollowTable(g)
            ll1 = LL1(fft)

            ok_ll1 = ll1.verify()
            if ok_ll1 == True:
                table = ll1.create_table()
                print('''
            The grammar is ok for ll1! Check table_ll1.csv to see the table''')
            else:
                print('''
            Error: looks like we have some conflicts there''')
        elif inp == "2":
            if ok_ll1 == False:
                print('''\n
            You did not put a valid grammar yet''')
            else:
                input_string = input('''
        Please input a string to be checked
        >> ''').split()
                # input_string = ['var', 'identifier', ';', 'identifier', ';', 
                # 'begin', 
                # 'read', '(', 'identifier', ')', ';',
                # 'write', '(', 'identifier', ')', ';',
                # 'end']
                ok, output_band = ll1.parse_string(input_string)

                if ok:
                    print('''
            Yoo-hoo! The input string is correct.''')
                    print_production_rules(output_band, g)
                    # print(output_band)
                else:
                    print('''
            Oh no! Looks like you can do better and pick a correct string.''')
        elif inp == "3":


            inp = input("Load your FIP file:")
            fip_array = []
            fip_file = open(inp)
            for line in fip_file.readlines():
                line = line.split()
                if line[1].isnumeric():
                    fip_array += list(line[-1])
                else:
                    fip_array.append(line[-1])
            
            ok, output_band = ll1.parse_string(fip_array)

            if ok:
                print('''
        Yoo-hoo! The fip is correct with C++ grammar💪.''')
                print_production_rules(output_band, g)
                # print(output_band)
            else:
                print('''
        Oh no! Looks like you can do better and pick a correct string.''')
        else: 
            return

if __name__ == '__main__':
    run()
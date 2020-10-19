# Submitter: abathole(Bathole, Archita)
# Partner  : jensenak(Jensen, Alexis)
# We certify that we worked cooperatively on this programming
# assignment, according to the rules for pair programming

import goody
import prompt

def read_fa(file : open) -> {str:{str:str}}:
    line_list = [line.rstrip('\n') for line in file] 
    d = {}
    for l in line_list:
        new_list = l.split(';')
        key = new_list.pop(0)
        t_list = list(zip([x for x in new_list if new_list.index(x) % 2 == 0],[x for x in new_list if new_list.index(x) % 2 != 0]))
        d[key] = {k:v for (k,v) in t_list}        
    return d

def fa_as_str(fa : {str:{str:str}}) -> str:
    for k,v in fa.items():
        sort_fa = sorted([(k,(num,word)) for k,v in fa.items() for num,word in v.items()],  key = lambda x: x[1][0])
    s = ''
    for k in sorted(fa.keys()):
        s += "  " + str(k) +" transitions: [" 
        for key in sort_fa:
            if key[0] == k:
                s += str(key[1]) + ", "
        s = s[:-2]
        s += "]\n"
    return s
    
def process(fa : {str:{str:str}}, state : str, inputs : [str]) -> [None]:
    l = [state]
    for s in inputs:
        if s in fa[state]: 
            l.append((s,fa[state][s]))
            state = fa[state][s]
        else:
            l.append((s,None))
    return l

def interpret(fa_result : [None]) -> str:
    s = "Start state = " + str(fa_result[0]) + "\n"
    for l in fa_result[1:]:
        if l[1] == None:
            s += "  Input = " + str(l[0]) + "; illegal input: simulation terminated\n"
        else:
            s += "  Input = " + str(l[0]) + "; new state = " + str(l[1]) + "\n"
    s += "Stop state = " + str(fa_result[(len(fa_result) - 1)][1]) + "\n"
    return s



if __name__ == '__main__':
    # Write script here
    '''
    f1 = prompt.for_string("Select the file name encoding the Finite Automaton")
    f1_lines = read_fa(open(f1))
    print('The Description of the file selected for the Finite Automaton ')
    print(fa_as_str(f1_lines))
    f2 = prompt.for_string("Select the file name encoding a sequence of start-states and all their inputs")
    f2_list = [line.rstrip('\n').split(';') for line in open(f2)]
    for line in f2_list:
        print("\nBegin tracing the current FA in the selected start-state\n" + interpret(process(f1_lines,line.pop(0),line)))
    '''
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bscp13S19.txt"
    driver.default_show_traceback = True
    driver.default_show_exception = True
    driver.default_show_exception_message = True
    driver.driver()
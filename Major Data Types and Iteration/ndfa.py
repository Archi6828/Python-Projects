# Submitter: abathole(Bathole, Archita)
# Partner  : jensenak(Jensen, Alexis)
# We certify that we worked cooperatively on this programming
# assignment, according to the rules for pair programming

import goody
from collections import defaultdict
import prompt

def read_ndfa(file : open) -> {str:{str:{str}}}:
    line_list = [line.rstrip('\n') for line in file] 
    print(str(file))
    d = {}
    t_list = []
    for l in line_list:
        new_list = l.split(';')
        key = new_list.pop(0)
        t_list = list(zip([x for x in new_list if new_list.index(x) % 2 == 0],[x for x in new_list if new_list.index(x) % 2 != 0]))
        d[key] = {}
        for (k,v) in t_list:
            if k in d[key]:
                d[key][k].add(v)
            else:
                d[key][k] = {v}       
    return d


def ndfa_as_str(ndfa : {str:{str:{str}}}) -> str:
    for k,v in ndfa.items():
        sort_ndfa = sorted([(k,(num,sorted(list(word)))) for k,v in ndfa.items() for num,word in v.items()],  key = lambda x: x[1][0])   
    s = ''
    s_l = []
    for k in sorted(ndfa.keys()):
        s += "  " + str(k) +" transitions: [" 
        if ndfa[k]:
            for key in sort_ndfa:
                if key[0] == k:
                    s += str(key[1]) + ", "
        else: 
            s += ", "
        s = s[:-2]
        s += "]\n"
    return s
       
def process(ndfa : {str:{str:{str}}}, state : str, inputs : [str]) -> [None]:
    org = state
    l = [state]
    counter_d = {}
    counter_s = 0
    for s in inputs:
        # track of repeating ints
        if s not in counter_d:
            counter_d[s] = 1
        else:
            counter_d[s] += 1
        try:   
            if s in ndfa[state]:
                inner_values = ndfa[state][s]
            
                if counter_d[s] == 1:
                    l.append((s,inner_values))
                
                    for word in sorted(list(inner_values)):
                        if word != state and ndfa[word]:
                            state = word
                            max = len(inner_values)
                            if len(inner_values) > 1:
                                counter_s += 1
                            break
                elif state == org:
                    l.append((s,inner_values)) 
                    for word in sorted(list(inner_values)):
                        if word != state and ndfa[word]:
                            state = word
                            max = len(inner_values)
                            if len(inner_values) > 1:
                                counter_s += 1
                            break
                else:
                    new_values = []
                    for input in l:
                        if input[0] == s:
                            new_values = [v for v in input[1]]
                    for v in inner_values:
                        new_values.append(v)
                    new_values = sorted(new_values)
                    l.append((s,set(new_values)))
                
                    for word in sorted(list(new_values)):
                        if word != state and ndfa[word]:
                            state = word
                            max = len(set(new_values))
                            if len(new_values) > 1:
                                counter_s += 1
                            break          
            else:
                #if counter_d[s] == 1:
                    
                if counter_s != max:
                    l.append((s,inner_values)) 
                    for word in sorted(list(inner_values)):
                        if word != state and ndfa[word]:
                            state = word
                            break
                else:
                    l.append((s,set()))
                    counter_s = 0
                    return l
                    
        except:
            pass
    return l
    '''
    l = [state]
    print(str(ndfa))
    for s in inputs:
        try:
            if s in ndfa[state]:
                t = ndfa[state][s]
                
                # check if s is in List
                for num in l:
                    if s == num[0]:
                        new_set = num[1].copy()
                        for w in t:
                            new_set.add(w)
                        l.append((s,new_set))  
                    break
                # else append it           
                    else:
                        l.append((s,t))
                    
                if len(ndfa[state][s]) == 1:
                    state = str(next(iter(ndfa[state][s])))
                else:
                    first_l = list(ndfa[state][s])
                    state = str(first_l[0])
            else:
                return l
        except: 
            pass
    return l
    '''

def interpret(result : [None]) -> str:
    s = "Start state = " + str(result[0]) + "\n"
    for l in result[1:]:
        s += "  Input = " + str(l[0]) + "; new possible states = " + str(sorted(list(l[1]))) + "\n"
    s += "Stop state(s) = " + str(sorted(list(result[(len(result) - 1)][1]))) + "\n"
    return s


if __name__ == '__main__':
    '''
    # Write script here
    f1 = prompt.for_string("Select the file name encoding the Non-Deterministic Finite Automaton")
    f1_lines = read_ndfa(open(f1))
    print('The Description of the file selected for the Non-Deterministic Finite Automaton')
    print(ndfa_as_str(f1_lines))
    f2 = prompt.for_string("Choose the file name representing the start-states and their inputs")
    f2_list = [line.rstrip('\n').split(';') for line in open(f2)]
    for line in f2_list:
        print("\nBegin tracing the current NDFA in the selected start-state\n" + interpret(process(f1_lines,line.pop(0),line)))
    '''
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bscp14S19.txt"
    driver.default_show_traceback = True
    driver.default_show_exception = True
    driver.default_show_exception_message = True
    driver.driver()
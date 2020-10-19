# Submitter: abathole(Bathole, Archita)
# Partner  : jensenak(Jensen, Alexis)
# We certify that we worked cooperatively on this programming
# assignment, according to the rules for pair programming

import prompt
from goody import irange

# Use these global variables to index the list associated with each name in the dictionary.
# e.g., if men is a dictionary, men['m1'][match] is the woman who matches man 'm1', and 
# men['m1'][prefs] is the list of preference for man 'm1'.
# It would seems that this list might be better represented as a named tuple, but the
# preference list it contains is mutated, which is not allowed in a named tuple. 

match = 0   # Index 0 of list associate with name is match (str)
prefs = 1   # Index 1 of list associate with name is preferences (list of str)


def read_match_preferences(open_file : open) -> {str:[str,[str]]}:
    line_list = [line.rstrip('\n') for line in open_file] 
    m_dict = {}
    for l in line_list:
        matches = []
        for x in range(1,len(l.split(';'))):
            matches.append(l.split(';')[x])
        m_dict[l.split(';')[0]] = [None ,matches]
    return m_dict


def dict_as_str(d : {str:[str,[str]]}, key : callable=None, reverse : bool=False) -> str:
    o_dict = sorted(d, key = key, reverse = reverse)
    s = ''
    for k in o_dict:
        if k in d:
            s += "  " + str(k) + " -> " + str(d[k]) + '\n'
    return s


def who_prefer(order : [str], p1 : str, p2 : str) -> str:
    return order[min([order.index(p1), order.index(p2)])]
        


def extract_matches(men : {str:[str,[str]]}) -> {(str,str)}:
    return {(key,value[0]) for (key,value) in men.items() }


def make_match(men : {str:[str,[str]]}, women : {str:[str,[str]]}, trace : bool = False) -> {(str,str)}:
    men_copy = men.copy()# copy of men dict   
    unmatched = set(men_copy.keys())
    match = set()
    message = ''
    if trace:
        print("Women Preferences (unchanging)\n" + str(dict_as_str(women)))
    while unmatched:
        if trace:
            print( message + "\nMen Preferences (current)\n" + str(dict_as_str(men_copy)) + "\nunmatched men = " + str(unmatched))
        m = unmatched.pop()
        w = men_copy[m][1].pop(0)
        for man,p in men_copy.items():
            if w == p[0]:  
                current = man 
                if who_prefer(women[w][1], m,current) == m:
                    message = "\n" + str(m) + " proposes to "+str(w)+ " who is matched, ergo she accepts the proposal (liking her new match better)\n"
                    unmatched.add(current)    
                    match.remove((current,w))   # remove old match
                    if (m,w) not in match:
                        match.add((m,w))  # add new match
                    #else:
                        
                    men_copy[m] = w
                else:
                    message = "\n" + str(m) + " proposes to "+str(w)+ " who is matched, ergo she rejects the proposal (liking her current match better)\n"
                    unmatched.add(m)
            else:
                message = "\n" + str(m) + " proposes to " + str(w) + " who is not matched, ergo accepts the proposal\n"
                match.add((m,w))    
                men_copy[m] = w
    if trace:
        print(message + "\nalgorithm concluded: the final matches = " + str(match))
    return set(match)
    
    
if __name__ == '__main__':
    '''
    # Write script here
    m_file = prompt.for_string("Select the file name encoding all mens preferences")
    m_d = read_match_preferences(open(m_file))
    w_file = prompt.for_string('Select the file name encoding all womens preferences')
    w_d = read_match_preferences(open(w_file))
    print("Men Preferences\n"+ str(dict_as_str(m_d)) + "\nWomen Preferences\n" + str(dict_as_str(w_d)))
    trace = prompt.for_bool("Select whether to trace the algorithm[True]")
    print("the final matches =  " + str(make_match(m_d,w_d,trace)))
    '''
   
    print()
    import driver
    driver.default_file_name = "bscp12S19.txt"
    driver.default_show_traceback = True
    driver.default_show_exception = True
    driver.default_show_exception_message = True
    driver.driver()
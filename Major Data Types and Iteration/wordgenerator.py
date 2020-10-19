# Submitter: abathole(Bathole, Archita)
# Partner  : jensenak(Jensen, Alexis)
# We certify that we worked cooperatively on this programming
# assignment, according to the rules for pair programming

import goody
from goody import irange
import prompt
from random import choice


# For use in read_corpus: leave unchanged in this file
def word_at_a_time(file : open):
    for line in file:
        for item in line.strip().split():
                yield item


def read_corpus(os : int, file : open) -> {(str):[str]}:
    d = {}
    i = word_at_a_time(file)
    l = [next(i) for n in range(0,os)]
    for c in i:              # iterate over all remaining values in the file
        if tuple(l) in d:
            if c not in d[tuple(l)]:
                d[tuple(l)].append(c)
        else:
            d[tuple(l)] = [c]
        oldest = l.pop(0)    # drop oldest word
        l.append(c)          # add youngest word 
    return d
    

def corpus_as_str(corpus : {(str):[str]}) -> str:
    s = ''
    min = len(corpus[sorted(corpus)[0]])
    max = len(corpus[sorted(corpus)[0]])
    for key in sorted(corpus):
        s += "  " + str(key) + " can be followed by any of " + str(corpus[key]) + "\n"
        if len(corpus[key]) > max:
            max = len(corpus[key])
        if len(corpus[key]) < min:
            min = len(corpus[key])
    s += "max/min list lengths = " + str(max) + "/" + str(min) + "\n" 
    return s 


def produce_text(corpus : {(str):[str]}, start : [str], count : int) -> [str]: 
    r_l = []
    for w in start:
        r_l.append(w)
    l_key = r_l.copy()
    while count:
        if tuple(l_key) in corpus.keys():
            word = choice(corpus[tuple(l_key)])
            r_l.append(word)
            l_key.append(word)
            l_key.pop(0)
            count -= 1
        else:
            r_l.append(None)
            break
    return r_l


        
if __name__ == '__main__':
    '''
    # Write script here
    num = prompt.for_int("Select an order statistic")
    file = prompt.for_string("Select the file name to read")
    print("Corpus")
    d = read_corpus(num,open(file))
    print(corpus_as_str(d))
    print("Select 2 words for start of list")
    w1 = prompt.for_string("Select word 1")
    w2 = prompt.for_string("Select word 2")
    n_words = prompt.for_int("Choose # of words for appending to list")
    print("Random text = " + str(produce_text(d,[w1,w2],n_words)))
    '''
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bscp15S19.txt"
    driver.default_show_traceback = True
    driver.default_show_exception = True
    driver.default_show_exception_message = True
    driver.driver()
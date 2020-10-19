# Submitter: abathole(Bathole, Archita)
# Partner  : jensenak(Jensen, Alexis)
# We certify that we worked cooperatively on this programming
# assignment, according to the rules for pair programming

import goody
import prompt
from collections import defaultdict


def read_graph(file : open) -> {str:{str}}:
    line_list = [line.rstrip('\n') for line in file] 
    '''
    line_list = [line.rstrip('\n').split(';') for line in open(file)] 

    print(line_list)
    node_dict = defaultdict(set)
    value_set = {i.split(';')[1] if line_list.count() > 1 else '' for i in line_list}
    node_dict = {n1 : n2 for n1,n2 in line_list if line_list.count(n1) == 1 else }
    print(node_dict)
     #   value_set = {node_dict[n1].add(n2) for n1,n2 in node_dict if n1 not in node_dict}
    #    print(value_set)
    
    '''
    node_dict = {}
    for i in line_list:
        n1,n2 = i.split(';')
        
        if n1 in node_dict:
            node_dict[n1].add(n2)
        else:
            node_dict[n1] = set(n2)
   
        
        
   # node_dict = {i.split(';')[0] if i.split(';')[0] not in node_dict else node_dict[i.split(';')[0]].add(i.split(';')[1])  :set(i.split(';')[1]) for i in line_list}
   # print(node_dict)
    return node_dict


def graph_as_str(graph : {str:{str}}) -> str: # sorted
    sentence = ''
    for k,v in sorted(graph.items()):
        sentence += f"  {k} -> ['" + "', '".join(sorted(v)) + "']\n"
    #print(sentence)
    return sentence

        
def reachable(graph : {str:{str}}, start : str, trace : bool = False) -> {str}:
    '''
    reached_nodes = set()
    exploring_list = [start]
    while exploring_list:
        if trace:
            print("reached set = " + str(reached_nodes) + '\n' + "exploring list = " + str(exploring_list))
        current = exploring_list.pop(0)
        if trace:
            print('removing node from the exploring list/adding it to reached list: node = '+ current)
        reached_nodes.add(current)
        if current in graph.keys():
            for v in graph.get(current):
                exploring_list.append(v)
            if trace: 
                print('after adding all nodes reachable directly from a but not already in reached, exploring = ' + str(list(graph[current])))
    return reached_nodes
    '''
    pass
  
if __name__ == '__main__':
    # Write script here
    '''
    start = ''
    file = prompt.for_string("Select the file name encoding the graph")
    nodes = read_graph(open(file))
    print("Graph: node --> [all destination nodes of that node]")
    graph_as_str(nodes)
    start = prompt.for_string("Select the starting node (or select quit)", is_legal = (lambda start: True if start in nodes.keys()  or start == 'quit'  else False), error_message = "Illegal: not a source node")
    while start != 'quit':
        trace = prompt.for_bool("Select whether to trace the algorithm[True]")
        print("From node {start} the reachable nodes = " + str(reachable(nodes, start, trace))+'\n')
        start = prompt.for_string("\nSelect the starting node (or select quit)",is_legal = (lambda start: True if start in nodes.keys() or start == 'quit' else False), error_message = "Illegal: not a source node")
    '''
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bscp11S19.txt"
    driver.default_show_traceback = True
    driver.default_show_exception = True
    driver.default_show_exception_message = True
    driver.driver()
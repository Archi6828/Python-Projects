# Submitter: abathole(Bathole, Archita)
# Partner  : jensenak(Jensen, Alexis)
# We certify that we worked cooperatively on this programming
# assignment, according to the rules for pair programming

import re, traceback, keyword

def pnamedtuple( type_name, field_names, mutable =False ):
    def show_listing(s):
        for line_num, line_text in enumerate( s.split('\n'),1 ):
            print(f' {line_num: >3} {line_text.rstrip()}')

    # put your code here
    pat = r"([a-zA-Z])([a-zA-z]+|[1-9]+|\_+)*" #([a-zA-z]+)([1-9]+|\_+)
    if type_name in keyword.kwlist:
        raise SyntaxError(f"SyntaxError: type_name: {type_name} must not be a Python keyword")
    elif not re.match(pat,str(type_name)):
        raise SyntaxError(f"SyntaxError: type_name: {type_name} does not start with a letter which can be followed by 0 or more letters, digits, or underscore characters")
    else:
        if type(field_names) not in (str,list): 
            raise SyntaxError(f"SyntaxError: field_names: {field_names} must be list or str")
        else:
            m = field_names
   
    # change field_names into a [(),] based on 5? diferent ways?? 
    if type(field_names) is str:  
        if "," in field_names:
            k = field_names.split(",")
            l = [ (a.strip(),a.strip() ) for a in k]
            
        else:
            l = [ (a.strip(), a.strip()) for a in field_names.split()] 
          
        # check fieldnames
        for a in l:
            if not re.match(pat,a[0]):
                raise SyntaxError(f"SyntaxError: field_names: {a[0]} does not start with a letter which can be followed by 0 or more letters, digits, or underscore characters")
            if a[0] in keyword.kwlist:
                raise SyntaxError(f"SyntaxError: field_names: {a[0]} must not be a Python keyword")
     
    # turn list into a 2-()
    if type(field_names) is list:
        l = [(a,a) for a in m]
    
                        
    # gen
    def unique(iterable):
        u = set()
        for i in iterable:
            if i not in u:
                u.add(i)
                yield(i)
    n_l = list(unique(l))
  
    # bind class_definition (used below) to the string constructed for the class
    # init
    def gen_init(iterable):
        for i in iterable:
            yield(i)
            
    p = ",".join([i[0] for i in gen_init(n_l)])
        
    s_list = []
    for a,b in n_l:
        s_list.append(f"self.{a} = {b}")
 
    # reformat s for __repr__
    f_s = ''
    for a,b in n_l:
        f_s += f"{a} = {{ }},"
    f_s = f_s.strip(', ')
        
    # format get_
    get_string = ''
    for v in n_l:
        get_string += f"\n    def get_{v[0]}(self):\n        return self.{v[0]}\n"
        
    
    class_template ='''\
class {type_name}:
    def __init__(self,{p}):
        {arg}
        self._fields = {init}
        self._mutable = {m}
        self._notDone = False
        self._initDone = True
        
    def __repr__(self):
        self._notDone = True
        s = ''
        for a in self._fields:
            value = "self.get_" + a + "()"
            s = s + a + "=" + str(eval(value)) + ","
        s = s.rstrip(',')
        self._notDone = False
        return "{type_name}(" + s + ")"
    {name}    
    def __getitem__(self,index):
        if type(index) == str and index in self._fields:
            return eval("self.get_" + index + "()")
        elif type(index) == int:
            if index > len(self._fields):
                raise IndexError("Index: " + str(index) + " out of bounds.")
            if self._fields[index]:
                return eval("self.get_" + self._fields[index] + "()")
            else:
                raise IndexError("Index: " + str(index) + " out of bounds.")
        else:
            raise IndexError("Index: " + str(index) + " string not in field.")
          
    def __eq__(self,other):
        if type(other) is {type_name}:
            if len(other._fields) == len(self._fields):
                return all(self.__getitem__(i) == other.__getitem__(i) for i in self._fields)
        else:
            return False
            
    def _replace(self,**kargs):
        self._notDone = True
        d = kargs
        if self._mutable:
            for k,v in d.items():
                if k in self._fields:
                    self.__dict__[k] = v
                else:
                    self._notDone = False
                    raise TypeError(str(k) + 'is not a field name')
            self._notDone = False
        else:
            s = eval(self.__repr__())
            for k,v in d.items():
                if k in s._fields:
                    s.__dict__[k] = v
                else:
                    self._notDone = False
                    raise TypeError(str(k) + 'is not a field name')
            self._notDone = False
            return s  
    '''
    class_definition = class_template.format(type_name = type_name,p = p, arg = '\n        '.join(a for n,a in enumerate(s_list,1) if n != 1 or a), init = '['+','.join(["'"+i[0]+"'" for i in gen_init(n_l)])+']', m = str(mutable), f_s = f_s, name = get_string)
     
    
    #getitem_string = getitem_string
    # While debugging, remove comment below showing source code for the class
    # show_listing(class_definition)
    
    # Execute this class_definition (a str) in a local name space; then, bind the
    #   the source_code attribute to class_definition; after except, return the
    #   class object created; if there is a syntax error, list the class and
    #   also show the error
    name_space = dict( __name__ = f'pnamedtuple_{type_name}' )  
    
    
    try:
        exec(class_definition,name_space)
        name_space[type_name].source_code = class_definition
    except (TypeError,SyntaxError):      
        show_listing(class_definition)
        traceback.print_exc()
    return name_space[type_name]

    '''
    def __setattr__(self,name,value):
        if self._initDone:
            #if not self._mutable:
            self.__dict__[name] = value
        else:
           raise AttributeError(str({type_name}) + ".__setattr(): cannot change or add attributes.")  
     '''       
    


    
if __name__ == '__main__':
    # Test pnamedtuple below in script: e.g., Point = pnamedtuple('Point','x,y')
     
    #driver tests
    import driver
    driver.default_file_name = 'bscp3S19.txt'
#     driver.default_show_exception= True
#     driver.default_show_exception_message= True
#     driver.default_show_traceback= True
    driver.driver()

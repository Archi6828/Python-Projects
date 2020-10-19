Class Point:
    def __init__(self,*fieldnames):
        # initialize
        self._fields = list(gen_init(*fieldnames))
        print(self._fields)
        self._mutable = {m}
        
        def gen_init(iterable):
        for i in iterable:
            yield(i)
        
    def __repr__(self):
        return f'{type_name}({f_s})'
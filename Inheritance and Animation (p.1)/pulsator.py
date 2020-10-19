# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions


from blackhole import Black_Hole


class Pulsator(Black_Hole): 
    counter = 30
    
    def __init__(self,x,y): 
        Black_Hole.__init__(self,x,y)
        self._count = 0
        
    def update(self,model):
        self._count += 1
        
        if self.get_dimension() == (0,0):
            model.remove(self)
    
        e = Black_Hole.update(self, model)
        
        if e:
            for _ in range(len(e)):
                self.change_dimension(1, 1)
           
        if self._count == Pulsator.counter:
            self._count = 0
            if not e:
                self.change_dimension(-1, -1)
            
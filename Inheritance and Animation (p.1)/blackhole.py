# Black_Hole is derived from Simulton only, updating by finding+removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey


class Black_Hole(Simulton):
    radius = 10
    
    def __init__(self,x,y): 
        Simulton.__init__(self,x,y,Black_Hole.radius*2,Black_Hole.radius*2)

    def contains(self, xy):
        return True if self.distance(xy) < Black_Hole.radius else False

    def update(self,model):
        f_list = model.find(lambda x : isinstance(x,Prey))
        eaten = set()
        for s in f_list:
            if self.contains(s.get_location()):
                eaten.add(s)
        for e in eaten:        
            model.remove(e)
        return eaten    
        self.move()
        self.wall_bounce()

    def display(self,canvas):
        canvas.create_oval(self._x-Black_Hole.get_dimension(self)[0]/2, self._y-Black_Hole.get_dimension(self)[1]/2,
                            self._x+Black_Hole.get_dimension(self)[0]/2, self._y+Black_Hole.get_dimension(self)[1]/2,
                            fill= 'black')

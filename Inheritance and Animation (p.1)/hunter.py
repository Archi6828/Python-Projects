# Hunter is derived from each of the Mobile_Simulton and Pulsator classes:
#   updating/displaying like a Pulsator, but also moving (either in a straight
#   line or in pursuit of Prey).


from prey import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2


class Hunter(Pulsator, Mobile_Simulton):
    dist = 200
    def __init__(self,x,y): 
        Pulsator.__init__(self,x,y)
        self.set_speed(5)
        self.randomize_angle()
        
    def update(self,model):
        Pulsator.update(self, model)
        p = model.find(lambda x: isinstance(x, Prey) and self.distance(x.get_location()) <=  Hunter.dist)
        
        if p:
            closest = min([(self.distance(prey.get_location()),prey) for prey in p], key = lambda x: x[0])
            
            angle = atan2(closest[1].get_location()[1] - self.get_location()[1], closest[1].get_location()[0] - self.get_location()[0])
            self.set_angle(angle)
                
        self.move()
        self.wall_bounce()
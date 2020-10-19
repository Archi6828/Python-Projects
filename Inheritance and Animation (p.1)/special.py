# Special is derived from Hunter.It is an AI meteor object designed to purposefully
# hit other objects. Every 4 hits, there is a 20% chance the meteor changes its speed 
# and angle by a + or - 0.8 random value. But the speed limit is (1,10).The meteor 
# behaves like a Hunter except it is purple.

# It degrades the level of any prey simulton object it touches: [Floater --> Ball --> destroys Ball] 
# So, the floater gets eaten, but a new Ball is added to the canvas near the top left of the screen.
# It also destroys any Hunter or Pulsator whose distance is 10 or less from the meteor.
# The meteor gets eaten by Black_Holes.

#   updating/displaying like a Hunter, but also moving (either in a straight
#   line or in pursuit of Prey).

from hunter import Hunter
from blackhole import Black_Hole
from prey import Prey
from ball import Ball
from random import random

class Special(Hunter):
    hits = 0
    
    def __init__(self,x,y):
        Hunter.__init__(self, x, y)
    
    def update(self,model):
        Hunter.update(self, model)
        
        transform_Black_hole_types = ['Hunter','Pulsator','Black_Hole','None']
        p = model.find(lambda x: isinstance(x, Black_Hole) and self.distance(x.get_location()) <=  10)
        for k in p:
            if isinstance(k, Black_Hole):
                        for t in transform_Black_hole_types:
                            if t in str(k):
                                # create new object
                                if (t == 'Hunter' or t == 'Pulsator'):
                                    model.remove(k)
                                if t == 'Black_Hole':
                                    model.remove(self)
        
        crashed = Black_Hole.update(self, model)
        
        if crashed:
            for c in crashed:
                # update Special.hits
                Special.hits += 1
               
                if Special.hits % 4 == 0:
                    n = random() * 100
                    if n < 20:
                        s = random()
                        while abs(self.get_speed() + s) < 0 and abs(self.get_speed() + s) > 0.8:
                            s = random()
                        new_speed = self.get_speed() + s
                        if new_speed >= 1 and new_speed <= 10:
                            self.set_speed(new_speed)
                            self.randomize_angle()
                     
                # degrade objects that meteor crashed into
               
                transform_Prey_types = ['Floater','Ball','None']
                
                if isinstance(c, Prey):
                    for t in transform_Prey_types:
                        if t in str(c):
                            # create new object
                            new_obj = transform_Prey_types[transform_Prey_types.index(t)+ 1]
                            if new_obj != 'None':
                                if t == 'Floater':
                                    n = random() * 10
                                    model.add(Ball(0 + n , 0 + n))
                              
        self.move()
        self.wall_bounce()

    def display(self,canvas):
        canvas.create_oval(self._x-Special.radius, self._y-Special.radius,
                            self._x+Special.radius, self._y+Special.radius,
                            fill= 'purple')
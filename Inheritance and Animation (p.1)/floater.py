# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


#from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random


class Floater(Prey): 
    radius = 5
    
    def __init__(self,x,y): 
        Prey.__init__(self,x,y,2*Floater.radius,2*Floater.radius,0,5)
        self.randomize_angle()

    def update(self,model):
        n = int(random() * 100)
        
        if n < 31:
            r = self.get_angle()
            self.randomize_angle()
            while abs(self.get_angle() + r) < 0 and abs(self.get_angle() + r) > 0.5:
                self.randomize_angle()  
            
            s = random()
            while abs(self.get_speed() + s) < 0 and abs(self.get_speed() + s) > 0.5:
                s = random()
            new_speed = self.get_speed() + s
            if new_speed >= 3 and new_speed <= 7:
                self.set_speed(new_speed)
        self.move()
        self.wall_bounce()

    def display(self,canvas):
        canvas.create_oval(self._x-Floater.radius, self._y-Floater.radius,
                            self._x+Floater.radius, self._y+Floater.radius,
                            fill= 'red')

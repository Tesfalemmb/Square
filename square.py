
import turtle

class Polygon:
    def __init__(self,name,sides):
        self.name = name
        self.sides = sides

    def draw(self):
        for i in range(self.sides):
            turtle.forward(100)
            turtle.right(90)
        turtle.done()

pol1 = Polygon('square',4) 
pol2 = Polygon('pentagon',5)

pol1.draw()
#pol2.draw()

    

        
    
         
        



   

     


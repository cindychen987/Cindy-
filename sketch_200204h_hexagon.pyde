gamebegin = False
angle = 0
e=40
d=30
def setup():
  background (0)
  size(1200, 800);
 
def draw():
    background(0)
    global angle
    global d
    global e
    Hex(0, 0, 44, angle)
    if keyPressed:
        gamebegin= True
        if keyCode == LEFT:
            angle = angle + PI/45
        if keyCode == RIGHT:
            angle = angle - PI/45
            MouseMove=False
    
    
    rect(e,d, 20, 20)
    e = e + 3
    d = d + 4
    if d > 397 and d <= 402:
        d = 20
    

   # Hex(float x, float y, float gs) 
   
   
def  Hex(x, y, gs, angle):
    stroke (255)
    pushMatrix()
    translate(width/2, height/2)
    rotate(angle)
    beginShape
    point(x - gs, y - sqrt(3) * gs);
    line(x - gs, y - sqrt(3) * gs, x + gs, y - sqrt(3) * gs)
    point(x + gs, y - sqrt(3) * gs);
    point(x + 2 * gs, y);
    point(x + gs, y + sqrt(3) * gs);
    point(x - gs, y + sqrt(3) * gs);
    point(x - 2 * gs, y);
    line(x + gs, y - sqrt(3) * gs, x + 2 * gs, y)
    line(x + 2 * gs, y, x + gs, y + sqrt(3) * gs)
    line(x + gs, y + sqrt(3) * gs, x - gs, y + sqrt(3) * gs)
    line(x - gs, y + sqrt(3) * gs, x - 2 * gs, y)
   
    endShape(CLOSE);
    popMatrix()

    
    
        

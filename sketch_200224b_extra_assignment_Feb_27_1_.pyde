   
class Particle:
    def __init__(self):
        self.pos_x=random(0,width)
        self.pos_y=random(0,height)
        
        
        self.speed_x = random (-5,5)
        self.speed_y = random (-5,5)
        
        
    
     
    def move(self):
        # updates the position of the ball according to game physics.
        
        self.pos_x += self.speed_x
        self.pos_y += self.speed_y
        if self.pos_x > width:
            self.pos_x = 0
        if self.pos_x < 0:
            self.pos_x = width
        if self.pos_y > height:
            self.pos_y = 0
        if self.pos_y < 0:
            self.pos_y = height
    
    def draw(self):
        # Draws the particle on the screen
        fill(255)
        circle(self.pos_x, self.pos_y, 12)
        pass
        
     
def setup():
    global particle
    # particle = Particle()
    particle=[]
    
    size(500, 500)
    
    for i in range(10):
        particle.append(Particle())
        # particle[i] = Particle(i)
        #particle.append(random.random())
        # pos_x(random.random())
        # pos_y(random.random())
    
    
def draw():
    global particle
    background(0)
    for i in range(10):
    
    #particle.move()
    #particle.draw()
        particle[i].move()
        particle[i].draw()
    

    
    
    
    
    

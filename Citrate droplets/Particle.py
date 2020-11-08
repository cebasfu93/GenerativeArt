class Particle:
    def __init__(self):
        self.pos = PVector(random(width), random(height))
        self.vel = PVector(0,0)
        self.acc = PVector(0,0)
        self.maxspeed = 3
        self.prevPos = self.pos.copy()
        
    def update(self):
        self.vel += self.acc
        self.vel.limit(self.maxspeed)
        self.pos += self.vel
        self.acc.mult(0)
        
    def applyForce(self, force):
        self.acc += force
        
    
    def show(self, pic):
        ndx = int(self.pos.y * pic.width + self.pos.x)

        r, g, b = red(pic.pixels[ndx]), green(pic.pixels[ndx]), blue(pic.pixels[ndx])
        noFill()
        stroke(r, g, b, 10)
        #stroke(0)
        strokeWeight(1)
        line(self.prevPos.x, self.prevPos.y, self.pos.x, self.pos.y)
        
    def edges(self):
        if self.pos.x > width-1:
            self.pos.x = 0        
            self.updatePrev()     
        if self.pos.x < 0:
            self.pos.x = width-1
            self.updatePrev()
        if self.pos.y > height-1:
            self.pos.y = 0
            self.updatePrev()       
        if self.pos.y < 0:
            self.pos.y = height-1
            self.updatePrev()
            
    def updatePrev(self):
        self.prevPos.x = self.pos.x
        self.prevPos.y = self.pos.y
        
            
    def follow(self, vectors, scl, cols, rows):
        x = int(self.pos.x/scl)%cols
        y = int(self.pos.y/scl)%rows
        ndx = y*cols + x
        force = vectors[ndx]
        self.applyForce(force)

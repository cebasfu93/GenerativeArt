class Particle:
    def __init__(self):
        self.pos = PVector(random(width), random(height))
        self.vel = PVector(0,0)
        self.acc = PVector(0,0)
        self.maxspeed = 30
        self.prevPos = self.pos.copy()
        
    def update(self):
        self.vel += self.acc
        self.vel.limit(self.maxspeed)
        self.pos += self.vel
        self.acc.mult(0)
        
    def applyForce(self, force):
        self.acc += force
        
    def show(self, hplus, hmem):
        cini = (201,68,180,8) #violet
        cfin = (26,150,255,8) #cyan
        clow = (145,180,120,16) #tree
        
        d1 = dist(width/2, hplus, self.pos.x, self.pos.y)
        d1 = constrain(d1, width/3, width/1.8)
        d1 = map(d1, width/3, width/1.8, 0, 1)
        #d1 = dist(width/2, hplus, self.pos.x, self.pos.y)
        #d1 = map(d1, width/2.5, width/1.6, 0, 1)
        c = [ci+(cf-ci)*d1 for ci, cf in zip(cini, cfin)]
        
        d2 = self.pos.y
        #d2 = map(d2, 0, hmem*1.1, 0, 1)
        d2 = constrain(self.pos.y, hmem-height/5, hmem*1.1)
        d2 = map(d2, hmem-height/5, hmem*1.1, 0, 1)
        clast = [cc+(cl-cc)*d2 for cl, cc in zip(clow, c)]
        
        d3 = map(self.pos.y, 0, height, 2,4)
        stroke(*clast)
        strokeWeight(d3)
        line(self.pos.x, self.pos.y, self.prevPos.x, self.prevPos.y)
        
        #fill(255,200,200)
        #ellipse(self.pos.x, self.pos.y, 15, 15)
        
    def updatePrev(self):
        self.prevPos.x = self.pos.x
        self.prevPos.y = self.pos.y
        
    def resetPos(self, hnp, hmem):
        mc = random(0,1)
        if mc > 0.2:
            #self.pos = PVector(random(width), (randomGaussian()*(height-hmem)+hmem))
            self.pos = PVector(random(width), height)
        else:
            self.pos = PVector(random(width/4, 3*width/4), random(0,hmem))
        self.vel = PVector(0,0)
        self.acc = PVector(0,0)
        
    def edges(self, hnp, hmem):
        if self.pos.x > width:
            self.pos.x = 0
            self.updatePrev()
            #self.resetPos(hnp, hmem)
        if self.pos.x < 0:
            self.pos.x = width
            self.updatePrev()
            #self.resetPos(hnp, hmem)
        if self.pos.y > height:
            self.pos.y = 0
            self.updatePrev()
        if self.pos.y < 0:
            #self.pos.y = height
            self.resetPos(hnp, hmem)
            
    def follow(self, vectors, scl, cols, rows):
        x = int(self.pos.x/scl)%cols
        y = int(self.pos.y/scl)%rows
        ndx = y*cols + x
        force = vectors[ndx]
        self.applyForce(force)

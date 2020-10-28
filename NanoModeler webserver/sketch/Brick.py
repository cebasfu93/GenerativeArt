class Brick:
    def __init__(self, x0, y0):
        self.R = dist(x0, y0, width/2, height/2)
        rsc = constrain(self.R, width/3.2, width/1.3)
        self.size = map(rsc, width/3.2, width/1.3, 20, 120)
        self.x0, self.y0 = x0, y0
        self.x1, self.y1 = self.x0 + self.size*random(0,1), self.y0 + self.size*random(0,1)
        self.x2, self.y2 = self.x0 + self.size*random(0,1), self.y0 - self.size*random(0,1)
        self.x3, self.y3 = self.x0 - self.size*random(0,1), self.y0 - self.size*random(0,1)
        self.x4, self.y4 = self.x0 - self.size*random(0,1), self.y0 + self.size*random(0,1)
        
    def show(self):
        transin = width/2.2
        transout = width/1.3
        rc = constrain(self.R, transin, transout)
        rr = map(rc, transin, transout, 245, 21)
        rg = map(rc, transin, transout, 30, 204)
        rb = map(rc, transin, transout, 231, 93)
        rca = constrain(self.R, width/3, width/1.5)
        ra = map(rca, width/3, width/1.5, 0, 255)
        fill(rr, rg, rb, ra)
        
        rw = map(rc, transin, transout, 0, 4)
        if rw == 0.0:
            noStroke()
        else:
            stroke(0)
            strokeWeight(rw)
        quad(self.x1, self.y1, self.x2, self.y2, self.x3, self.y3, self.x4, self.y4)
        
        
        
        

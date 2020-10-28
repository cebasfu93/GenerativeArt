class Cuadrado:
    def __init__(self, ymin, ymax, r, pn=0.3):
        x0, y0 = random(-width*0.05, width), random(min(ymin, ymax), max(ymin, ymax))
        x1, y1 = x0 + r*random(1-pn,1+pn), y0 + r*random(-pn,pn) 
        x2, y2 = x1, y1 - r*random(1-pn,1+pn)
        x3, y3 = x2 - r*random(1-pn,1+pn), y2
        
        self.p0 = PVector(x0, y0)
        self.p1 = PVector(x1, y1)
        self.p2 = PVector(x2, y2)
        self.p3 = PVector(x3, y3)
        self.xy = [x0, y0, x1, y1, x2, y2, x3, y3]
        self.mid = PVector(0.25*(x0+x1+x2+x3), 0.25*(y0+y1+y2+y3))
        self.r = r
    
    def show(self, ci, cf, param):
        col = [c1+(c2-c1)*param for c1, c2 in zip(ci, cf)]
        fill(*col)
        stroke(0, col[3])
        strokeWeight((param)*6)
        #quad(*self.xy)
        square(self.mid.x, self.mid.y, self.r)
        
class Circulo:
    def __init__(self, nprad, r, pn=0.3):
        r_loc = random(0, nprad)
        th_loc = random(0, TWO_PI)
        self.x, self.y = r_loc*cos(th_loc)+width/2, r_loc*sin(th_loc)+height/2
        self.r = r*random(1-pn,1+pn) 
    
    def show(self, ci, cf, param):
        col = [c1+(c2-c1)*param for c1, c2 in zip(ci, cf)]
        fill(*col)
        stroke(0, col[3])
        strokeWeight(5)
        #circle(self.x, self.y, self.r)
        square(self.x, self.y, self.r)

def sign(x):
    if x > 0:
        return 1
    else:
        return -1

class Tail:
    def __init__(self, yfin, yini, nbeads=10, r=10):
        self.r=r
        xini = random(0,1)*width
        sgnx = sign(xini-width/2)
        sgny = sign(yini-height/2)
        rad = dist(xini, yini, width/2, height/2)
        
        if sgnx == 1:
            thini = sgny*acos((xini-width/2)/rad)
            thfin = asin((yfin-height/2)/rad)
            thfin = asin((yfin-height/2)/rad)
        else:
            thini = PI - sgny*(PI - acos((xini-width/2)/rad))  
            thfin = PI - asin((yfin-height/2)/rad)
        
        dth = (thfin-thini)/(nbeads-1)
        self.beads = []
        for j in range(nbeads):
            th = thini + dth*j
            x = rad*cos(th)+width/2
            y = rad*sin(th)+height/2
            self.beads.append(PVector(x, y))
            
    def show(self, ci, cf, param):
        col = [c1+(c2-c1)*param for c1, c2 in zip(ci, cf)]
        beginShape()
        for bead in self.beads:
            noFill()
            stroke(0, col[3])
            strokeWeight(7)
            #square(bead.x, bead.y, self.r)
            vertex(bead.x, bead.y)
        endShape()
        
        for bead in self.beads:
            fill(*col)
            stroke(*col)
            strokeWeight(5)
            square(bead.x, bead.y, 10)
            
        
        
        

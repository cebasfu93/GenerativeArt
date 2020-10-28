class Nano:
    def __init__(self, x0, y0, r0, rsmall):
        self.x0 = x0
        self.y0 = y0
        self.r0 = r0
        self.n_inner = 500
        self.rsmall = self.r0/3
        
    def show(self):
        np_col = (255, 167, 3, 200) #Central color of the metal core
        fill(*np_col)
        stroke(0)
        strokeWeight(2)
        ellipse(self.x0, self.y0, 2*self.r0+self.rsmall, 2*self.r0+self.rsmall)
        
        stroke(0)
        strokeWeight(1)
        #noStroke()
        for i in range(self.n_inner):
            r, g, b = randomize_color(np_col)
            fill(r,g,b)
            
            rad = self.rsmall*random(0.5,1)
            r_rand = self.r0*random(0,1)
            theta = random(0, TWO_PI)
            x = self.x0 + r_rand*cos(theta)
            y = self.y0 + r_rand*sin(theta)
            ellipse(x, y, rad, rad)
            
            
        cit_col = (3,131,255) #Central color of the citrate
        stroke(0)
        strokeWeight(1)
        #noStroke()
        for i in range(self.n_inner):
            r, g, b = randomize_color(cit_col)
            fill(r,g,b, 155)
            
            rad = self.rsmall*random(0.3,0.7)
            r_rand = self.r0*random(1.1,1.4)
            theta = random(0, TWO_PI)
            x = self.x0 + r_rand*cos(theta)
            y = self.y0 + r_rand*sin(theta)
            ellipse(x, y, rad, rad)
            

            

        
def randomize_color(c, delta=40):
    r = c[0] + random(-delta, delta)
    g = c[1] + random(-delta, delta)
    b = c[2] + random(-delta, delta)
    return r,g,b

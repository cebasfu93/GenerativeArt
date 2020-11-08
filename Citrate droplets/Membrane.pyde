from Particle import Particle
from Network import networkize

WIDTH = 800
HEIGHT = int(1.41*WIDTH)
inc = 0.01
scl = 20
cols, rows = int(WIDTH/scl), int(HEIGHT)/scl
koff = 0
N_part = 400
particles = []
flowfield = []
HMEM = 2*HEIGHT/3
HNP = HEIGHT/3
WNP = WIDTH/2
HPLUS = HNP+(HMEM-HNP)/2
n_fire = 300

static = False

def generate_field(x, y, pn):
    v = PVector.fromAngle(pn)
    v.setMag(8)
    
    return v
       
def pirix(t, a, b):
    return a*width*(1-sin(t))*cos(t)

def piriy(t, a, b):
    return -b*height*(sin(t)-1)


def setup():
    #Call global variables
    global WIDTH, HEIGHT, cols, rows, N_part, particles, static, HPLUS, HMEM, n_fire
    
    #Set display properties
    if static:
        noLoop()
    size(WIDTH, HEIGHT)
    background(255)
    pic = loadImage("VMD/Embellish2.png")
    pic.resize(width, height)
    image(pic, 0, 0, width, height)
        
    #Initializes particles
    for i in range(N_part):
        particles.append(Particle())
    
    for i in range(rows):
        for j in range(cols):
            flowfield.append(0)
    
    
def draw():
    global inc, scl, cols, rows, koff, particles, N_part, flowfield, HMEM, HNP, HPLUS, static
    
    ioff = 0 
    for i in range(rows):
        joff = 0
        for j in range(cols):
            ndx = i*cols + j
            pn = noise(joff, ioff, koff)*TWO_PI*4
            v = generate_field(j*scl, i*scl, pn)
            flowfield[ndx] = v
            
            if static:
                stroke(0,100)
                push()
                translate(j*scl, i*scl)
                rotate(v.heading())
                line(0, 0, scl, 0)
                pop()
            
            joff += inc
        ioff += inc
    koff += 0.008
    
    #pic = loadImage("VMD/gHNP-PMF-M1.dat.png")
    #pic = loadImage("VMD/Embellish.png")
    pic = loadImage("VMD/Embellish2.png")
    pic.resize(width, height)
    #pic.loadPixels()
    #image(pic, 0, 0, width, height)        
    
    """if not static:
        for i in range(N_part):
            particles[i].follow(flowfield, scl, cols, rows)
            particles[i].update()
            particles[i].edges()
            particles[i].show(pic)
            particles[i].updatePrev()"""
    
    networkize(pic, DY=0, n_nodes=300)
        
    if frameCount%100 == 0:
        print(frameCount)
    if frameCount == 20:
        noLoop()
        save('Cover.png')
        

    
                        

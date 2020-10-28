from Particle import Particle
from Network import networkize

WIDTH = 2490
HEIGHT = 3510
inc = 0.1
scl = 120
cols, rows = int(WIDTH/scl), int(HEIGHT)/scl
koff = 0
N_part = 500
particles = []
flowfield = []
HMEM = 2*HEIGHT/3
HNP = HEIGHT/3
WNP = WIDTH/2
HPLUS = HNP+(HMEM-HNP)/2
n_fire = 300

static = False

def generate_field(x, y, pn):
    global HMEM, HNP, WNP, HPLUS
    if y < HMEM:
        #Outside membrane
        v_plusx = constrain(width/(0.1+x-width/2), -10, 10)
        v_plusx = map(v_plusx, -10, 10, -2, 2)
        yf = map(y, height/4, HPLUS, 0.0, 1)
        
        v_plusy = constrain(y, height/4, HMEM)
        v_plusy = map(v_plusy, height/4, HMEM, -2.5, -0.2)
        v_plus = PVector(yf*v_plusx,v_plusy)
        
        if y < HPLUS:
            #Above nanoparticle
            v_flowx = constrain(abs(x-width/2.0), 0, width/2)
            v_flowx = map(v_flowx, 0, width/2, 0, 1.)
            if x < width/2:
                v_flow = PVector(v_flowx,-1)
            else:
                v_flow = PVector(-1*v_flowx, -1)
            v_perlin = PVector.fromAngle(pn)
            v_perlin.setMag(1.8) # 1.2
        else:
            #Below nanoparticle
            v_flow = PVector(0,-1)
            v_perlin = PVector.fromAngle(pn)
            v_perlin.setMag(0.4)
   
    else:
        #Inside membrane
        v_flow = PVector(0, -1.6)
        v_plus = PVector(0,0)
        v_perlin = PVector.fromAngle(pn)
        v_perlin.setMag(1)

    v = v_flow + v_plus + v_perlin
    v.setMag(8)
    
    return v
       
def pirix(t, a, b):
    return a*width*(1-sin(t))*cos(t)

def piriy(t, a, b):
    return -b*height*(sin(t)-1)

def pirishape(ytrans, a, b, n_pts=100):
    ymin = piriy(-PI/2, a, b)
    push()
    translate(width/2, ytrans-ymin)
    beginShape()
    thini, thfin = 3*PI/4+random(-PI/6, PI/6), 9*PI/4+random(-PI/6, PI/6)
    dth = (thfin-thini)/n_pts
    noiseini = random(0, 200)
    for i in range(n_pts):
        noisefactor = noise((i+noiseini)*0.02)*1.5
        th = i*dth + thini
        x = (pirix(th, a, b) - 0)*noisefactor + 0
        y = (piriy(th, a, b) - ymin)*noisefactor + ymin
        curveVertex(x,y)
    endShape()
    pop()
    

def setup():
    #Call global variables
    global WIDTH, HEIGHT, cols, rows, N_part, particles, static, HPLUS, HMEM, n_fire
    
    #Set display properties
    if static:
        noLoop()
    size(WIDTH, HEIGHT)
    background(255)
    
    #Initializes particles
    for i in range(N_part):
        particles.append(Particle())
    
    for i in range(rows):
        for j in range(cols):
            flowfield.append(0)
    
    aini, afin = 0.1, 0.41
    bini, bfin = 0.15, 0.62
    cini = (201,68,180,10) #violet
    cfin = (26,150,255,50) #cyan
    for i in range(n_fire):
        a = (afin-aini)/n_fire*i
        b = (bfin-bini)/n_fire*i
        noiseSeed(i)
        par = map(i, 0, n_fire-1, 0,1)
        c = [ci+(cf-ci)*par for ci, cf in zip(cfin, cini)]
        noFill()
        stroke(*c)
        strokeWeight(par+3)
        a*=1.1
        b*=1.1
        pirishape(HPLUS*1.25, a, b)
    
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
    koff += 0.003

    #stroke(0)
    #strokeWeight(2)
    #fill(255,0,0)
    #ellipse(width/2, HNP, 10, 10)
    #line(0, HMEM, width, HMEM)

    if not static:
        for i in range(N_part):
            particles[i].follow(flowfield, scl, cols, rows)
            particles[i].update()
            particles[i].show(HPLUS, HMEM)
            particles[i].edges(HNP, HMEM)
            particles[i].updatePrev()
        
        
    """if frameCount in [150, 300, 450]:
        NP = loadImage("VMD/NP_noSurf.png", 'png')
        NP.resize(width, height)
        networkize(NP, DY=0.7*(HNP-height/2), n_nodes=300)
        
        MEM = loadImage("VMD/MEM.png", 'png')
        MEM.resize(width, height)
        networkize(MEM, DY=height/9, n_nodes=600)"""
        
    if frameCount%100 == 0:
        print(frameCount)
    if frameCount == 3500:
        noLoop()
        save('Cover.png')
        

    
                        

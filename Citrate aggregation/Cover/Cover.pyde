from Nano import Nano
from Halo import Halo
WIDTH = 2490
HEIGHT = 3510#int(WIDTH*1.41)
N_nano = 15
N_cells = 12
N_halos = 24

def setup():
    #Call global variables
    global WIDTH, HEIGHT
    #Set display properties
    noLoop()
    size(WIDTH, HEIGHT)
    background(255,255,255)
    
def draw():
    #Call global variables
    global N_nano, N_cells
    
    ANG = PI/3
    DH = height/2.5
    x1, y1 = width/2, height/2-DH/2
    x2, y2 =width/2, height/2+DH/2
    Rnp = width/6
    
    cells = []
    th_ini, th_fin = -PI/4, 5*PI/4
    dth = (th_fin - th_ini)/(N_cells-1)
    F = 1.6
    for i in range(N_cells):
        cells.append([x1+F*Rnp*cos(th_ini+i*dth), y1+F*Rnp*sin(th_ini+i*dth)])
        cells.append([x2+F*Rnp*cos(-th_ini-i*dth), y2+F*Rnp*sin(-th_ini-i*dth)])
    """for cell in cells:
        fill(0,0,255)
        ellipse(cell[0], cell[1], 20, 20)"""
    
    loadPixels()
    for i in range(height):
        for j in range(width):
            ndx = i*width + j
            dists = []
            for n in range(2*N_cells):
                v = cells[n]
                d = dist(j, i, v[0], v[1])
                dists.append(d)
            dists.sort()
            r = map(dists[3], width/14, width/4, 0, 220)
            g = map(dists[0], width/10, width/4, 0, 220)
            b = map(dists[2], 0, width/2.7, 255, 50)
            pixels[ndx] = color(r,g,b)
    updatePixels()
    print('done')
    
    randomSeed(667)
    perlinseed = 0
    for i in range(N_halos):
        perlinseed += 1
        noiseSeed(perlinseed)
        r_th = random(-PI/3, PI/3)
        Halo(x1, y1, 1.8*Rnp, 0, TWO_PI, i, N_halos-1)
        perlinseed += 1
        noiseSeed(perlinseed)
        Halo(x2, y2, 1.8*Rnp, 0, TWO_PI, i, N_halos-1)
        
    save("Cover.png")
    
def cosrule(a, b, c):
    return acos((a**2+b**2-c**2)/(2*a*b))

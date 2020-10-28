from Bodies import Solvent, Nano, Leaflet
test = False

if test:
    WIDTH = 600
    HEIGHT = int(WIDTH*1.41)
else:
    WIDTH = 2490
    HEIGHT = 3510 
    
mem_width = HEIGHT/3.2 #2.0
h_upper = HEIGHT/2-mem_width/2
h_lower = HEIGHT/2+mem_width/2
np_radius = 1.4*mem_width/2 #1.1

norred = (255,255,255,0)
norwhite= (255,255,255,255)
norblue = (0,48,135,255)

csolin = (200,16,46,255)#255
csolout = norred#(242,169,132,255)#(242,206,132, 255)#beige
cnpin = (240,240,240,100)
cnpout = (50,50,50,200)
ctailin = norred # (170,17, 160,255) #purple
ctailmed = (255,255,255,100) #(17,170,51,0) #green
ctailout = norblue

def setup():
    size(WIDTH, HEIGHT)
    background(255)
    noLoop()
    
def draw():
    #line(0,h_upper, width, h_upper)
    #line(0,h_lower, width, h_lower)

    Leaflet(ntails=1400, 
            yini=h_upper, randwidth=-1*mem_width, 
            nbeads=40, beadsize=90, rnp=0, 
            cmin=(50,50,50,255), cmax=ctailmed)
    print('Done with leaflet 1')
    Leaflet(ntails=800, 
            yini=h_lower, randwidth=1*mem_width, 
            nbeads=40, beadsize=90, rnp=np_radius, 
            cmin=ctailmed, cmax=ctailout)
    print('Done with leaflet 2')
    Nano(nprad=np_radius, r=60, ncir=20000, cmin=cnpout, cmax=cnpin, pn=0.2)
    print('Done with NP')
    
    Solvent(ymin=h_upper, ymax=0, nsq=3000, r=110, cmin=csolout, cmax=csolin, nprad=np_radius)#3000
    print('Done with solvent 1')
    Solvent(ymin=h_lower, ymax=height, nsq=3000, r=110, cmin=csolout, cmax=csolin, nprad=np_radius)#3000
    print('Done with solvent 2')
    save('Cover.png')
    
    return 0
        

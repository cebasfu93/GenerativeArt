from Brick import Brick
from ShowImages import show_plain, show_radial_trans

WIDTH, HEIGHT = 2490, 3510 #A4 at 300 dpi
n_quad = 15000

def setup():
    #Call global variables
    global WIDTH, HEIGHT
    #Set display properties
    size(WIDTH, HEIGHT)
    noLoop()
    background(255, 230, 140)

def draw():
    #Call global variables
    global n_quad
    
    #Display quadrilaterals
    for i in range(n_quad):
        brick = Brick(random(width), random(height))
        brick.show()
        
    #Load images
    core = loadImage("./coreg.png", "png")
    core_s = loadImage("./core_sg.png")
    core_s_lig = loadImage("./core_s_ligg.png")
    lig_surf = loadImage("./lig_surfg.png")
    sol_surf = loadImage("./sol_surfg.png")

    #Resize figures to canvas
    ylag = (height-width)/2
    core.resize(width, width*core.height/core.width)
    core_s.resize(width, width*core_s.height/core_s.width)
    core_s_lig.resize(width, width*core_s_lig.height/core_s_lig.width)
    lig_surf.resize(width, width*lig_surf.height/lig_surf.width)
    sol_surf.resize(width, width*sol_surf.height/sol_surf.width)
    
    #Show figures
    show_plain(core, ylag=ylag)
    show_plain(core_s, ylag=ylag)
    show_plain(core_s_lig, ylag=ylag)
    show_radial_trans(lig_surf, width/5, width/2, 0, 255, ylag=ylag)
    show_radial_trans(sol_surf, width/4, width/2, 0, 115, ylag=ylag)
    #show_radial_trans(sol_surf, width/4, width/2, 0, 75, ylag=ylag)

    
    save("Cover.png")
    
                

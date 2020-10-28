WIDTH = 2490
HEIGHT = 3510#int(WIDTH*1.41)

def setup():
    #Call global variables
    global WIDTH, HEIGHT
    #Set display properties
    noLoop()
    size(WIDTH, HEIGHT)
    background(255,255,255)
    #background(255)
    
def draw():
    #Call global variables
    
    #Place cells
    cells = [[3*width/4, height/2],
             [width/2, height/3.5],
             [width/4, height/2],
             [width/2, 2.9*height/4]]
    
    loadPixels()
    for i in range(height):
        for j in range(width):
            ndx = i*width + j
            dists = []
            for k in range(len(cells)):
                v = cells[k]
                d = dist(j, i, v[0], v[1])
                dists.append(d)
            dists.sort()
            r = map(dists[0], width/3.1, width/2.1, 255, 235)
            g = map(dists[0], width/3.1, width/2.1, 248, 226)
            b = map(dists[0], width/3.1, width/2.1, 200, 173)
            pixels[ndx] = color(r,g,b)
    updatePixels()
    
    #Import images
    core = loadImage("VMD/Cover-core2.png", "png")
    andtop = loadImage("VMD/Cover-andtop.png", "png")
    andbot = loadImage("VMD/Cover-andbot2.png")    
    
    #Resize images
    core.resize (width, height)
    andtop.resize(width, height)
    andbot.resize(width, height)
    
    #Remove backgrounds
    core = remove_background(core)
    andtop = remove_background(andtop)
    andbot = remove_background(andbot)
    
    DD = 10
    F = int(width/4.5)
    Afadein1 = 110 
    Afadein2 = 60 
    Afadeout1 = 190 
    Afadeout2 = 110 
    
    anaglyph(core, RED=255, GREEN=255, BLUE=255, ALP=255, DX=0, DY=3)
    print('Done with core')
    
    anaglyph(andtop, RED=0, GREEN=255, BLUE=255, ALP=Afadein1, DX=DD, DY=0)
    anaglyph(andtop, RED=255, GREEN=0, BLUE=255, ALP=Afadein2, DX=-DD, DY=0)
    print('Done with Top In')
    
    anaglyph(andbot, RED=0, GREEN=255, BLUE=255, ALP=Afadein1, DX=DD, DY=0)
    anaglyph(andbot, RED=255, GREEN=0, BLUE=255, ALP=Afadein2, DX=-DD, DY=0)
    print('Done with Bottom In')
    
    anaglyph(andtop, RED=0, GREEN=255, BLUE=255, ALP=Afadeout1, DX=DD, DY=F)
    anaglyph(andtop, RED=255, GREEN=0, BLUE=255, ALP=Afadeout2, DX=-DD, DY=F)
    print('Done with Top Out')
    
    anaglyph(andbot, RED=0, GREEN=255, BLUE=255, ALP=Afadeout1, DX=DD, DY=-F)
    anaglyph(andbot, RED=255, GREEN=0, BLUE=255, ALP=Afadeout2, DX=-DD, DY=-F)
    print('Done with Bottom Out')
     
    save("Cover.png")

def remove_background(im, bg=color(255)):
    img = im.copy()
    img.loadPixels()
    for i in range(img.height):
        for j in range(img.width):
            ndx = i*img.width + j
            if color(img.pixels[ndx]) == bg:
                img.pixels[ndx] = color(255,1)
    img.updatePixels()
    return img

def anaglyph(img, RED=255, GREEN=255, BLUE=255, ALP=255, DX=0, DY=0):
    edit = img.copy()
    
    img.loadPixels()
    edit.loadPixels()
    for i in range(edit.height):
        for j in range(edit.width):
            ndx = i*edit.width + j
            ndx_src = ((i+DY)%img.height)*img.width + (j+DX)%img.width
            if color(img.pixels[ndx_src]) != color(255,1):
                r = min(RED, red(img.pixels[ndx_src]))
                g = min(GREEN, green(img.pixels[ndx_src]))
                b = min(BLUE, blue(img.pixels[ndx_src]))
                edit.pixels[ndx] = color(r,g,b, ALP)
            else:
                edit.pixels[ndx] = color(255, 1)
    edit.updatePixels()
    img.updatePixels()
    
    image(edit, 0, 0)
    return edit
    

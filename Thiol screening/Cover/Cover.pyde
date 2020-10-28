from Networkize import networkize, argsort

test = False
if test:
    WIDTH = 1000#2490
    HEIGHT = int(WIDTH*1.41)
else:
    WIDTH = 2490
    HEIGHT = 3510 
    
N_cells = 145#80
PN = 0.005

def ligands(im):
    print("Processing ligands...")
    img = im.copy()
    img.loadPixels()
    for i in range(img.height):
        for j in range(img.width):
            noisefactor = map(noise(j*PN, i*PN), 0,1,100,225)
            ndx = i*img.width + j
            rad = dist(j,i,width/2, height/2)
            rad = constrain(rad, width/7, width/3)
            al = map(rad, width/7, width/3, 1,noisefactor)
            r = red(img.pixels[ndx])
            g = green(img.pixels[ndx])
            b = blue(img.pixels[ndx])
            img.pixels[ndx] = color(r,g,b,al)
    img.updatePixels()
    return img

def core(im):
    print("Processing core...")
    global PN
    img = im.copy()
    img.loadPixels()
    for i in range(img.height):
        for j in range(img.width):
            noisefactor = map(noise(j*PN, i*PN), 0,1,0.25,1)
            rad = dist(j,i,width/2, height/2)*noisefactor
            rad = constrain(rad, width/10, width/3.6)
            rad = map(rad, width/10, width/3.6, 255,0)
            ndx = i*img.width + j
            if saturation(img.pixels[ndx]) < 20:
                img.pixels[ndx] = color(255,1)
            else:
                r = red(img.pixels[ndx])
                g = green(img.pixels[ndx])
                b = blue(img.pixels[ndx])
                img.pixels[ndx] = color(r,g,b,rad)
    #img.updatePixels()
    return img

def setup():
    global WIDTH, HEIGHT
    noLoop()
    size(WIDTH, HEIGHT)
    background(255,100,200)
    
def draw():
    cells = []
    while len(cells) < N_cells:
        x, y = int(random(width)), int(random(height))
        good = True
        for cell in cells:
            d = dist(x, y, cell[0], cell[1])
            if d < width/12:
                good = False
        if good:
            cells.append(PVector(x,y))
            print(len(cells))
        
    """bg = createGraphics(width, height)
    bg.beginDraw()
    bg.loadPixels()
    for i in range(height):
        for j in range(width):
            ndx = i*width + j
            dists = []
            for n in range(N_cells):
                v = cells[n]
                d = dist(j, i, v.x, v.y)
                dists.append(d)
            dists.sort()
            r = map(dists[0], 0, width/10, 170, 215)
            g = map(dists[0], width/20, width/8, 2, 75) #110
            b = map(dists[0], width/20, width/5, 90, 70) #120
            bg.pixels[ndx] = color(r,g,b, 150)
        if i%(height/100)==0:
            print("Through {:.1f}% of background".format(float(i)/height*100))
    bg.updatePixels()
    bg.endDraw()
    image(bg,0,0)"""
    
    vmd = loadImage("VMD/Cover1.png", "png")
    lig = loadImage("VMD/LigandSphere.png", "png")
    vmd.resize(width, height)
    lig.resize(width, height)
    lig = ligands(lig)
    
    right = vmd.get(width/2, 0, width/2, height)
    left = right.copy()
    opac = createGraphics(width, height)
    opac.beginDraw()
    opac.pushMatrix()
    opac.translate(left.width,0)
    opac.scale(-1,1)
    opac.image(left,0,0)
    opac.popMatrix()
    opac.image(right, width/2, 0)
    opac.endDraw()
    
    blur = core(opac)
    image(blur, 0, 0)
    image(lig,0,0)
    
    
    #image(opac,0,0)
    
    opac.loadPixels()
    strokeWeight(2.5) #1
    for i, cell in enumerate(cells):
        print("Processing cell {} of {}".format(i, N_cells))
        dists = []
        for pt in cells:
            d = dist(cell.x, cell.y, pt.x, pt.y)
            dists.append(d)
        dists = argsort(dists)
        for n1, n2, n3 in [[0,1,3], [0,2,4], [0,1,2], [0,3,4], [0,5,6]]:
            p1, p2, p3 = cells[dists[n1]], cells[dists[n2]], cells[dists[n3]]
            midp = (p1+p2+p3)/3
            ndxx = int((p1.x+p2.x+p3.x)/3)
            ndxy = int((p1.y+p2.y+p3.y)/3)
            ndx = ndxy*width + ndxx
            r = red(opac.pixels[ndx])
            g = green(opac.pixels[ndx])
            b = blue(opac.pixels[ndx])
            
            rad = dist(midp.x, midp.y, width/2, height/2)
            rad1 = constrain(rad,0,width/2.6) #2.3
            al = map(rad1, 0, width/2.6, 255, 0)
            fill(r,g,b,al)
            rad2 = constrain(rad,0,width/1.5)
            sal = map(rad2, 0, width/1.5, 255, 25)
            stroke(0, sal)
            triangle(p1.x, p1.y, p2.x, p2.y, p3.x, p3.y)
        
    for cell in cells:
        ndx = int(cell.y)*width + int(cell.x)
        r = red(opac.pixels[ndx])
        g = green(opac.pixels[ndx])
        b = blue(opac.pixels[ndx])
        
        rad = dist(cell.x, cell.y, width/2, height/2)
        rad = constrain(rad,0,height/2)
        R = map(rad, 0, height/2, 70, 30) #20 to 10
        al = map(rad, 0, height/2, 255, 0)
        sw = map(rad, 0, height/2, 8,3) #2 to 0.5
        strokeWeight(sw)
        stroke(0, al)
        fill(r,g,b,map(al, 255, 0, 255, 160))
        ellipse(cell.x, cell.y, R, R)

    save('Cover.png')
    print('done')
        
    #networkize(left)
    
    
    
    
    
    
    

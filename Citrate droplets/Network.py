def argsort(seq):
    return sorted(range(len(seq)), key=seq.__getitem__)

def networkize(img, n_nodes=300, n_neigh=4, DY=0, n_rings=7):
    img.loadPixels()
    n_good = 0
    XX, YY, CC, RR = [], [], [], []
    while n_good < n_nodes:
        x = int(random(img.width))
        y = int(random(img.height))
        R = random(15, 80)
        ndx = y*img.width + x
        c = color(img.pixels[ndx])
        sat = saturation(c)
        if sat > -1:
            good = True
            for xx, yy in zip(XX, YY):
                d = dist(x, y, xx, yy)
                if d < 15 :
                    good = False
            if good:
                XX.append(x)
                YY.append(y)
                CC.append(c)
                RR.append(R)
                n_good += 1
                
    for x, y, c, R in zip(XX, YY, CC, RR):
        r = red(c)
        g = green(c)
        b = blue(c)
        dists = []
        for xx, yy in zip(XX, YY):
            dists.append(dist(x,y,xx,yy))
        dists = argsort(dists)
        for dd in dists[:n_neigh]:
            xx = XX[dd]
            yy = YY[dd]
            cc = CC[dd]
            col = (int(0.5*(r+red(cc))), int(0.5*(g+green(cc))), int(0.5*(b+blue(cc))), 30)
            stroke(*col)
            strokeWeight(2)
            #line(x, y+DY, xx, yy+DY)
            
    for x, y, c, R in zip(XX, YY, CC, RR):
        r = red(c)
        g = green(c)
        b = blue(c)
        dr = R/n_rings
        
        for i in range(n_rings):
            a = random(255)
            stroke(r,g,b,a)
            strokeWeight(random(0,3))
            noFill()
            ellipse(x, y+DY, i*dr, i*dr)

        #stroke(0, 0)
        #strokeWeight(1.5)
        #fill(r,g,b,a)
        #ellipse(x, y+DY, R, R)
    img.updatePixels()

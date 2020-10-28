def show_plain(img, ylag=0):
    print("Starting with plain...")
    loadPixels()
    img.loadPixels()
    back = hue(color(0, 255, 0))
    for i in range(img.height):
        for j in range(img.width):
            ndx = i*img.width + j
            ndx_canvas = (i+ylag)*width + j
            r = red(img.pixels[ndx])
            g = green(img.pixels[ndx])
            b = blue(img.pixels[ndx])
            c = color(r, g, b)
            h = hue(c)
            if h != back :
                pixels[ndx_canvas] = c
    updatePixels()
    
def show_radial_trans(img, transin, transout, alphain, alphaout, ylag=0):
    print("Starting with radial_trans...")
    back = hue(color(0, 255, 0))
    img.loadPixels()
    for i in range(img.height):
        for j in range(img.width):
            ndx = i*img.width + j
            ndx_canvas = (i+ylag)*width + j
            r = red(img.pixels[ndx])
            g = green(img.pixels[ndx])
            b = blue(img.pixels[ndx])
            c = color(r,g,b)
            h = hue(c)
            if h != back :
                R = dist(j, i+ylag, width/2, height/2)
                Rc = constrain(R, transin, transout)
                Ra = map(Rc, transin, transout, alphain, alphaout)
                stroke(r,g,b,Ra)
                point(j, i+ylag)

                

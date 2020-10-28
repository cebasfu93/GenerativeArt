def Halo(x0, y0, radius, th_ini, th_fin, iter, imax):
    N_pts = 100
    dt = (th_fin - th_ini)/(N_pts)
    noFill()
    #stroke(255,5,143, 125)
    fiter = iter*255/imax
    stroke(0, fiter)
    strokeWeight(4.0)#map(fiter, 0, 255, 1, 1.8))
    beginShape()
    for i in range(1,2*N_pts+10):
        
        noisefactor = map(noise(i*0.08), 0, 1, 0, 1.8)
        x = x0 +radius*cos(th_ini+i*dt)*noisefactor
        y = y0 +radius*sin(th_ini+i*dt)*noisefactor
        if i> 6:
            curveVertex(x,y)
    endShape()
    

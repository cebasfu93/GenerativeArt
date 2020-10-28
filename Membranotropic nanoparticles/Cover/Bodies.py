from Bricks import Cuadrado, Circulo, Tail

class Solvent:
    def __init__(self,ymin, ymax, nsq, r, nprad, cmin=(0,48,135,255), cmax=(255,255,255,50)):
        thick = abs(ymax-ymin)
        for i in range(nsq):
            cuadrado = Cuadrado(ymin, ymax, r)
            d = abs(cuadrado.mid.y - ymin)
            param = map(d, 0, thick, 0.0, 0.9)
            #d = dist(cuadrado.mid.x, cuadrado.mid.y, width/2, height/2)
            #d = constrain(d, nprad, height/2)
            #param = map(d, nprad, height/2, 0, 1)
            cuadrado.show(ci=cmin, cf=cmax, param=param)
            
class Nano:
    def __init__(self, nprad, r, ncir, cmin=(200,16,46,50), cmax=(255,255,255,255), pn=0.8):
        for i in range(ncir):
            circulo = Circulo(nprad=nprad, r=r, pn=0.8)
            d = dist(circulo.x, circulo.y, width/2, height/2)
            param = map(d, 0, nprad, 0, 1)
            circulo.show(ci=cmin, cf=cmax, param=param)
            
class Leaflet:
    def __init__(self, ntails, yini, randwidth, nbeads=10, beadsize=10, rnp=0, cmin=(170,17,160,255), cmax=(255,255,255,255)):
        for i in range(ntails):
            #yfin = random(min(yini, yini - randwidth), max(yini, yini - randwidth))
            #tail = Tail(yfin=yfin, yini=yini, nbeads=nbeads, r=beadsize)
            ytmp = random(0, height)
            yfin = random(0, height)
            tail = Tail(yfin=yfin, yini=ytmp, nbeads=nbeads, r=beadsize)
            
            d = dist(tail.beads[0].x, tail.beads[0].y, width/2, height/2)
            d = constrain(d, rnp, width/2)
            param = map(d, rnp, width/2, 0, 1)
            tail.show(ci=cmin, cf=cmax, param=param)


import math as math
class Cartesianas:
    def convertirEsfericas(x,y,z):
        print("Las coordenadas cartesiandas del vector P son: (", x, ",", y, ",", z, ").")
        # Sistema de Coordenadas esféricas
        r = math.sqrt((x**2) + (y**2) + (z**2))
        theta = math.atan((math.sqrt((x**2) + (y**2))) / z) 
        #theta = math.atan2((math.hypot(x,y)),z)
        fi = math.atan(y / x)
        #fi = math.atan2(y,x)

        print("Las coordenadas esféricas del vector P son: (", r, ",", theta, ",", fi, ").")

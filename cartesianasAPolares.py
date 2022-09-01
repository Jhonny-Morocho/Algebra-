import math as math
import parte2

class Coordenadas:
    def menuCoordenadas():
        print("Sistema de Coordenadas Cartesianas.")
        print("Vector P(x,y,z).")
        print()
        try:
            x = float(input("Ingrese la coordenada x del vector P:"))
            y = float(input("Ingrese la coordenada y del vector P:"))
            z = float(input("Ingrese la coordenada z del vector P:"))
            ############# PRIMERO PARTE #################
            ############# PRIMERO PARTE #################
            ############# PRIMERO PARTE #################
            print("Las coordenadas cartesiandas del vector P son: (", x, ",", y, ",", z, ").")
            P_modulo = math.sqrt((x**2)+(y**2)+(z**2))
            
            
            print("EL MODULO DEL VECTOR P(x,y,z) ES : ", P_modulo)
            
            
            ############# SEUNDO PARTE #################
            ############# SEUNDO PARTE #################
            ############# SEUNDO PARTE #################
            print( "LAS COORDENDAS ESFERICAS SON: ")
            #enviar valores para la conversion de cartesians a esfericas
            parte2.Cartesianas.convertirEsfericas(x,y,z)
            
            
            ############# TERCERA PARTE #################
            ############# TERCERA PARTE #################
            ############# TERCERA PARTE #################
        except:
            print("Ha ocurrido una expecion")
        



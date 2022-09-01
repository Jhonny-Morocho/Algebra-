import math as math
import parte2
import parte3
class Coordenadas:

    def menuCoordenadas():
        print("Sistema de Coordenadas Cartesianas.")
        print("Vector P(x,y,z).")
        print()
        try:
            x = float(input("1. Ingrese la coordenada x del vector P:"))
            y = float(input("2. Ingrese la coordenada y del vector P:"))
            z = float(input("3. Ingrese la coordenada z del vector P:"))
            ############# PRIMERO PARTE #################
            ############# PRIMERO PARTE #################
            ############# PRIMERO PARTE #################
            print("LAS COORDENADAS INGRESADAS SON LAS SIGUIENTES DEL VECTOR P SON: (", x, ",", y, ",", z, ").")
            P_modulo = math.sqrt((x**2)+(y**2)+(z**2))
            print("##########################################")
            print("EL MODULO DEL VECTOR P(x,y,z) ES : ", P_modulo)
            
            ############# SEUNDO PARTE #################
            ############# SEUNDO PARTE #################
            ############# SEUNDO PARTE #################
            print("##########################################")
            print( "LAS COORDENDAS ESFERICAS A CARTECIANAS SON : ")
            #enviar valores para la conversion de cartesians a esfericas
            parte2.Cartesianas.convertirEsfericas(x,y,z)
            
            
            ############# TERCERA PARTE #################
            ############# TERCERA PARTE #################
            ############# TERCERA PARTE #################
            print("##########################################")
            print( "COORDENADAS ESFERICAS A CARTESIANAS : ")
            parte3.EsfericasCartesianas.convertirEsfericasCartesianas(x,y,z)
        except:
            print("Ha ocurrido una expecion")
       



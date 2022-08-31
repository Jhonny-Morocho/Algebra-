# Libraries
# Math
import math as math


# Global variables


# Functions

	
# Main
print("Sistema de Coordenadas Cartesianas a Sistema de Coordenadas Esféricas.")
print("Vector P(x,y,z) a Vector P(r,theta,fi).")
print()

# Sistema de Coordenadas Cartesianas
x = float(input("Ingrese la coordenada x del vector P:"))
y = float(input("Ingrese la coordenada y del vector P:"))
z = float(input("Ingrese la coordenada z del vector P:"))

print("Las coordenadas cartesiandas del vector P son: (", x, ",", y, ",", z, ").")
print()

P_modulo = math.sqrt((x**2) + (y**2) + (z**2))
# hypot() => Return the Euclidean norm.
#P_modulo = math.hypot(x,y,z)
print("El módulo del vector P(x,y,z) es: ", P_modulo)
print()

# Sistema de Coordenadas esféricas
r = math.sqrt((x**2) + (y**2) + (z**2))
theta = math.atan((math.sqrt((x**2) + (y**2))) / z) 
#theta = math.atan2((math.hypot(x,y)),z)
fi = math.atan(y / x)
#fi = math.atan2(y,x)

print("Las coordenadas esféricas del vector P son: (", r, ",", theta, ",", fi, ").")
print()

# sqrt() => Return the square root.
P_modulo = math.sqrt((r**2) + (theta**2) + (fi**2))
#P_modulo = math.hypot(r,theta,fi)
print("El módulo del vector P(r,theta,fi) es: ", P_modulo)
print()
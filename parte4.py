"""
Executable Python Code:

Execute from terminal as:
$python3 AL_C_S10_E5.py

Powered by Darío Javier Valarezo Leon
"""


# Libraries
# Math
import math as math


# Global variables


# Functions

	
# Main
print("Sistema de Coordenadas Cilíndricas a Sistema de Coordenadas Cartesianas.")
print("Vector P(rho,fi,z) a Vector P(x,y,z).")
print()

# Sistema de Coordenadas Cilíndricas
rho = float(input("Ingrese la coordenada rho del vector P:"))
# 0 <= fi < 2pi
# not((fi >= 0) and (fi < (2 * math.pi))
fi = float(input("Ingrese la coordenada fi del vector P:"))
while not((fi >= 0) and (fi < (2 * math.pi))):
	fi = float(input("Ingrese la coordenada fi del vector P:"))
z = float(input("Ingrese la coordenada z del vector P:"))

print("Las coordenadas cilíndricas del vector P son: (", rho, ",", fi, ",", z, ").")
print()

P_modulo = math.sqrt((rho**2) + (fi**2) + (z**2))
#P_modulo = math.hypot(rho,fi,z)
print("El módulo del vector P(rho,fi,z) es: ", P_modulo)
print()

# Sistema de Coordenadas Cartesianas

x = rho * math.cos(fi)
y = rho * math.sin(fi)

print("Las coordenadas cartesiandas del vector P son: (", x, ",", y, ",", z, ").")
print()

P_modulo = math.sqrt((x**2) + (y**2) + (z**2))
#P_modulo = math.hypot(x,y,z)
print("El módulo del vector P(x,y,z) es: ", P_modulo)
print()

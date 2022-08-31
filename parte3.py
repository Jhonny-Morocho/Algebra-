import math as math


# Global variables


# Functions

	
# Main
print("Sistema de Coordenadas Esféricas a Sistema de Coordenadas Cartesianas.")
print("Vector P(r,theta,fi) a Vector P(x,y,z).")
print()


r = float(input("Ingrese la coordenada r del vector P:"))
# 0 <= theta < pi
# not((theta >= 0) and (theta < math.pi))
theta = float(input("Ingrese la coordenada theta del vector P:"))
while not((theta >= 0) and (theta < math.pi)):
	theta = float(input("Ingrese la coordenada theta del vector P:"))
# 0 <= fi < 2pi
# not((fi >= 0) and (fi < (2 * math.pi))
fi = float(input("Ingrese la coordenada fi del vector P:"))
while not((fi >= 0) and (fi < (2 * math.pi))):
	fi = float(input("Ingrese la coordenada fi del vector P:"))

print("Las coordenadas esféricas del vector P son: (", r, ",", theta, ",", fi, ").")
print()

# sqrt() => Return the square root.
P_modulo = math.sqrt((r**2) + (theta**2) + (fi**2))
# hypot() => Return the Euclidean norm.
#P_modulo = math.hypot(r,theta,fi)
print("El módulo del vector P(r,theta,fi) es: ", P_modulo)
print()

# Sistema de Coordenadas Cartesianas

x = (math.sin(theta) * r) * math.cos(fi)
y = (math.sin(theta) * r) * math.sin(fi)
z = r * math.cos(theta)

print("Las coordenadas cartesiandas del vector P son: (", x, ",", y, ",", z, ").")
print()

# sqrt() => Return the square root.
P_modulo = math.sqrt((x**2) + (y**2) + (z**2))
# hypot() => Return the Euclidean norm.
#P_modulo = math.hypot(x,y,z)
print("El módulo del vector P(x,y,z) es: ", P_modulo)
print()

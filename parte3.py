import math as math

class EsfericasCartesianas:
	def convertirEsfericasCartesianas(x,y,z):
		r = float(x)
		theta = float(y)
		while not((theta >= 0) and (theta < math.pi)):
			theta = float(input("Ingrese la coordenada theta del vector P:"))
		fi = float(z)
		while not((fi >= 0) and (fi < (2 * math.pi))):
			fi = float(input("Ingrese la coordenada fi del vector P:"))

		print("Las coordenadas esféricas del vector P son: (", r, ",", theta, ",", fi, ").")
		print()

		# Sistema de Coordenadas Cartesianas
		x = (math.sin(theta) * r) * math.cos(fi)
		y = (math.sin(theta) * r) * math.sin(fi)
		z = r * math.cos(theta)
		print("Las coordenadas cartesiandas del vector P son: (", x, ",", y, ",", z, ").")

class Usuario:
	def __init__(self, nombre, edad, email):
		self.nombre = nombre
		self.edad = edad
		self.email = email

	def saludar(self):
		print(f'Hola me llamo {self.nombre} y tengo {self.edad}')

	def cumplir_años(self):
		self.edad += 1

andres = Usuario("Andres", 15, "example@e.mx")
print(type(andres))
print(andres.nombre)
print(andres.saludar())

class Cliente(Usuario):
	def __init__(self, nombre, edad, email):
		self.nombre = nombre
		self.edad = edad
		self.email = email
		self.saldo = 0
	def establecer_saldo(self,saldo):
		self.saldo = saldo

	def saludos(self):
		return ("Me llamo {0}, tengo {1} y mi saldo es de ${2}".format(self.nombre, self.edad, self.saldo))

cliente1 = Cliente("Pancha",30,"kjsadhasj@kasdjk.xwi")
cliente1.establecer_saldo(10000)
print(cliente1.saludos())

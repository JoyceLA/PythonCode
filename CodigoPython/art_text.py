import pyfiglet

def imprimir(texto):


	ascii_banner = pyfiglet.figlet_format(texto)
	print(ascii_banner)

	ascii_banner = pyfiglet.figlet_format(texto, font='banner3-D')
	print(ascii_banner)

	ascii_banner = pyfiglet.figlet_format(texto,font='shadow')
	print(ascii_banner)

imprimir(input("Ingresa texto a imprimir:"))

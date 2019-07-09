miArchivo = open("texto.txt","w")


print(miArchivo.name)
print(miArchivo.closed)
print(miArchivo.mode)

miArchivo.write('jqij2f\n')
miArchivo.write('kuygiuhqwd\n')
miArchivo.close()

miArchivo = open("texto.txt","r")
print(miArchivo.read(10))
miArchivo.close()

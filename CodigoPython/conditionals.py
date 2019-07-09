x = 5
y = 25

if (x > y):
	print("%d es mayor que %d" % (x,y))
else:
	print("%d es mayor que %d" % (y,x))

print("----------------------------------------")

if (x > y):
	print("%d es mayor que %d" % (x,y))
elif (x==y):
	print("%d es igual que %d" % (x,y))

else:
	print(f'{y} es mayor que {x}')

if (x > 2):
	if (x <= 10):
		print(f'{x} es mas grande que 2 y menos o igual que 10')


numbers = [1,2,3,4,5]
z = 5

if z in numbers:
	print(f'{z} esta en la coleccion {numbers}')

y = 10
if y not in numbers:
	print(f'{z} no esta en la coleccion {numbers}')

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

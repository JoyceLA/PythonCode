person = ['andres','sofia','alejandra','benita']

print("Simple Loop")

for i in person:
	print(f'Current person: {i}')

print("Break loop")

for p in person:
	if(p == "benita"):
		break
	print(f'Current person: {p}')

for p in person:
	if (p == "sofia"):
		continue
	print(f'Current person: {p}')

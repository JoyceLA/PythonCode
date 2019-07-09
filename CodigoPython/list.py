#A list is a collection which is ordered and changable. Allows duplicate

#Create a list, 1st way to do it
numbers = [1,2,3,4,5]
fruits = ["apples","oranges","grapes","pears"]
#f = open("frutas.txt","r")

#Create a list, use a constructor
numbers2 = list((1,2,3,4,5))

print(numbers, fruits)
#Get a value of a list
print(fruits[0])
# Get length
print(len(fruits))
#append to the list
fruits.append('pineapples')
print(fruits)

fruits.remove('oranges')
print(fruits)

fruits.insert(2,"strawberries")
print(fruits)

fruits.pop(2)
print(fruits)

fruits.reverse()
print(fruits)

fruits.sort()
print(fruits)


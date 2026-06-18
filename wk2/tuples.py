print('Tuples')
x = ('samsung', 'iphone', 'tecno', 'redmi')
print(x)

print('\nFavorite Brand')
favorite=x[1]
print(favorite)

print('\nSecondlast brand')
secondlast= x[-2]
print(secondlast)

print('\nUpdate Iphone to Itel')
x_list=list(x)
x_list[1]='itel'
x=tuple(x_list)
print(x)

print('\nAdd Hawei to tuple')
x=x+('Hawei',)
print(x)

print('\nLoop through tuple')
for y in x:
    print(y)

print('\nDeleting the first value in tuple')
x_list= list(x)
del x_list[0]
x=x_list
print(x)

print('\nUse tuple constructor to make a tuple')
cities=tuple(('masaka', 'kampala', 'jinja', 'gulu', 'mbarara', 'hoima'))
print(cities)

print('\nUnpack tuple')
agriculturecity, capitalcity, nilecity, northcity, cattlecity, minecity= cities
print(agriculturecity)
print(capitalcity)
print(nilecity)
print(northcity)
print(cattlecity)
print(minecity)

print('\nPrint by index in tuple')
print('second city',cities[1])
print('third city',cities[2])
print('fourth city',cities[3])

print('\nFirstnames')
firstnames=('Mark', 'Justine', 'Magret', 'Joe')
print(firstnames)

print('\nLastnames')
lastnames=('Zziwa', 'Namuli', 'Nakachwa', 'Bayiga')
print(lastnames)

print('\nAllnames')
allnames= firstnames+lastnames
print(allnames)

print('\nColours')
colours=('red', 'green', 'blue', 'orange', 'purple', 'yellow')
print(colours)
print('Multiply colours tuple by 3')
coloursby3= colours * 3
print(coloursby3)

print('\nThis Tuple')
thistuple =(1,3,7,8,5,4,6,8,5)
print(thistuple)
eightcount=thistuple.count(8)
print(f'8 appears {eightcount} times in this tuple')
print('Beverages')
beverages = set(['Pepsi', 'Coke', 'Mirinda'])
print(beverages)

print('\nAdding more two')
beverages.update(['Sprite', 'Stoney'])
print(beverages)

print('\nMySet')
mySet = set(['oven', 'kettle', 'microwave', 'refrigerator'])
print(mySet)

print('\nRemove Kettle from set')
mySet.remove('kettle')
print(mySet)

print('\nLoop through set')
for x in mySet:
    print(x)

print('\nAdding a list and a set')
europeCars=set(['BMW', 'Mercedes', 'Audi'])
print(f'Europe Cars= {europeCars}')
englishCars=['Land Rover', 'Range Rover']
print(f'English Cars= {englishCars}')
europeCars.update(englishCars)
print(f'All cars={europeCars}')

print('\nAge and Firstnames')
age=set(['23', '26', '17'])
print(f'ages={age}')
firstnames=set(['Anna', 'John', 'Mary'])
print(f'firstnames={firstnames}')
combinedset=age.union(firstnames)
print(combinedset)

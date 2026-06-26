print('Dictionaries')
Shoes = {
    'brand':'Nike',
    'colour':'Black',
    'size':40
}

print(Shoes)
print(f'Shoe size is {Shoes['size']}')

print('\nChange Nike to Adidas')
Shoes['brand']='Adidas'
print(Shoes)

print('\nAdd type')
Shoes['type']='Sneaker'
print(Shoes)

print('\nDictionary Keys')
shoelist=list(Shoes.keys())
print(shoelist)

print('\nDictionary Values')
shoelist=list(Shoes.values())
print(shoelist)

print('\nCheck size key is in dictionary')
if 'size' in Shoes:
    print('Yes, size is a key in the dictionary')
else:
    print('No, size key doesn\'t exist')

print('\nLoop through the dictionary')
for key, value in Shoes.items():
    print(f'{key} : {value}')

print('\nRemove colour')
remove_colour = Shoes.pop('colour')
print(Shoes)

print('\nEmptying the Dictionary')
Shoes.clear()
print(Shoes)

print('\nMake a copy of a dictionary')
print('car')
car={
    'brand' : 'BMW',
    'model' : '335i',
    'year' : 2016,
    'country' : 'Germany'
}
print(car)
carcopy= car.copy()
print(f'carcopy\n{carcopy}')

print('\nNested dictionaries')
garage={
    'car1':{
        'brand' : 'BMW',
        'model' : '335i',
        'year' : 2018,
        'country' : 'Germany'
    },
    'car2':{
        'brand' : 'Subaru',
        'model' : 'VAB',
        'year' : 2016,
        'country' : 'Japan'
    },
    'car3':{
        'brand' : 'Audi',
        'model' : 'A6',
        'year' : 2022,
        'country' : 'Germany'
    }
}
print(f'Garage\n{garage}')

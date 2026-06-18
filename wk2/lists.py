names= ["Charles", "Milly", "Justine", "Mosses", "Aaron" ]
print(names)
second_name = names[1]
print('the second name is',second_name)

print("\nchange Charles to Alex")
names[0]= "Alex"
print(names)

print("\nadd Ezra to the list")
names.append("Ezra")
print(names)

print("\nadd Bethel in 3rd position")
names.insert(2, "Bathel")
print(names)

print("\nDelete 4th name")
del names[3]
print(names)

last_name = names[-1]
print("\nlastname on list is", last_name)

print("\nCereals")
cereals = ['millet', 'maize', 'sorghum', 'rice', 'wheat', 'barley', 'oats']
print(cereals)
cereal3=cereals[2]
cereal4=cereals[3]
cereal5=cereals[4]
print("the 3rd cereal is", cereal3)
print("the 4rd cereal is", cereal4)
print("the 5rd cereal is", cereal5)

print('\nNations')
nations = ["Kenya", "Uganda", "Tanzania", "Rwanda", "Burundi"]
print(nations)
print('Nations list copy')
nations0 = nations.copy()
print(nations0)

print('\nNations Looped list')
for nation in nations:
    print(nation)

print('\nNation with list index number')
for i in range(len(nations)):
    print(i, nations[i])

print('\Animals')
animals = ['lion', 'zebra', 'crocodile', 'ape', 'giraffe', 'hippo', 'baboon']
print(animals)

print('\n Animals (ascending order)')
animals.sort
print(animals)

print('\n Animals (descending order)')
animals.sort(reverse=True)
print(animals)

print('\nAnimal name start with A')
for animal in animals:
    if animal.lower().startswith('a'):
        print(animal)

print('\nFirstnames')
firstnames=['Mark', 'Justine', 'Magret', 'Joe']
print(firstnames)

print('\nLastnames')
lastnames=['Zziwa', 'Namuli', 'Nakachwa', 'Bayiga']
print(last_name)

print('\nAll Names')
allnames= firstnames+lastnames
print(allnames)




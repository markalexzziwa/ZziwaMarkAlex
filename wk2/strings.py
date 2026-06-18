city='Kampala'
plot=23
result = str(plot) + city
print(result)

print('\nRemove space')
text=' Hello, Uganda '
print(text)
print(text.replace(" ",""))

print('\nUpdate to uppercase')
text='txt'
print(text)
text=text.upper()
print(f'Uppercase\n{text}')

print('\nReplace u with v')
text='t.u.s'
print(f'old text = {text}')
newtext=text.replace('u', 'v')
print(f'new text = {newtext}')

print('\nPrinting range from 2 to 4')
text='I am proudly Ugandan'
result=text[1:4]
print(result)

print('\nCorrected code to print')
x="All 'Data Scientists' are cool!"
print(x)
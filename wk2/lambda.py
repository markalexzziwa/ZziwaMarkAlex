square =lambda x: x*x
print(square(5))
is_even =lambda x: x%2==0
print(is_even(4))
numbers = [4, 7, 10, 15, 20, 30, 35]
evens = list(filter(lambda x: x % 2==0, numbers))
print(evens)

above_20=list(filter(lambda x: x>20, numbers))
print(above_20)
words= ['Cherry', 'Banana', 'Aate', 'Mango', 'DragonFruit']
word_length = sorted(words, key=lambda x: len(x))
print(word_length)
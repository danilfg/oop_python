class Animal:
    color = 'green'
    paws = 4

Animal.paws = 2


cat = Animal()
dog = Animal()
cat.paws = 4
dog.color = 'white'

print(isinstance(cat, Animal))
print(isinstance(dog, Animal))
print()

# print('Paws:', Animal.paws)
# print()
# print('Paws cat:', cat.paws)
# print('Color cat:', cat.color)
print('All attr cat:', cat.__dict__)
print(cat.color)
print(id(cat))

# print()
# print('Paws dog:', dog.paws)
# print('Color dog:', dog.color)
print('All attr dog:', dog.__dict__)
print(dog.paws)

print(id(dog))


# print('All attr:', Animal.__dict__)
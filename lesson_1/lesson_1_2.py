class Animal:
    "Класс для создания животных"
    color = 'green'
    paws = 4


print(Animal.__doc__)
cat = Animal()
dog = Animal()

# cat.meal = "wiskas"

setattr(cat, 'meal', "wiskas")

print(cat.meal)
print(getattr(cat, 'meal'))
print(getattr(cat, 'color'))
print(getattr(cat, 'color_paw', 0))

# del cat.meal
# print(getattr(cat, 'meal', 'атрибут не найден'))

delattr(cat, 'meal')
print(getattr(cat, 'meal', 'атрибут не найден'))



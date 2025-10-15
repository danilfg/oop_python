"""
dander методы
магические методы
"""
class Animal:
    color = 'green'

    def __init__(self, paws: int = 4):
        print('Вызов __init__')
        self.paws = paws

    def __del__(self):
        print("Удаление экземпляра класса:", self)

animal = Animal(6)
del animal
print("Завершение программы")

# print(animal.__dict__)
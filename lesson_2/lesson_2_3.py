class Animal:
    color = 'green'
    instance = None

    def __new__(cls, *args, **kwargs):
        print("Вызов __new__")
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, paws: int = 4):
        print('Вызов __init__')
        self.paws = paws

animal = Animal()
animal_2 = Animal()

print(id(animal))
print(id(animal_2))
print(animal_2 is animal)

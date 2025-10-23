"""
__str__ - print(obj), str(obj) - читаемый вывод
__repr__ - repr(obj) или в консоли - отладочкая информация
__len__ - len(obj) - количество элементов
"""

class Product:
    def __init__(self, prod_id, name, price):
        self.prod_id = prod_id
        self.name = name
        self.price = price

    def __repr__(self):
        return f"<Product id={self.prod_id} name={self.name} price={self.price}>"

    def __str__(self):
        return f"{self.name} - {self.price}"

p = Product(101, "Наушники", 1200)

print(p)
print(str(p))
print(repr(p))

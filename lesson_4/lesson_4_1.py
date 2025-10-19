from datetime import datetime


class BankAccount:
    BANK_NAME = "Daniil Bank" # атрибут класса
    MIN_BALANCE = 0 # атрибут класса

    def __init__(self, owner, balance):
        self.owner = owner # атрибут экземпляра
        self.balance = balance # атрибут экземпляра

    def __getattribute__(self, name):
        print("[LOG] "
              f"{datetime.now().strftime("%d.%m.%Y %H:%M:%S")} "
              f"Доступ к атрибуту: {name}")
        return object.__getattribute__(self, name)

    def __setattr__(self, key, value):
        print("[LOG] "
              f"{datetime.now().strftime("%d.%m.%Y %H:%M:%S")} "
              f"Изменение параметра: {key} на значение: {value}")
        if key == "balance" and value < self.MIN_BALANCE:
            raise ValueError(f"Баланс должен быть больше: {self.MIN_BALANCE}")
        object.__setattr__(self, key, value)

    def __getattr__(self, name):
        print(f"[WARN] "
              f"{datetime.now().strftime("%d.%m.%Y %H:%M:%S")} "
              f"Атрибут '{name}' не найден")
        return None

    def __delattr__(self, name):
        print(f"[LOG] "
              f"{datetime.now().strftime("%d.%m.%Y %H:%M:%S")} "
              f"Удален атрибут '{name}'")
        object.__delattr__(self, name)

    @classmethod
    def set_min_balance(cls, value):
        cls.MIN_BALANCE = value


BankAccount.set_min_balance(-150)
a1 = BankAccount("Daniil", 5000)
# print(a1.balance)
a1.balance = 1000
# print(a1.balance)
# a1.balance = -199
del a1.balance
print(a1.credit)

# a2 = BankAccount("Bob", 10_000)


# print(a1.__dict__)
# print(BankAccount.__dict__)
#
# BankAccount.set_min_balance(-100)
#
# print(a1.MIN_BALANCE)
# print(BankAccount.MIN_BALANCE)

# print(a1.BANK_NAME)
# print(a2.BANK_NAME)
# print(a1.balance)
# print(a2.balance)



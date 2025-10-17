"""
attr - public - публичнный
_attr - protected - защищенный
__attr - private - приватный
"""


class BankAccount:
    MIN_BALANCE = 0
    MAX_BALANCE = 1_000_000

    def __init__(self, owner: str, balance: int):
        self._owner = owner
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount: int):
        self.__balance += amount

    @classmethod
    def demo(cls):
        return cls(owner='Test', balance=10_000)


ba = BankAccount.demo()
# print(ba.get_balance())

print(ba._BankAccount__balance)
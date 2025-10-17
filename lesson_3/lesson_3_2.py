class BankAccount:
    MIN_BALANCE = 0
    MAX_BALANCE = 1_000_000

    def __init__(self, owner: str, balance: int):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: int):
        self.balance += amount

    @classmethod
    def demo(cls):
        return cls(owner='Test', balance=10_000)

    @classmethod
    def validate_balance(cls, balance: int):
        return cls.MIN_BALANCE <= balance <= cls.MAX_BALANCE

    @staticmethod
    def calc_proc(balance: int, rate: int):
        return balance * (rate / 100)

ba = BankAccount.demo()

print(ba.balance)
ba.deposit(-100)
print(ba.balance)

# print(ba.owner)

# print(BankAccount.calc_proc(100, 23))
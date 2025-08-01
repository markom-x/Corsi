class Account:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n

def main():
    account = Account()
    print(account.balance)
    account.deposit(100)
    account.withdraw(50)


if __name__ == "__main__":
    main()

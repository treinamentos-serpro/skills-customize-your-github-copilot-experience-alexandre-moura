# Código a ser testado na atividade de Testes Automatizados com pytest
# Salve como bank_account.py e escreva os testes em test_bank_account.py

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("O valor do depósito deve ser positivo")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("O valor do saque deve ser positivo")
        if amount > self.balance:
            raise ValueError("Saldo insuficiente")
        self.balance -= amount

    def transfer(self, target, amount):
        self.balance -= amount
        target.deposit(amount)


def apply_interest(balance, rate):
    return balance * (1 + rate)

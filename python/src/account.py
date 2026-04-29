from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, account_holder, balance, account_number):
        # TODO: Implement constructor
        # TODO: Initialize a list to track transactions
        self.account_holder = account_holder
        self.balance = balance
        self.account_number = account_number
        self.transactions = []

    def get_account_holder(self):
        # TODO: Implement getter
        return self.account_holder

    def get_balance(self):
        # TODO: Implement getter
        return self.balance

    def set_balance(self, balance):
        # TODO: Implement setter
        if balance < 0:
            print("Invalid Balance")
        else:
            self.balance = balance

    def get_account_number(self):
        # TODO: Implement getter
        return self.account_number

    def credit(self, amount):
        # TODO: Implement credit method (add money to account)
        # TODO: Record this transaction
        if amount < 0:
            print("Invalid Amount")
        else: 
            self.balance += amount
            self.transactions.append(amount)
    
    def debit(self, amount):
        # TODO: Implement debit method (remove money from account)
        # TODO: Record this transaction
        if amount < 0:
            print("Invalid Amount")
        else: 
            self.balance -= amount
            self.transactions.append(amount)

    def get_transactions(self):
        # TODO: Implement method to return transaction history
        return self.transactions

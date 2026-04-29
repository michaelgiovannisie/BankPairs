from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, account_holder, balance, account_number):
        # TODO: Implement constructor
        # TODO: Initialize a list to track transactions
        pass

    def get_account_holder(self):
        # TODO: Implement getter
        return None

    def get_balance(self):
        # TODO: Implement getter
        return None

    def set_balance(self, balance):
        # TODO: Implement setter
        pass

    def get_account_number(self):
        # TODO: Implement getter
        return None

    def credit(self, amount):
        # TODO: Implement credit method (add money to account)
        # TODO: Record this transaction
        pass

    def debit(self, amount):
        # TODO: Implement debit method (remove money from account)
        # TODO: Record this transaction
        pass

    def get_transactions(self):
        # TODO: Implement method to return transaction history
        return None

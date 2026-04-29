from src.account import Account


class CheckingAccount(Account):
    def __init__(self, account_holder, balance, account_number, overdraft_protection):
        super().__init__(account_holder, balance, account_number)
        # TODO: Implement constructor
        self.overdraft_protection = overdraft_protection

    def get_overdraft_protection(self):
        # TODO: Implement getter
        return self.overdraft_protection

    def set_overdraft_protection(self, overdraft_protection):
        # TODO: Implement setter
        self.overdraft_protection = overdraft_protection

    def debit(self, amount):
        # TODO: Implement debit method
        # If overdraft_protection is True, don't allow balance to go negative
        # If overdraft_protection is False, allow balance to go negative
        if self.overdraft_protection and amount > self.balance:
            print("Transaction Declined")
            return
        self.balance -= amount

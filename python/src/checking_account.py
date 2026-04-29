from src.account import Account


class CheckingAccount(Account):
    def __init__(self, account_holder, balance, account_number, overdraft_protection):
        super().__init__(account_holder, balance, account_number)
        # TODO: Implement constructor

    def get_overdraft_protection(self):
        # TODO: Implement getter
        return False

    def set_overdraft_protection(self, overdraft_protection):
        # TODO: Implement setter
        pass

    def debit(self, amount):
        # TODO: Implement debit method
        # If overdraft_protection is True, don't allow balance to go negative
        # If overdraft_protection is False, allow balance to go negative
        pass

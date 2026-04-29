from src.account import Account


class InvestmentAccount(Account):
    def __init__(self, account_holder, balance, account_number, interest_rate):
        super().__init__(account_holder, balance, account_number)
        # TODO: Implement constructor

    def get_interest_rate(self):
        # TODO: Implement getter
        return None

    def set_interest_rate(self, interest_rate):
        # TODO: Implement setter
        pass

    def apply_interest(self):
        # TODO: Implement method to apply interest to the balance
        # New balance = current balance + (current balance * interest rate)
        # Note: Interest applies even to negative balances
        pass

    def debit(self, amount):
        # TODO: Implement debit method
        # Investment accounts do NOT have overdraft protection - allow balance to go negative
        pass

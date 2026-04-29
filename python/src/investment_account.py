from src.account import Account


class InvestmentAccount(Account):
    def __init__(self, account_holder, balance, account_number, interest_rate):
        super().__init__(account_holder, balance, account_number)
        # TODO: Implement constructor
        self.interest_rate = interest_rate

    def get_interest_rate(self):
        # TODO: Implement getter
        return self.interest_rate

    def set_interest_rate(self, interest_rate):
        # TODO: Implement setter
        if interest_rate < 0:
            print("Invalid Interest rate.")
        else:
            self.interest_rate = interest_rate

    def apply_interest(self):
        # TODO: Implement method to apply interest to the balance
        # New balance = current balance + (current balance * interest rate)
        # Note: Interest applies even to negative balances
        interest_amount = self.get_balance() * self.interest_rate
        self.set_balance(self.get_balance() + interest_amount)

    def debit(self, amount):
        # TODO: Implement debit method
        # Investment accounts do NOT have overdraft protection - allow balance to go negative
        self.balance -= amount

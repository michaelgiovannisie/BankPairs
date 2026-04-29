from src.account import Account


class SavingsAccount(Account):
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
        self.balance += (self.balance * self.interest_rate)

    def debit(self, amount):
        # TODO: Implement debit method
        # Savings accounts have overdraft protection - don't allow balance to go negative
        if self.balance - amount >=0:
            self.balance -= amount


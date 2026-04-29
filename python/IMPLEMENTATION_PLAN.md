# Bank Account System — Implementation Plan for Beginners (Python)

## Overview
This document provides a step-by-step guide to implement a bank account system in Python. The project uses **Test-Driven Development (TDD)**, meaning all tests are already written for you. Your job is to make the tests pass by implementing the code.

## Before You Start

### Understanding the Project Structure
```
python/
├── src/
│   ├── person.py             # Individual account holder
│   ├── business.py           # Business account holder
│   ├── account.py            # Abstract base class for all accounts
│   ├── checking_account.py   # Checking account implementation
│   ├── savings_account.py    # Savings account with interest
│   └── investment_account.py # Investment account with interest
└── tests/
    ├── test_person.py
    ├── test_business.py
    ├── test_account.py
    ├── test_checking_account.py
    ├── test_savings_account.py
    └── test_investment_account.py
```

### Running Tests
From inside the `python/` directory:
- Run all tests: `python -m pytest`
- Run specific test: `python -m pytest tests/test_person.py`
- Currently: 53 tests total, all failing (this is expected!)

---

## Implementation Steps

### Step 1: Implement the `Person` Class (Easiest — Start Here!)
**Goal**: Create a class to represent an individual account holder.

**What you need**:
- 4 fields: `first_name`, `last_name`, `email`, `phone_number` (all strings)
- Constructor (`__init__`) to set all fields
- Getters and setters for each field

**Pseudo-code**:
```
CLASS Person:
    FIELDS:
        first_name (str)
        last_name (str)
        email (str)
        phone_number (str)

    CONSTRUCTOR(first_name, last_name, email, phone_number):
        SET self.first_name = first_name
        SET self.last_name = last_name
        SET self.email = email
        SET self.phone_number = phone_number

    METHOD get_first_name():
        RETURN first_name

    METHOD set_first_name(first_name):
        SET self.first_name = first_name

    METHOD get_last_name():
        RETURN last_name

    METHOD set_last_name(last_name):
        SET self.last_name = last_name

    METHOD get_email():
        RETURN email

    METHOD set_email(email):
        SET self.email = email

    METHOD get_phone_number():
        RETURN phone_number

    METHOD set_phone_number(phone_number):
        SET self.phone_number = phone_number
```

**Testing**: After implementing, run `python -m pytest tests/test_person.py`. You should see 9 tests pass! ✓

---

### Step 2: Implement the `Business` Class (Also Easy!)
**Goal**: Create a class to represent a business account holder.

**What you need**:
- 1 field: `business_name` (str)
- Constructor to set the field
- Getter and setter for `business_name`

**Pseudo-code**:
```
CLASS Business:
    FIELDS:
        business_name (str)

    CONSTRUCTOR(business_name):
        SET self.business_name = business_name

    METHOD get_business_name():
        RETURN business_name

    METHOD set_business_name(business_name):
        SET self.business_name = business_name
```

**Testing**: Run `python -m pytest tests/test_business.py`. You should see 3 tests pass! ✓

---

### Step 3: Implement the `Account` Abstract Class (More Complex)
**Goal**: Create the base class that all account types will extend.

**What you need**:
- Fields: `account_holder` (object — can be `Person` or `Business`), `balance` (float), `account_number` (str)
- A list to store transactions
- Constructor to initialize all fields
- Getters and one setter (for `balance`)
- Methods: `credit` (add money), `debit` (subtract money), `get_transactions`

**Pseudo-code**:
```
ABSTRACT CLASS Account:
    FIELDS:
        account_holder (object)
        balance (float)
        account_number (str)
        transactions (list of str)

    CONSTRUCTOR(account_holder, balance, account_number):
        SET self.account_holder = account_holder
        SET self.balance = balance
        SET self.account_number = account_number
        CREATE new list for transactions

    METHOD get_account_holder():
        RETURN account_holder

    METHOD get_balance():
        RETURN balance

    METHOD set_balance(balance):
        SET self.balance = balance

    METHOD get_account_number():
        RETURN account_number

    METHOD credit(amount):
        ADD amount to balance
        ADD "Credit: $" + str(amount) to transactions list

    METHOD debit(amount):
        SUBTRACT amount from balance
        ADD "Debit: $" + str(amount) to transactions list

    METHOD get_transactions():
        RETURN transactions list
```

**Key Concepts**:
- `credit()` increases the balance (deposits)
- `debit()` decreases the balance (withdrawals)
- Track each transaction as a string in the list

**Testing**: Run `python -m pytest tests/test_account.py`. You should see 9 tests pass! ✓

---

### Step 4: Implement the `CheckingAccount` Class (Inheritance!)
**Goal**: Create a checking account that extends `Account` and adds overdraft protection.

**What you need**:
- 1 new field: `overdraft_protection` (bool)
- Constructor that calls the parent (`super()`) constructor
- Getter and setter for `overdraft_protection`
- Override the `debit()` method to check overdraft rules

**Pseudo-code**:
```
CLASS CheckingAccount EXTENDS Account:
    FIELDS:
        overdraft_protection (bool)

    CONSTRUCTOR(account_holder, balance, account_number, overdraft_protection):
        CALL parent constructor with (account_holder, balance, account_number)
        SET self.overdraft_protection = overdraft_protection

    METHOD get_overdraft_protection():
        RETURN overdraft_protection

    METHOD set_overdraft_protection(overdraft_protection):
        SET self.overdraft_protection = overdraft_protection

    OVERRIDE METHOD debit(amount):
        IF overdraft_protection is True:
            IF amount > balance:
                DO NOT allow the transaction (balance stays the same)
                DO NOT record a transaction
            ELSE:
                CALL parent debit method (super().debit(amount))
        ELSE:
            CALL parent debit method (super().debit(amount))
            # This allows negative balance
```

**Key Concepts**:
- `super().__init__(...)` calls the parent class constructor
- `super().debit(amount)` calls the parent class method
- `overdraft_protection = True` → cannot go negative
- `overdraft_protection = False` → can go negative

**Testing**: Run `python -m pytest tests/test_checking_account.py`. You should see 9 tests pass! ✓

---

### Step 5: Implement the `SavingsAccount` Class (Interest Calculations!)
**Goal**: Create a savings account that earns interest and has overdraft protection.

**What you need**:
- 1 new field: `interest_rate` (float)
- Constructor that calls the parent constructor
- Getter and setter for `interest_rate`
- Method to apply interest: `apply_interest()`
- Override `debit()` to prevent overdrafts

**Pseudo-code**:
```
CLASS SavingsAccount EXTENDS Account:
    FIELDS:
        interest_rate (float)

    CONSTRUCTOR(account_holder, balance, account_number, interest_rate):
        CALL parent constructor with (account_holder, balance, account_number)
        SET self.interest_rate = interest_rate

    METHOD get_interest_rate():
        RETURN interest_rate

    METHOD set_interest_rate(interest_rate):
        SET self.interest_rate = interest_rate

    METHOD apply_interest():
        CALCULATE interest_amount = balance * interest_rate
        ADD interest_amount to balance
        # Example: balance = 1000, rate = 0.05
        # interest_amount = 1000 * 0.05 = 50
        # new balance = 1000 + 50 = 1050

    OVERRIDE METHOD debit(amount):
        IF amount > balance:
            DO NOT allow the transaction
            DO NOT record a transaction
        ELSE:
            CALL parent debit method (super().debit(amount))
```

**Key Concepts**:
- Interest formula: `new balance = current balance + (current balance × interest rate)`
- Savings accounts ALWAYS have overdraft protection (cannot go negative)
- Use `set_balance()` method to update the balance after calculating interest

**Testing**: Run `python -m pytest tests/test_savings_account.py`. You should see 11 tests pass! ✓

---

### Step 6: Implement the `InvestmentAccount` Class (Final Class!)
**Goal**: Create an investment account that earns interest but allows overdrafts.

**What you need**:
- 1 new field: `interest_rate` (float)
- Constructor that calls the parent constructor
- Getter and setter for `interest_rate`
- Method to apply interest: `apply_interest()`
- Override `debit()` to allow negative balances

**Pseudo-code**:
```
CLASS InvestmentAccount EXTENDS Account:
    FIELDS:
        interest_rate (float)

    CONSTRUCTOR(account_holder, balance, account_number, interest_rate):
        CALL parent constructor with (account_holder, balance, account_number)
        SET self.interest_rate = interest_rate

    METHOD get_interest_rate():
        RETURN interest_rate

    METHOD set_interest_rate(interest_rate):
        SET self.interest_rate = interest_rate

    METHOD apply_interest():
        CALCULATE interest_amount = balance * interest_rate
        ADD interest_amount to balance
        # Note: Interest applies even if balance is negative!
        # Example: balance = -100, rate = 0.10
        # interest_amount = -100 * 0.10 = -10
        # new balance = -100 + (-10) = -110

    OVERRIDE METHOD debit(amount):
        CALL parent debit method (super().debit(amount))
        # Always allow the transaction, even if it makes balance negative
```

**Key Concepts**:
- Same interest formula as `SavingsAccount`
- NO overdraft protection (can go negative)
- Interest applies to negative balances (makes them more negative!)

**Testing**: Run `python -m pytest tests/test_investment_account.py`. You should see 12 tests pass! ✓

---

## Final Testing

After implementing all classes, from the `python/` directory run:
```bash
python -m pytest
```

You should see:
```
53 passed
```

**Success!** All 53 tests passing! 🎉

---

## Common Beginner Mistakes to Avoid

### 1. Forgetting to assign fields in the constructor
❌ **Wrong**:
```python
def __init__(self, first_name, last_name, email, phone_number):
    pass  # Fields are not set!
```

✅ **Correct**:
```python
def __init__(self, first_name, last_name, email, phone_number):
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.phone_number = phone_number
```

### 2. Forgetting to return values in getters
❌ **Wrong**:
```python
def get_first_name(self):
    pass  # Returns None — tests will fail!
```

✅ **Correct**:
```python
def get_first_name(self):
    return self.first_name
```

### 3. Not calling `super().__init__()` in subclass constructors
❌ **Wrong**:
```python
def __init__(self, account_holder, balance, account_number, overdraft_protection):
    self.overdraft_protection = overdraft_protection
    # Parent fields are not initialized!
```

✅ **Correct**:
```python
def __init__(self, account_holder, balance, account_number, overdraft_protection):
    super().__init__(account_holder, balance, account_number)  # Call parent constructor
    self.overdraft_protection = overdraft_protection
```

### 4. Forgetting to initialize the transactions list
❌ **Wrong**:
```python
def __init__(self, account_holder, balance, account_number):
    self.account_holder = account_holder
    self.balance = balance
    self.account_number = account_number
    # transactions list never created!
```

✅ **Correct**:
```python
def __init__(self, account_holder, balance, account_number):
    self.account_holder = account_holder
    self.balance = balance
    self.account_number = account_number
    self.transactions = []  # Create the list
```

### 5. Accessing balance directly instead of using `get_balance()` / `set_balance()`
❌ **Wrong** (in `apply_interest`):
```python
def apply_interest(self):
    self.balance = self.balance + (self.balance * self.interest_rate)
    # This may work, but bypasses the setter — be consistent with the design!
```

✅ **Correct**:
```python
def apply_interest(self):
    interest_amount = self.get_balance() * self.interest_rate
    self.set_balance(self.get_balance() + interest_amount)
```

---

## Object-Oriented Programming Concepts Used

### Encapsulation
- Private-by-convention fields (prefixed with `_`) with public getters and setters
- This protects data and controls access

### Inheritance
- `CheckingAccount`, `SavingsAccount`, and `InvestmentAccount` all extend `Account`
- They inherit fields and methods from the parent class
- Use `super().__init__()` to call the parent constructor
- Use `super().method_name()` to call parent methods

### Polymorphism
- `account_holder` can be either a `Person` or a `Business`
- Different account types override the `debit()` method differently

### Abstraction
- `Account` is abstract (uses Python's `ABC`) — you can't create an `Account` directly
- You must create a specific type (`CheckingAccount`, `SavingsAccount`, or `InvestmentAccount`)

---

## Tips for Success

1. **Work incrementally**: Complete one class at a time
2. **Test frequently**: Run tests after each implementation
3. **Read error messages**: They tell you exactly what's wrong
4. **Use the tests as documentation**: Read the test files to understand what's expected
5. **Don't modify the test files**: Your job is to make the existing tests pass
6. **Ask for help**: If stuck, review the pseudo-code or ask your instructor/pair partner

---

## Progress Checklist

- [ ] `Person` class implemented (9 tests)
- [ ] `Business` class implemented (3 tests)
- [ ] `Account` class implemented (9 tests)
- [ ] `CheckingAccount` class implemented (9 tests)
- [ ] `SavingsAccount` class implemented (11 tests)
- [ ] `InvestmentAccount` class implemented (12 tests)
- [ ] All 53 tests passing! 🎉

---

## Additional Resources

### Python Syntax Reminders

**Creating a list**:
```python
my_list = []
```

**Adding to a list**:
```python
my_list.append("item")
```

**Calling parent constructor**:
```python
super().__init__(param1, param2)
```

**Calling parent method**:
```python
super().method_name(arguments)
```

**Conditional logic**:
```python
if condition:
    # do something
else:
    # do something else
```

**Abstract class setup**:
```python
from abc import ABC, abstractmethod

class Account(ABC):
    ...
```

### Understanding the Tests

Each test file has comments explaining what it's testing. For example:
- `test_person.py` tests that getters return the correct values
- `test_account.py` tests that credit/debit update the balance correctly
- `test_checking_account.py` tests overdraft protection logic

Read the test names and you'll understand what needs to work!

---

Good luck! Remember: coding is learned by doing. Don't be afraid to try, fail, and try again. That's how you learn! 🚀

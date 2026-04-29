# Unit Tests Guide — Python Track

This project includes comprehensive unit tests to guide your implementation of the bank account system.

## Test Overview

The tests are organised into the following test classes:

### 1. `TestPerson` — `tests/test_person.py` (9 tests)
Tests for the `Person` class which represents an individual account holder with:
- First name, last name, email, phone number
- Getters and setters for all properties

### 2. `TestBusiness` — `tests/test_business.py` (3 tests)
Tests for the `Business` class which represents a business account holder with:
- Business name
- Getter and setter for business name

### 3. `TestAccount` — `tests/test_account.py` (9 tests)
Tests for the abstract `Account` class which includes:
- Account holder (`Person` or `Business`)
- Balance management
- Account number
- Credit and debit operations
- Transaction history tracking

### 4. `TestCheckingAccount` — `tests/test_checking_account.py` (9 tests)
Tests for `CheckingAccount` which extends `Account` and adds:
- **Overdraft protection** — a boolean flag
  - When `True`: Cannot withdraw more than the current balance
  - When `False`: Can overdraw the account (negative balance allowed)

### 5. `TestSavingsAccount` — `tests/test_savings_account.py` (11 tests)
Tests for `SavingsAccount` which extends `Account` and includes:
- **Interest rate** — ability to earn interest
- **Interest application** — `apply_interest()` method that adds interest to balance
- **Overdraft protection** — Always enabled (cannot go negative)

Formula: `new balance = current balance + (current balance × interest rate)`

### 6. `TestInvestmentAccount` — `tests/test_investment_account.py` (12 tests)
Tests for `InvestmentAccount` which extends `Account` and includes:
- **Interest rate** — typically higher than savings accounts
- **Interest application** — `apply_interest()` method
- **No overdraft protection** — Can go negative
- Interest applies even to negative balances

Formula: `new balance = current balance + (current balance × interest rate)`

---

## Running the Tests

Make sure you are inside the `python/` directory first.

**Install dependencies** (first time only):
```bash
pip install -r requirements.txt
```

**Run all tests**:
```bash
python -m pytest
```

**Run a specific test file**:
```bash
python -m pytest tests/test_person.py
python -m pytest tests/test_checking_account.py
```

**Run with verbose output**:
```bash
python -m pytest -v
```

---

## Implementation Strategy

1. **Start with the simple classes**: Implement `Person` and `Business` first
   - These have no dependencies on other classes
   - Run `python -m pytest tests/test_person.py` to verify

2. **Implement the abstract `Account` class**: Create the base functionality
   - Define fields for account holder, balance, account number
   - Implement basic credit/debit operations
   - Add transaction tracking (use a list)

3. **Implement `CheckingAccount`**: Extend `Account`
   - Add `overdraft_protection` field
   - Override `debit()` to respect overdraft protection

4. **Implement `SavingsAccount`**: Extend `Account`
   - Add `interest_rate` field
   - Implement `apply_interest()` method
   - Override `debit()` to prevent overdrafts

5. **Implement `InvestmentAccount`**: Extend `Account`
   - Add `interest_rate` field
   - Implement `apply_interest()` method
   - Keep default `debit()` behaviour (allows overdrafts)

---

## Test-Driven Development (TDD)

The tests are written before the implementation. As you implement each class:

1. Run the tests — they will fail initially
2. Implement the minimal code to make one test pass
3. Run the tests again
4. Repeat until all tests pass

---

## Expected Test Results

Initially, all **53 tests will fail** because the stub implementations only have `TODO` comments.

As you complete the implementation:
- `Person`: 9 tests should pass
- `Business`: 3 tests should pass
- `Account` + `CheckingAccount`: ~18 tests should pass
- `SavingsAccount`: 11 tests should pass
- `InvestmentAccount`: 12 tests should pass

**Goal**: All 53 tests passing ✓

---

## Key Concepts Tested

- **Encapsulation**: Getters and setters for fields
- **Inheritance**: Account subclasses extend the abstract `Account` class
- **Polymorphism**: Account holder can be `Person` or `Business`
- **Business logic**: Overdraft protection, interest calculation
- **State management**: Balance updates, transaction tracking

# Bank Account Pair Coding — Python Track

For this assignment, we're going to pair up and build some bank accounts in Python.

Start with building out your UML for all of this and then go into writing your tests and code.
The UML here should help you simplify your ideas.

You should have:
* An abstract account that has all of the values that non-abstract accounts share.  These should have:
    * an `account_holder`
    * a `balance`
    * an `account_number`
    * A record of every transaction
    * some basic methods that all accounts should share like `credit`, `debit`, getters and setters (where appropriate)

    * A checking account that has the following:
        * An `overdraft_protection` boolean that makes it so the user cannot withdraw more money than they have in their account; if `True` overdraft is not allowed, if `False` overdraft is allowed
    * A savings account that:
        * Gains interest
        * Has overdraft protection
    * An investment account that:
        * Gains interest

Also, there should be two different account holder types:
* `Person` which has a `first_name`, a `last_name`, an `email`, `phone_number`
* `Business` which just has a `business_name`

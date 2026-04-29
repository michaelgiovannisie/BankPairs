package io.zipcoder;

public class CheckingAccount extends Account {
    private boolean overdraftProtection;

    public CheckingAccount(Object accountHolder, Double balance, String accountNumber, boolean overdraftProtection) {
        super(accountHolder, balance, accountNumber);
        // TODO: Implement constructor
        this.overdraftProtection = overdraftProtection;
    }

    public boolean getOverdraftProtection() {
        // TODO: Implement getter
        return overdraftProtection;
    }

    public void setOverdraftProtection(boolean overdraftProtection) {
        // TODO: Implement setter
        this.overdraftProtection = overdraftProtection;
    }

    @Override
    public void debit(Double amount) {
        // TODO: Implement debit method
        // If overdraftProtection is true, don't allow balance to go negative
        // If overdraftProtection is false, allow balance to go negative
        if(this.overdraftProtection) {
            if(amount > getBalance()) {
                System.out.println("Transaction declined.");
                return;
            } else {
                super.debit(amount);
            }
        } else {
            super.debit(amount);
        }
    }

    // OVERRIDE METHOD debit(amount):
    //     IF overdraftProtection is TRUE:
    //         IF amount > balance:
    //             DO NOT allow the transaction (balance stays the same)
    //             DO NOT record a transaction
    //         ELSE:
    //             CALL parent debit method (super.debit(amount))
    //     ELSE:
    //         CALL parent debit method (super.debit(amount))
    //         # This allows negative balance
}

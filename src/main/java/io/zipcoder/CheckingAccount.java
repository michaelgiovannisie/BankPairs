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
        if(this.overdraftProtection && amount >= getBalance()alance()) {
            System.out.println("Transaction Declined");
            return;            System.out.println("Transaction Declined");
         
        double newBalance = getBalance() - amount;   return;
        }
        double newBalance = getBalance() - amount;
    }
}

package io.zipcoder;

public class Person {
    private String firstName;
    private String lastName;
    private String email;
    private String phoneNumber;

    public Person(String firstName, String lastName, String email, String phoneNumber) {
        // TODO: Implement constructor
        this.firstName = firstName;
        this.lastName = lastName;
        this.email = email;
        this.phoneNumber = phoneNumber;
    }

    public String getFirstName() {
        // TODO: Implement getter
        return firstName;
    }

    public void setFirstName(String firstName) {
        // TODO: Implement setter
        if(firstName != null && !firstName.isEmpty()) {
            this.firstName = firstName;
        } else {
            System.out.println("Invalid input");
        }
    }

    public String getLastName() {
        // TODO: Implement getter
        return lastName;
    }

    public void setLastName(String lastName) {
        // TODO: Implement setter
        if(lastName != null && !lastName.isEmpty()) {
            this.lastName = lastName;
        } else {
            System.out.println("Invalid input");
        }
    }

    public String getEmail() {
        // TODO: Implement getter
        return email;
    }

    public void setEmail(String email) {
        // TODO: Implement setter
        if(email != null && !email.isEmpty()) {
            this.email = email;
        } else {
            System.out.println("Invalid input");
        }
    }

    public String getPhoneNumber() {
        // TODO: Implement getter
        return phoneNumber;
    }

    public void setPhoneNumber(String phoneNumber) {
        // TODO: Implement setter
        if(phoneNumber != null && !phoneNumber.isEmpty()) {
            this.phoneNumber = phoneNumber;
        } else {
            System.out.println("Invalid input");
        }
    }
}

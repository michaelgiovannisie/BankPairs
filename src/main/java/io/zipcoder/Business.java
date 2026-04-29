package io.zipcoder;

public class Business {
    private String businessName;

    public Business(String businessName) {
        // TODO: Implement constructor
        this.businessName = businessName;
    }

    public String getBusinessName() {
        // TODO: Implement getter
        return businessName;
    }

    public void setBusinessName(String businessName) {
        // TODO: Implement setter
        if(businessName != null && !businessName.isEmpty()) {
            this.businessName = businessName;
        } else {
            System.out.println("Invalid input");
        }
    }
}

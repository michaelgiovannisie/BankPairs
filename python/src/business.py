class Business:
    def __init__(self, business_name):
        # TODO: Implement constructor
        self.business_name = business_name

    def get_business_name(self):
        # TODO: Implement getter
        return self.business_name

    def set_business_name(self, business_name):
        # TODO: Implement setter
        if business_name == None or business_name == "":
            print("Invalid Business Name.")
        else:
            self.business_name = business_name

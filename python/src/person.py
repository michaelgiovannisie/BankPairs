class Person:
    def __init__(self, first_name, last_name, email, phone_number):
        # TODO: Implement constructor
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number

    def get_first_name(self):
        # TODO: Implement getter
        return self.first_name

    def set_first_name(self, first_name):
        # TODO: Implement setter
        if first_name == None or first_name == "":
            print("Invalid First Name.")
        else:
            self.first_name = first_name

    def get_last_name(self):
        # TODO: Implement getter
        return self.last_name

    def set_last_name(self, last_name):
        # TODO: Implement setter
        if last_name == None or last_name == "":
            print("Invalid Last Name.")
        else:
            self.last_name = last_name

    def get_email(self):
        # TODO: Implement getter
        return self.email

    def set_email(self, email):
        # TODO: Implement setter
        if email == None or email == "":
            print("Invalid Email.")
        else:
            self.email = email

    def get_phone_number(self):
        # TODO: Implement getter
        return self.phone_number

    def set_phone_number(self, phone_number):
        # TODO: Implement setter
        if phone_number == None or phone_number == "":
            print("Invalid Phone Number.")
        else:
            self.phone_number = phone_number

import re
class ValidationError(Exception):
    def __init__(self,msg):
        super().__init__(msg)

class PersonDetails:
    def __init__(self,first_name,last_name,email,mobile_no,password):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.mobile_no=mobile_no
        self.password=password
    
    def valid_first_name(self):

        if not re.match("[A-Z][a-z,A-Z]{2,}$",self.first_name):
            raise ValidationError(f'{self.first_name}this is not valid first name \n first_name should  starts with capital letter and should be more than 2 letters!')
        print(f'first name is:{self.first_name}')
    
    def valid_last_name(self):
       
        if not re.match("[A-Z][a-z,A-Z]{2,}$",self.last_name):
            raise ValidationError(f'{self.last_name} this is not valid last name ')
        print(f'last name is:{self.last_name}')
    
    def valid_email(self):

        if not re.match(r'abc+(\.[a-zA-Z]+)?@bl\.co\.[a-zA-Z]{2,}$',self.email):
            raise ValidationError(f'{self.email} this is not valid email!!')
        print(f'email:{self.email}')
    
    def valid_mobile_no(self):
        if not re.match(r'[0-9]{2} [0-9]{10}$',self.mobile_no):
            raise ValidationError(f'{self.mobile_no} this is not valid mobile number!')
        print(f'mobile number:{self.mobile_no}')


    def Valid_password(self):

        if not re.match(r'^(?=.*[A-Z])(?=.*[0-9])(?=.*[@#*$&])[a-zA-Z0-9@#$*&]{8,}$',self.password):
            raise ValidationError(f'{self.password} give an strong password')
        print("password:",self.password)
    def exception_handling(self):
        try:
            self.valid_first_name()
        except ValidationError as e:
            print(e)
        try:
            self.valid_last_name()
        except ValidationError as e:
            print(e)
        try:
            self.valid_email()
        except ValidationError as e:
            print(e)
        try:
            self.valid_mobile_no()
        except ValidationError as e:
            print(e)
        try :
            self.Valid_password()
        except ValidationError as e:
            print(e)
pd=PersonDetails("Ram","Reddy","Ram@gmail.com","91 9392540901","123456")
pd.exception_handling()
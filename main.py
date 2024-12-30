

import re
class PersonDetails:
    def __init__(self,first_name,last_name,email,mobile_no,password):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.mobile_no=mobile_no
        self.password=password
    def rgex(self):
        #first_name
        if re.match(r'^[A-Z][a-zA-Z]{2,}$',self.first_name):
            print(f'Your first name is:{self.first_name}')
        else:
            print("Enter the valid first_name,aggain:")
        #last_name
        if re.match(r'^[A-Z][a-zA-z]{2,}',self.last_name):
            print(f'your last name is {self.last_name}')
            print(f'your full name is : {self.first_name + " "+ self.last_name}')
        else:
            print("Enter the last name again!!")
            obj=PersonDetails("Ram","Reddy")
        #emial
        if re.match(r'abc+(\.[a-zA-Z]+)?@bl\.co\.[a-zA-Z]{2,}$',self.email):
            print(f'your email:{self.email}')
        else:
            print("your email is not valid ,, enter again")
        
        #mobile_no
        if re.match(r'[0-9]{2} [0-9]{10}$',self.mobile_no):
            print(f'your mobile_no is : {self.mobile_no}')
        else:
            print("Enter valid mobile number")
        
        #password

        if re.match(r'[a-zA-z0-9@#$*&]{8,}$',self.password):
            print(f'your password is :{self.password}')
        else:
            print("invalid password enter again.")

obj=PersonDetails("Ram","Reddy","abc.xyzzzxxxx@bl.co.in","91 9392540901","@ram123456")
obj.rgex()
import re
class PersonDetails:
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
    def rgex(self):
        if re.match(r'^[A-Z][a-zA-Z]{2,}$',self.first_name):
            print(f'Your first name is:{self.first_name}')
        else:
            print("Enter the valid first_name,aggain:")
        
        if re.match(r'^[A-Z][a-zA-z]{2,}',self.last_name):
            print(f'your last name is {self.last_name}')
            print(f'your full name is : {self.first_name + " "+ self.last_name}')
        else:
            print("Enter the last name again!!!")
obj=PersonDetails("Ram","Reddy")
obj.rgex()
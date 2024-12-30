import re
class PersonDetails:
    def __init__(self,first_name):
        self.first_name=first_name
    def rgex(self):
        if re.findall(r'^[A-Z][a-zA-Z]{2,}$',self.first_name):
            return self.first_name
        else:
            return "Enter the valid first_name,aggain:"
    
obj=PersonDetails("Ram")
name=obj.rgex()
print(name)
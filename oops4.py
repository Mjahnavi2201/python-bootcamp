#Encapsulation
class Employee:
    def __init__(self,name,role,salary):
        self.name=name
        self.role=role
        self.__salary=salary #'__' is used for private so the data is private
    def get_salary(self):
        return self.__salary #private can be accessed only inside class
    def empdisplay(self):
        print(self.name,self.role,self.__salary) #public method
class Company(Employee):
    def __init__(self,cname,loc):
        self.cname=cname
        self.loc=loc
    def comdisplay(self):
        print(self.cname,self.loc)
    def _hiring(self):
        print('hiring for manager post') #protected method
cobj=Company('Jahnavi','Hyd')
cobj._hiring()
cobj.comdisplay()
eobj=Employee('Jahnavi','Developer',1000000)
print(eobj.get_salary())
eobj.empdisplay()
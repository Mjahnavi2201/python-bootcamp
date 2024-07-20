'''
#parameterized constructor
#Student Example
class Student:
    def __init__(self,name,roll,branch,address,email):
        self.name=name
        self.roll=roll
        self.branch=branch
        self.address=address
        self.email=email
    def display(self):
        print("Name:",self.name)
        print("Roll:",self.roll)
        print("Branch:",self.branch)
        print("Adress:",self.address)
        print("Email:",self.email)
s1=Student('M.Jahnavi','21D21A05A1','CSE','Hyderabad','m.jahnavi1@gmail.com')
s1.display()
#Employee Example
class Employee:
    def __init__(self,name,eid,des,address,email):
        self.name=name
        self.eid=eid
        self.des=des
        self.address=address
        self.email=email
    def display(self):
        print("Name:",self.name)
        print("Roll:",self.eid)
        print("Designation:",self.des)
        print("Adress:",self.address)
        print("Email:",self.email)
e1=Employee('M.Jahnavi',1234567,'programmer','Hyderabad','m.jahnavi1@gmail.com')
e1.display()
'''
'''
MEMORY ALLOCATION:
-str-8 bytes
-int-4 bytes
so total 36 bytes are allocated for Employee and 40 bytes are allocated for Student
'''
'''
Static:
-it is used for memory management
-creating only one data,property and passing to all objects which are common
-instead of creating individual data for common data,create a static data and pass the copy to all objects
'''
'''
#to reduce space take static data(doesn't change)
#static example1
#Student Example
class Student:
    #static data 
    branch='CSE'
    def __init__(self,name,roll,address,email):
        self.name=name
        self.roll=roll
        self.address=address
        self.email=email
    def display(self):
        print("Name:",self.name)
        print("Roll:",self.roll)
        print("Branch:",Student.branch)
        print("Adress:",self.address)
        print("Email:",self.email)
s1=Student('M.Jahnavi','21D21A05A1','Hyderabad','m.jahnavi1@gmail.com')
s1.display()
'''
'''
#static example2
#project Example
class Project:
    name='data mining'
    pid=512
    def __init__(self,ename,eid,email):
        self.ename=ename
        self.eid=eid
        self.email=email
    def display(self):
        print("Employee Name:",self.ename)
        print("Employee id:",self.eid)
        print("Employee email:",self.email)
        print("Project Name:",Project.name)
        print("Project id:",Project.pid)
p1=Project('M.jahnavi',102,'m.jahnavi1@gmail')
p2=Project('N.gouthami',103,'n.gouthami@gmail.com')
p1.display()
p2.display()
'''
'''
#displaying output without display function
class Student:
    #static data 
    branch='CSE'
    def __init__(self,name,roll,address,email):
        self.name=name
        self.roll=roll
        self.address=address
        self.email=email
    def __str__(self):
        return f'{self.name} {self.roll} {Student.branch} {self.address} {self.email}'
s1=Student('M.Jahnavi','21D21A05A1','Hyderabad','m.jahnavi1@gmail.com')
print(s1)
'''
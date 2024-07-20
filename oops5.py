#POLYMORPHISM
#Polymorphism with inheritance
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f'{self.name},{self.age}'
class Student(Person):
    def __init__(self,name,age,roll,branch):
        super().__init__(name,age)
        self.roll=roll
        self.branch=branch
    def __str__(self):
        persondetails=super().__str__()
        return f'{persondetails},{self.roll},{self.branch}'
class AnnualDay(Student):
    def __init__(self,name,age,roll,branch,program):
        super().__init__(name,age,roll,branch)
        self.program=program
    def __str__(self):
        studentdetails=super().__str__()
        return f'{studentdetails},{self.program}'
aobj=AnnualDay('Jahnavi',20,101,'CSE','Solo')
print(aobj)
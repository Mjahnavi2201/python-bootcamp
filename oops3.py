#Abstract classes (non-abstract:concrete)
from abc import ABC
class RBIBANK(ABC):
    def interest(self):
        pass #abstract method
    def loan(self):
        print("Provides Home loan") #concrete method
class HDFC(RBIBANK):
    def interest(self):
        print('7.5% interest')
class SBI(RBIBANK):
    def interest(self):
        print('11% interest')
class BOB(RBIBANK):
    def interest(self):
        print('13% interest')
h1=HDFC()
h1.loan()
h1.interest()
s1=SBI()
s1.loan()
s1.interest()
b1=BOB()
b1.loan()
b1.interest()
#Example for abstract and concrete
class Laptop(ABC):
    def name(self):
        pass
    def ram(self):
        pass
    def processor(self):
        print("Intel core i7")
class Lenovo(Laptop):
    def name(self):
        print("Laptop Name:Lenovo")
    def ram(self):
        print("RAM:16GB")
class MSI(Laptop):
    def name(self):
        print("Laptop Name:MSI")
    def ram(self):
        print("RAM:8GB")
class HP(Laptop):
    def name(self):
        print("Laptop Name:HP")
    def ram(self):
        print("RAM:16GB")
l1=Lenovo()
l2=MSI()
l3=HP()
l1.name()
l1.ram()
l1.processor()
l2.name()
l2.ram()
l2.processor()
l3.name()
l3.ram()
l3.processor()
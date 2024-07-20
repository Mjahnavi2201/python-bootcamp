#Single Inheritance
class JNTU:
    def schedule_academic(self):
        print("Scheduling Academics")
    def declare_holidays(self):
        print('National and Summer Holidays')
    def results(self):
        print('go to www.jntuhresults.com')
class SriDevi(JNTU):
    def fees(self):
        print('3rd year fee is 85k')
jobj=JNTU()
jobj.results()
#jobj.fees()
s1=SriDevi()
s1.fees()
s1.schedule_academic()
s1.declare_holidays()
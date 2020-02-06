class Company:

    _count=0

    @classmethod
    def disp_cnt(cls):
        cls._count=cls._count+1
        return cls._count

    @staticmethod
    def company_details():
        name='Accenture'
        loc='Chennai'
        return name,loc
    
class Employee(Company):

    def __init__(self,name='',id=0):
        if id>0:
            self.id=id
            Company.disp_cnt()
        else:
            self.id=Company.disp_cnt()
        self.name=name

    def setId(self,id):
        self.id=id

    def setName(self,name):
        self.name=name

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def grossSalCalc(self,basicPay):
        gross_salary = basicPay + (10 * basicPay) / 100 + (12 * basicPay) / 100
        return self.id,self.name,gross_salary

name,loc=Employee.company_details()
print('Company Name:',name)
print('Location:',loc)

e1=Employee('Subbu',121)

e2=Employee('surudhi')

e3=Employee()
e3.setId(143)
e3.setName('sudee')

print('Id -  name  : gross salary')

id1,name1,gs1=e1.grossSalCalc(20000)
print(id1,'-',name1,':',gs1)

id2,name2,gs2=e2.grossSalCalc(25000)
print(id2,'-',name2,':',gs2)

id3,name3,gs3=e3.grossSalCalc(22000)
print(id3,'-',name3,':',gs3)
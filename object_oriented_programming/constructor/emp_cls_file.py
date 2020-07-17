class Employee:
    def __init__(self,eid,name,desig,sal,exp):
        self.eid=eid
        self.name=name
        self.desig=desig
        self.sal=sal
        self.exp=exp
    def printEmp(self):
        print(self.eid,",",self.name,",",self.desig,",",self.sal,",",self.exp)

f=open("C:/Users/user/PycharmProjects/pythonclass/object_oriented_programming/constructor/emp.txt")
emp=[]
for data in f:
    #print(data)
    employee=data.rstrip("\n").split(",")
    eid=employee[0]
    name=employee[1]
    desig=employee[2]
    sal=int(employee[3])
    exp=employee[4]
    ob=Employee(eid,name,desig,sal,exp)
    ob.printEmp()
    emp.append(ob)
#######to print employee name with salary>17000
for employee in emp:
    #print(employee.eid)
    if(employee.sal>17000):
        print(employee.name)
###########convert emplyee name to uppercase
for employee in emp:
    name=employee.name
    print(name.upper())
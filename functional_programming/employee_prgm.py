#QUESTION
#convert employee name to upper case
#print emplyee salary greater than 15000
#provide increment of 5000 for all employee who mhave experience greater than or equal to 2
#list all employees designation=developer

class Employee:
    def __init__(self,eid,name,desig,sal,exp):
        self.eid=eid
        self.name=name
        self.desig=desig
        self.sal=sal
        self.exp=exp
    def printEmp(self):
        print(self.eid,",",self.name,",",self.desig,",",self.sal,",",self.exp)
f=open("employee","r")
emp=[]
for data in f:
    #print(data)
    employee=data.rstrip("\n").split(",")
    eid=employee[0]
    name=employee[1]
    desig=employee[2]
    sal=int(employee[3])
    exp=int(employee[4])
    ob=Employee(eid,name,desig,sal,exp)
    ob.printEmp()
    emp.append(ob)

#convert employee name to upper case
uppercase=list(map(lambda Employee:Employee.name.upper(),emp))
print("NAME IN UPPER CASE")
print(uppercase)
#print emplyee salary greater than 15000
salary=list(filter(lambda Employee:Employee.sal>17000,emp))
print("SALARY >17000")
for val in salary:
    print(val.name)
#provide increment of 5000 for all employee who have experience>= 2
incrmnt=list(filter(lambda Employee:Employee.exp>=2,emp))
for i in incrmnt:
    print("Employee Name:",i.name,"Previous Salary:",i.sal)
    sal=i.sal+5000
    print("New Salary:",sal)
#list all employees designation=developer
dev=list(filter(lambda Employee:Employee.desig=="developer",emp))
print("EMPLOYEE WHOSE DESIGNATION IS DEVELOPER")
for j in dev:
    print(j.name)
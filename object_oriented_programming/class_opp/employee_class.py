#employee=>name,id,designation,company_name,salary
#set
#print

class Employee:
    def set_value(self,id,name,desig,company,salary):
        self.id=id
        self.name=name
        self.desig=desig
        self.company=company
        self.salary=salary
    def print_value(self):
        print("id:",self.id)
        print("name:",self.name)
        print("desig:",self.desig)
        print("company:",self.company)
        print("salary:",self.salary)

ob=Employee()
ob.set_value(100,"mohamed","developer","abc",25000)
ob.print_value()

ob1=Employee()
ob1.set_value(101,"safeer","designer","xyz",30000)
ob1.print_value()
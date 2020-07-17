'''class Student:
    def stuDetails(self,name,roll,course):
        #stuDetails is used to initialize variable
        self.name=name
        self.roll=roll
        self.course=course
    def printDetails(self):
        print(self.name,",",self.roll,",",self.course)

ob=Student()
ob.stuDetails("ajay",101,"mca")
ob.printDetails()'''

##############CONSTRUCTOR
class Student:
    def __init__(self,name,roll,course):
        #constructor is also used to initialize variable
        #by default it is "__init__" method
        self.name=name
        self.roll=roll
        self.course=course

    def printDetails(self):
            print(self.name, ",", self.roll, ",", self.course)

#we dont need to call the init method,can directly pass objects in class
ob = Student("ajay",101,"mca")
ob.printDetails()
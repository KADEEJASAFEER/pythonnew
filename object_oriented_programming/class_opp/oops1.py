#class
#object
#reference


#create class
#class ClassName:
#        methods

class Person:
#method
    def setValues(self,age,name):
        self.age=age
        self.name=name
    def printValues(self):
        print("name:",self.name)
        print("age:",self.age)
#reference name=classname()
ob=Person()
ob.setValues(25,"jini")
ob.printValues()

#different types of vaariable
#instance variable instance means related to object
#local variables
#class or static variable


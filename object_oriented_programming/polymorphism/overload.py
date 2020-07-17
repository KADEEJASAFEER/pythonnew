#polymorphism
#method overloading
#method overridding
#operator overloading

#method overloading:
# same method but differnt number of arguments

class mathop:
    def add(self):
        print("inside no argument")
    def add(self,num1):
        print("inseide 1 argument method")
    def add(self,num1,num2):
        print("inside 2 argument method")
    def add(self,num1,num2,num3):
        print("inside arg 4")

ob=mathop()
ob.add(10,20,30)
#ob.add()   #error
#python does not support method overloading
#it considers only the last method

#####CONSTRUCTOR OVERLOADING
'''class mathop:
    def __init__(self):
        print("inside default constructor")
    def __init__(self,num1):
        print("inside single argument constructor")
    
ob=mathop(10,20,30)
#here also support only last method passed'''
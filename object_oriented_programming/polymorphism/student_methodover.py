'''#base class
class object:
    def __str__(self):
        pass
    '''

class Student:
    def __init__(self,name,roll,course):
        self.name=name
        self.roll=roll
        self.course=course

    def printDetails(self):
            print(self.name, ",", self.roll, ",", self.course)

    def __str__(self):
        return self.name
ob = Student("ajay",101,"mca")
#ob.printDetails()
print(ob)    #<__main__.Student object at 0x003DB100>
#returns the memory of ob
#when ob is printed is works a new method automatically
#def __str(self):
#pass

#there is a base class for every class we create
#so the def __str() method works from that object class

#to create our own definition
#def __str__(self):
#    return self.name
#we need to return a string

#method overrriding works with different class


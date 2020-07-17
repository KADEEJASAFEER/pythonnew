class book:
    def __init__(self,pages):
        self.pages=pages

    def __add__(self, other):
        return  (self.pages+other.pages)

    def __sub__(self, other):
        return (self.pages - other.pages)

    def __mul__(self, other):
        return (self.pages * other.pages)

    def __divmod__(self, other):
        return (self.pages / other.pages)

    def __str__(self):
        return str(self.pages)
    #this should return a string


b=book(100)
b1=book(200)
#print(b)
#print(type(b))     #<class '__main__.book'>
#b1=book(200)
#print(b+b1) #error since b and b1 are type class or bookobject
#needs to overrides objects: b and b1
#to need to add 2 objects we need new definition
'''    def __add__(self, other):
        return  (self.pages+other.pages)'''

#print(b+b1) #300

#for subtraction
#print(b1-b)

#for multiplication
#print(b*b1)

#for division
#print(b1//b)

#b2=book(300)
#print(b+b1+b2)
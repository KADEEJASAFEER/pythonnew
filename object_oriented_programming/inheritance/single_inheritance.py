#inheritance
'''class Parent:
    def phone(self):
        print("parent have nokia phone")


class Child(Parent):
    pass
#child class inheritance proprty of parent class
#so child class can acquire property of parent class

c=Child()
c.phone()       '''

class Parent:
    def phone(self):
        print("parent have nokia phone")


class Child(Parent):
    def phone2(self):
        print("child has iphone")

p=Parent()
#p.phone()
#p.phone2 will execute error
#parent class cnt access property of child class

c=Child()
c.phone2()
c.phone()
#single inheritance=>with single parent class and child class
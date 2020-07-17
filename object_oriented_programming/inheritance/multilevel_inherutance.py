#MULTILEVEL INHERITANCE
class p1:
    def m1(self):
        print("inside parent1")
class p2(p1):
    def m2(self):
        print("inside parent2")
class p3(p2):
    def m3(self):
        print("inside parent3")

ob1=p3()
#if we need to inherit the values need to connect p1 &p2
ob1.m3()
ob1.m2()
ob1.m1()

ob2=p2()
ob2.m2()
ob2.m1()
#ob2.m3()

ob3=p1()
ob3.m1()

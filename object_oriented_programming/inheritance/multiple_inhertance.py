#MULTIPLE INHERITANCE
class p1:
    def m1(self):
        print("inside parent1")
class p2:
    #def m1(self):
     #   print("inside parent1-2")
    def m2(self):
        print("inside parent2")
class p3(p2,p1):
    def m3(self):
        print("inside parent3")

ob1=p3()
#if we need to inherit the values need to connect p1 &p2
#p3 can invoke both p1 &p2
#ob1.m3()
#ob1.m2()
#ob1.m1()
#p2 can inherit only that method
P2=p2()
#p2.m2()
#m1 metgod in both p1 and p2 so java does not support multiple inhertance
#but python supports
a=p3()
a.m3()
#a.m2()
a.m2()
a.m1()
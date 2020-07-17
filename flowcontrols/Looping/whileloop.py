#initialization
#i=0
 #condition
#while(i<10):
   # print("hello")
 #increment
   # i+=1
##############
#??? program to print 0 to 10
'''i=1
while(i<=10):
    print(i)
    i+=1'''
 ################
 #  prgm to print nmbrs in reverse
#i=10
#while(i>=0):
 #   print(i)
  #  i-=1
#######################
#?? prgm to print up to a range
#num=int(input("enter a num:"))
#i=0
#while(i<=num):
 #   print(i)
  #  i+=1
#######################
#?? prgm to print between two numbers
#llimit=int(input("enter a lower limit:"))
#ulimit=int(input("enter a upper limit:"))
#i=llimit;
#while(llimit<=ulimit):
#    print(llimit)
#    llimit+=1
#######################
 # ?? prgm to print even nmbrs up to a range
#limit=int(input("enter limit"))
#i=1
#while(i<=limit):
 #   if(i%2==0):
#        print(i)
 #   i+=1
#######################
 # ?? prgm to calculate sum of n numbers
#n=int(input("enter limit:"))
#i=0
#sum=0
#while(i<=n):
#    sum=sum+i
#    i+=1
#print(sum)
#######################
 # ?? prgm to find sum of even nmbrs and odd nmbrs in a range
#n=int(input("enter limit:"))
#i=0
#evensm=0
#oddsm=0
#while(i<=n):
#    if(i%2==0):
#        evensm=evensm+i
#   else:
#       oddsm=oddsm+i
#    i+=1
#print("evensm:",evensm)
#print("oddsum",oddsm)
#######################
# ?? prgm to convert 123 to 321(PALINDROME)
#num=int(input("enter a number"))
#rev=0
#while(num>0):
#    rem=num%10
#    rev=rev*10+rem
#    num=num//10
#print(rev)
#######################
# ?? prgm to convert 123 to 321(PALINDROME)
num=int(input("enter a number"))
res=0
while(num>0):
    rem=num%10
    res=res+(rem**3)
    num=num//10
print(res)

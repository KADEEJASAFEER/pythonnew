#if we want to check or evaluate multiple condn we can use if...elif...else
#if(cond1):
#    stmnt1
#elif(condn2):
#   stmnt2
#else(condn3)
#   stnmnt3
#
#
#elif(condn n)
#   stmnt n

#check the number is positive or negative

'''num=int(input("enter a number:"))
if(num>0):
   print("num is positive")
elif(num==0):
    print("number is 0")
else:
    print("num is negative")'''


#############################
#print the largest among two numbers
#num1 = int(input("enter a number1:"))
#num2 = int(input("enter a number2:"))
#if (num1 > num2):
#    print(num1, "is largest")
#elif(num1==num2)
#    print(num1,"and",num2,"are equal")
#else:
#    print(num2, "is largest")
##################################
#input 3 nmbrs and find  largest
#num1=int(input("enter a number1:"))
#num2=int(input("enter a number2:"))
#num3=int(input("enter a number3:"))
#if((num1>num2) & (num1>num3)):
#    print(num1,"is largest")
#elif((num2>=num1) & (num2>=num3)):
 #   print(num2,"is largest")
#else:
 #   print(num3,"is largest")
####################################
#input 3 nmbrs and find  second largest
#num1=int(input("enter a number1:"))
#num2=int(input("enter a number2:"))
#num3=int(input("enter a number3:"))
#if((num1>num2) &(num1>num3)):
 #   if(num2>num3):
#       print(num2,"is second largest")
#    else:
 #       print(num3,"is second largest")
#elif((num2>num1) & (num2>num3)):
 #   if(num1>num3):
 #        print(num1,"is second largest")
#    else:
#        print(num3, "is second largest")
#elif((num3>num1)&(num3>num2)):
#    if(num1>num2):
 #       print(num1, "is second largest")
 #   else:
 #       print(num2, "is second largest")
 #################################################
 #read the name od student and 3 marks and find total
#total>145 printA+
#total 145-140 printA
#total 140-135 print B+
#total 135-130 print B
#below 130 fail
name = input("enter name:")
mark1=int(input("enter mark1:"))
mark2=int(input("enter mark2:"))
mark3=int(input("enter mark3:"))
total=mark1+mark2+mark3
print("total mark is : ",total)
if(total>145):
    print("your grade is: A+")
elif((total<=145)&(total>140)):
    print("your grade is: A")
elif((total<140)&total>135):
    print("your grade is: B+")
elif((total<135)&total>130):
    print("your grade is: B")
else:
    print("you failed")

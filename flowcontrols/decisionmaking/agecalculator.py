#dob=input("enter date of birth:")
cdate=8
cmnth=6
cyear=2020
bdate=int(input("enter date"))
bmnth=int(input("enter mnth"))
byear=int(input("enter year"))
age=cyear-byear

if(bmnth>cmnth):
    if(bdate<cdate):
        age=age-1;
print("you are",age,"years old")
#elif(cmnth<bmnth):
 #   age=cyear-byear-1
  #  print(age)'''


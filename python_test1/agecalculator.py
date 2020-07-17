from datetime import date
#program to calculate age
'''cdate=29
cmnth=6
cyear=2020
bdate=int(input("enter date"))
bmnth=int(input("enter mnth"))
byear=int(input("enter year"))
age=cyear-byear

if(bmnth>cmnth):
    if(bdate<cdate):
        age=age-1;
print("you are",age,"years old")'''

######################
dob=input("enter your dob dd/mm/yy")
#print(dob)
dob=dob.split("/")
b_date=dob[0]
b_month=dob[1]
b_year=dob[2]
#print(b_month)
today=str(date.today())
print("Today's date:", today)
today=today.split("-")
c_date=today[2]
c_month=today[1]
c_year=today[0]
#print(c_year)
age=int(c_year) - int(b_year)
if((c_month<b_month)):
    age-=1
if((c_month<b_month)):
    if(c_date<b_date):
        age-=1
print("your age is",age)
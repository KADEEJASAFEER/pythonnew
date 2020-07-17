import re

x='[a-zA-Z]\w*@gmail[.]com'

mail=input("enter mail id")

match=re.fullmatch(x,mail)
if(match!=None):
    print("valid")
else:
    print("invalid")
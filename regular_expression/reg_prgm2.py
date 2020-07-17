#first character should be alphabet b/w: A-K
#second character should be digit and didvisible by 3
#third character sholud be any nmbr of characters
#a9kjnc

import re

x='[a-k][369][a-z]*'
#'*' is used to reprsent any nmbr of characters
vname=input("enter varaiable name")

match=re.fullmatch(x,vname)
#fullmatch to chk whether the given varailble name fully match with the conditions
if(match!=None):
    print("valid")
else:
    print("invalid")


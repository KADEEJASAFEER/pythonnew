#9020105653

import re

x='\d{10}'

nmbr=input("enter  number")

match=re.fullmatch(x,nmbr)
if(match!=None):
    print("valid")
else:
    print("invalid")
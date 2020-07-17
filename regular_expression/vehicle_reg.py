#kl47H1200

import re

#x='KL[0-9]{2}[a-z]{2}[0-9]{4}'
x='KL\d{2}[a-z]{2}\d{4}'

nmbr=input("enter vehicle number")

match=re.fullmatch(x,nmbr)
if(match!=None):
    print("valid")
else:
    print("invalid")

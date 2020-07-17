import re

f=open("mailfile","r")
x='[a-zA-Z]\w*@gmail[.]com'
for data in f:
    #print(data)
    match = re.fullmatch(x,data)
    if (match != None):
        print(data,"->valid")
    else:
        print(data,"->invalid")


f=open("abc.txt","r")
#f.write("hello")
#lst=["hai","welcome","file"]
#for i in lst:
#    f.write(i+"\n")

####################
#read even numbers from file and store in new file

fw=open("out.txt","w")

for i in f:
    num=int(i)
    if(num%2==0):
        fw.write(str(i))
#using file =>"file1"
fin=open("/file_s/file1", "r")
lst=[]
#for i in fin:
#    print(i)
for name in fin:
    lst.append(name.rstrip("\n"))
print(lst)
for name in fin:
    lst.upper(fin)
print(lst)
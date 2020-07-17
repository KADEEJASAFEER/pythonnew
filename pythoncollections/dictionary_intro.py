###############DICTIONARY
#values are stored in dictoinary in the form of key,value pairs
#person={"name":"ajay","age":25,"gender":"male"}
'''print(person["name"])       #ajay
print(person["gender"])     #male
print(person["age"])  '''      #25
#we need to use key value to fetch the value
#JSON=>java script object notation   #it is used in front end in django
## duplicate values are allowed
###to fetch the keys
#for i in person:
    #print(i)
    #print(person[i])
##############to return key and value in dictionary
'''for k,v in person.items():
    print(k,",",v)  '''


#########
#employee=>name,id,salary,designation
employee={"name":"amith","id":"1","salary":25000,"designation":"developer"}
#print(employee["name"])
#for k,v in employee.items():
#    print(k,"",v)
#####to append a value in dictionary
employee["exp"]=2
print(employee)
#######increase salary
#employee["salary"]+=5000
#print(employee)
#########to check whether key word is in dictionary
#print("name" in employee)
###############
##to update value in dictionary
#employee["name"]="ajith"
#print(employee)
##key cannot be updated
#################
'''student={"name":"abin","age":22,"course":"mca"}
for k in student:
    print("key:",k)     #name   age   course
#print both key and value:
for k,v in student.items():
    print(k,",",v)
#adding new key value pair
student["tot"]=150  '''








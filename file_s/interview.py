#printPerson(id=101)#print name
#printPerson(id=101,slary)#print name,salary of person
#printPerson(id=102,property=designation) #print name,salary,designation
f1=open("C:/Users/user/PycharmProjects/pythonclass/file_s/person.txt","r")
emp={}


for data in f1:
    #print(data)
    val=data.rstrip("\n").split(",")
    #print(val)  #['100', 'sooraj', '25', 'developer', '2', '25000']
    id=val[0]
    name=val[1]
    age=val[2]
    desig=val[3]
    exp=val[4]
    salary=val[5]
    if(id not in emp):
        emp[id]={"id":id,"name":name,"age":age,"desig":desig,"exp":exp,"salary":salary}
    else:
        pass
#print("employee",emp)
for k,v in emp.items():
    print(k,"\t",v)

#######################
#function to print employee name by passing id
'''def printEmp(**kwargs):
    for k,v in kwargs.items():
        id=v
        if(id in emp):
            print(emp[id]["name"])
        else:
            print("employee not found")

printEmp(id="100")'''

#######################
#function to print employee name and salary by passing id
'''def printEmp1(**wargs):
    for k,v in wargs.items():
        id=v
        if(id in emp):
            print(emp[id]["name"])
            print(emp[id]["salary"])
        else:
            print("employee not found")

printEmp1(id="100")'''

#######################
#function to print employee name and property by passing id and property
def printEmp2(**wargs):
    #for k,v in wargs.items():
        #print(k,"\t",v)     #id   100 propert  desig
    if "id" in wargs:
        id = wargs["id"]
        if id in emp:
            print("employee name:",emp[id]["name"])
        else:
            print("employee not found")
    if "property" in wargs:
        prop=wargs["property"]
        print(prop,":",emp[id][prop])
    #print(id,"\t",prop)


printEmp2(id="100",property="salary")


###############################
'''emp={}
#{100{name:sooraj,age:25,desig:developer,exp:2,salary:25000}}=>stored as nested dictonary
emp={100:{"name":"sooraj","age":25,"design":"developer","exp":2,"sal":25000},
     101:{"name":"jinon","age":26,"design":"sales","exp":3,"sal":30000}}
#print(emp[100]["name":"sooraj","age":25,"designation":"developer","experience])
print(emp[101]["sal"])

for emp in f1:
    emp1=emp.rstrip("\n").split(",")
    #print("{",emp1[0],":{name:",emp1[1],",age:",emp1[2],",designation:",emp1[3],",experience:",emp1[4],",salary:",emp1[5],"}}")
'''





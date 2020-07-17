f=open("C:/Users/user/PycharmProjects/pythonclass/file_s/complete.csv","r")

cases_dict={}
recover_dict={}
died_dict= {}
covid={}

for line in f:
    data=line.rstrip("\n").split(",")
    #print(data)
    state=data[1]
    #print(state)
    confirmed=data[4]
    #print(confirmed)
    cured=data[6]
    death=data[8]
    #print(death)
    if (state not in cases_dict):
        cases_dict[state]=confirmed
    else:
        cases_dict[state]=confirmed
#print(cases_dict)
    if(state not in recover_dict):
        recover_dict[state]=cured
    else:
        recover_dict[state]=cured
    if(state not in died_dict):
        died_dict = death
    else:
        pass
#print("total death:",died_dict)

    if(state not in covid):
        covid[state]={"id":state,"confirmed":confirmed,"cured":cured,"death":death}
    else:
        pass
#print(covid)
for k,v in covid.items():
    print(k,"\t",v)
#print(covid)
#print("total cases:",cases_dict)
#print("total cured:",recover_dict)

def getvalue(**kwargs):
    for k,v in kwargs.items():
        #print("ka",k,v)
        id=v
        #print(id)
        if id in covid:
            print("state",covid[id])
        else:
            pass
        '''if property in covid:
            prop=covid["property"]
            print("property",covid[id][prop])'''

getvalue(id="Telangana",property="confirmed")




f=open("C:/Users/user/PycharmProjects/pythonclass/file_s/complete.csv","r")

i=0
dict={}
dict1={}
tot=0

#############check statewise cases
for line in f:
    rprt=line.rstrip("\n").split(",")
    #print(rprt)
    state=rprt[1]
    #print(state)
    cases=int(rprt[4])
    recover=int(rprt[6])
    #print(recover)
    if(state not in dict):
        dict[state]=cases
    else:
        dict[state]=cases
#print(dict)
    if(state not in dict1):
        dict1[state]=recover
    else:
        dict1[state]=recover
#print(dict1)
##########to check total nmbr of cases in india
'''caseslist=[]
for k,v in dict.items():
    caseslist.append(v)
print(sum(caseslist))
#OR
total=0
for k,v in dict.items():
    total+=v
print(total)    '''
#########state with  highest number confirmed cases
'''statelst=[]
for k,v in dict.items():
    statelst.append((v,k))
print(statelst)
sortedata=sorted(statelst,reverse=True)
print("state with highest nmbr pf confirmed cases",sortedata[:3])   '''
#########state with highest recoverd number
#print(recover)
'''recvrlst=[]
for k,v in dict1.items():
   recvrlst.append((v,k))
print(max(recvrlst))
sortlst=sorted(recvrlst,reverse=True)
print("states with highest recovery rate are: ",sortlst[:3])'''










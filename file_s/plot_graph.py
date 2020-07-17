#import matplotlib.pyplot as plt

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

tot=0
##finding the 3 states having maximum number of cases
states=[]
cnt=[]
srtlst=[]
for k,v in dict.items():
    srtlst.append((v,k))
print(srtlst)
sorteddata=sorted(srtlst,reverse=True)
report=sorteddata[:3]
for val in report:
    cnt.append(val[0])
    states.append(val[1])
#plt.bar(states,cnt)
#plt.show()

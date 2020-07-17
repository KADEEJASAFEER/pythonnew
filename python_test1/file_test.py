f=open("C:/Users/user/PycharmProjects/pythonclass/python_test1/data.txt","r")

dict={}
dist_lst=[]

for data in f:
    data=data.rstrip("\n").split(",")
    #print(data)
    dist=data[0]
    #print(dist)
    temp=data[1]
    #print(temp)
    if(dist not in dict):
        dict[dist]=temp
    elif(temp>dict[dist]):
        dict[dist]=temp
    else:
        pass
print(dict)
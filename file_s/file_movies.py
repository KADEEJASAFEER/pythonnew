f=open("C:/Users/user/PycharmProjects/pythonclass/file_s/movies .csv","r")
list1=[]
list2=[]
list3=[]
dict={}
i=0
for line in f: #1	The Nightmare Before Christmas	1993	3.9	4568
    word=(line.rstrip("\n").split(","))
    print(word)
    rate=(word[3])
    rate=(float(rate))
    print(rate)
    if((rate)>=3.5):
        list1.append(word)
    elif(3.5>=(rate)>=2.5):
        list2.append(word)
    elif((rate<=2.5)):
        list3.append(word)
    else:
        pass
    i+=1
    if(i==100):
        break
l1=len(list1)
l2=len(list2)
l3=len(list3)
print("m with rating >=3.5",list1)
print("list2",list2)
print("list3",list3)

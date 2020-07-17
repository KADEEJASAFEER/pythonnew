##prgm to find missing integer from [-1,0,1,3,4]
lst=[-1,0,1,2,3,5]
lst.append(0)
lst.sort()
#print(lst)
temp=0
num=0
lower=0
upper=len(lst)-1
mid=(lower+upper)//2
while(lower<upper):
    temp=lower+1
    if((lst[temp]-lst[lower])>1):
        num=lst[lower]+1
        print(num)
        break
    lower=lower+1

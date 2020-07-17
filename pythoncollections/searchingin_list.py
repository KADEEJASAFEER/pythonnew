#linear searching==> compare each and every element,which increases processing time)
#####
# prgm to search a nmbr in list
#increses complexity
#lst=[10,11,12,13,14,15]
#cnt=0
#elmnt=int(input("enter elmnt for searching"))
#flg=0
#for i in lst:
#    cnt+=1
#    if(i==elmnt):
#        flg=1
#    else:
#        pass
#if(flg==1):
#    print("elemnt found in position",cnt)
#    print("elmnt in list")
#else:
#    print("not in list")
##############################
## binary search
####lst=[11,10,9,8,6,7,12]
#first we need to sort this list
###lst.sort()
#print(lst)
#input of binary search is an sorted araay
#lst=[6,7,8,9,10,11,12]
#upper=len(lst)
###searchelement=11
#low=0
#upper=7
#calculate mid=(low+upper)/2   =>(0+7)/2=3.5=>3
#print(lst[3])
#we will compare srchelement with middle elmnt
#3 possible cases
#11 middle element=9
#case1: searchelemnt>lst[mid]  11>9
#low=mid+1
#case2 : searchelement<mid  suppose search elemnt is 7 ie., 7<9
#upper=mid-1
#case3:search elemnt =lst[mid] ie., searchelemnt is 9 and mid is 9 "element found

###################################
###prgm using binary seaech
'''lst=[10,9,11,8,12,7,13,6]
lst.sort()
print(lst)
low=0
upper=len(lst)-1 #7 (same size as array)
print(upper)
element=int(input("enter search element : "))  #11
while(low<upper):           #0<7            #4<7
    mid=(low+upper)//2      #(0+7)//2=3     #(4+7)//2=5
    if(element>lst[mid]):   #11>9           #11>lst[5],11>11
        low=mid+1           #low=4
    elif(element==lst[mid]):
        print("element found")
        break   '''


##################################
##
'''lst=[10,15,18,16,12,20,11,19]
lst.sort()
#############[10, 11, 12, 15, 16, 18, 19, 20]
print(lst)
low=0
upper=len(lst)-1 #7 (same size as array)
#print(upper)
flg=0
element=int(input("enter search element : "))  #11
while(low<upper):           #0<7
    mid=(low+upper)//2      #(0+7)//2=3     #(4+7)//2=5
    print(mid)
    if(element>lst[mid]):   #11>15           #11>lst[5],11>11
        low=mid+1           #low=4
        print(low)
    elif(element==lst[mid]): #11==15
        flg=1
        break
    elif(element<lst[mid]): #11<15
        upper=mid-1         #upper=3-1=2
        print(upper)
if(flg==1):
    print("element found")
else:
    print("element not found")  '''

################################
##prgm to find pairs from list when sum is given using binary search
lst=[2,1,4,3]   #sum=6
lst.sort()  #[1,2,3,4]
val=int(input("enter sum to find pairs: "))
lower=0
upper=len(lst)-1    #3
#print(upper)
pairs=[]
while(lower<upper):                 #0<3        #1<3
    res=lst[lower]+lst[upper]       #res=1+4=5  #res=2+4=6
    if(res==val):                   #6==5       #6=6
        pairs.append((lst[lower],lst[upper]))
        print(pairs)
        #print("pairs: (",lst[lower],",",lst[upper],")")
        break
    elif(res<val):                  #5<6
        lower=lower+1               #lower=0+1=1
    elif(res>val):                  #5>6
        upper=upper-1


####################





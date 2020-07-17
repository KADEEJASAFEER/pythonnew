# ==========LIST===============
# create using square brackets  []
# lst=[] #creates empty list
# to check type of list
# lst=list()
# print(type(lst))   #<class 'list'>

# we can store different types of data inside
# lst=[10,20,"hello",True]
# print(lst)

############################
# prgm to print even nmbrs from list
# lst=[45,78,98,65,32,12,74,52,41,36,25,99,258]
# for i in lst:
#   if(i%2==0):
#        print(i)
#   else:
#       pass

############################
# prgm to print sum of nmbrs in list
# lst=[45,78,98,65,32,12]
# tot=0
# for val in lst:
#    tot=tot+val
# print(tot)

############################
# prgm to print max  from list
# lst=[45,78,98,65,32,12]
# print(max(lst))

############################
# prgm to print min  from list
# lst=[45,78,98,65,32,12]
# print(min(lst))

############################
#####slicing
#lst=[45,78,98,65,32,12,74,52,41,36,25,99,258]
#print(lst[1:3])
######print first 7 elements
#print(lst[:4])
#########print after 2 elements
#print(lst[2:])
#########python supports -ve indexing
#print(lst[-2])
########append element
# lst.append(50)
# print(lst)

#########################
##create a list and store even nmbrs in even list and odd nmbrs in odd list
#lst = [42, 24, 12, 58, 78, 98, 65, 35, 32, 34, 74, 45, 12]
#evn = []
#odd = []
#for i in lst:
#    if (i % 2 == 0):
#        evn.append(i)
#    else:
#        odd.append(i)
#print(evn)
#print(odd)

#########################
##create a list and store even nmbrs in even list and odd nmbrs in odd list and find squares
#lst=[]
#for a in range(1,10):
#    lst.append(a)
#    evn=[]
#    odd=[]
#evn=[i for i in lst if i%2==0]
#print(evn)
#for i in lst:
#    if (i%2 == 0):
#        evn.append(i**2)
#    else:
#        odd.append(i**2)
#print("even list",evn)
#print("odd list",odd)
#################################
#using function
#def sqre(lst):
#    squares=[]
#    for item in lst:
#        squares.append(item**2)
#    return squares
#evensquare=sqre[even]












###################################
# prgm to search a nmbr in list (linear searching==> compare each and every element,which increases processing time)
#lst=[10,11,12,13,14,15]
#cnt=0
#elmnt=int(input("enter elmnt for searching"))
#flg=0
#for i in lst:
#    cnt+=1
 #   if(i==elmnt):
 #   else:
#if(flg==1):
 #   print("elemnt found in position",cnt)
 #   print("elmnt in list")
#else:
#    print("not in list")

#################################


#o/p=>6(read from user)
#pair which give 6 when adding 2 nmbrs in list
#lst=[1,2,3,4]
#tot=int(input("enter the sum : "))
#for i in lst:
#    for j in lst:
#        if(i+j==tot):
#            print("sum is",tot,"when the pairs  (",i,j,")")

#in this type complexity is high
#####################################
#  i/p  =>  o/p
#[4,6,8]=>[14,12,10]
#or
#[3,4,8]=>[12,11,7]
lst=[4,6,8]
#print(lst[0])
lst1=[]
'''lst[0]+=10
lst[1]+=6
lst[2]+=2
print(lst)'''
for i in lst1:
    lst1[0]=lst[1]+lst[2]
    lst1[1]=lst[0]+lst[2]
    lst1[2]=lst[0]+lst[1]
    lst1.append(i)
print(lst1)
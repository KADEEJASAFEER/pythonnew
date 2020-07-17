#for loop
#initialization
#increment/decrement
##  no increment / decrement case
#for i in range(0,10):
 #   print(i)

##with increment
#for i in range(0,10,2):   #increment by 2
 #   print(i)

##with decrement
#for i in range(10,0,-1):  # increment by -1
#    print(i)

##################
#print multiplication table of 2
#n=int(input("enter the number"))
#for i in range(0,11):
#   print(i,"*",n,"=",(i*n))

##################
#print factorial
#n=int(input("enter number"))
#f=1
#if(n>0):
#    for i in range(1,n+1):
 #       f=f*i
#    print(f)
#else:
 #   print("no factorial")

##################
#prgm to print in format
#123
#456
#789

#for i in range(1,10,3):
#    for n in range(i, i+3):
#        print(n, end=' ')
#    print("")



##################
#prgm to check prime nmbr
#n=int(input("enter a nmbr: "))
#flg=0
#for i in range(2,n):
#    if(n%i==0):
 #      flg=1
 #      break
 #   else:
#       pass
#if(flg>0):
#    print(n," is not prime")
#else:
#    print(n,"is prime")

##################
#prgm to print prime nmbrs btwn a range
#10..........17
#l=int(input("enter lower limit"))
#u=int(input("enter upper limit"))
#for i in range(l,(u+1)):
#    flg = 0
#    for n in range(2,i):
#        if((i%n)==0):
#            flg=1
#            break
#        else:
#            pass
#    if(flg>0):
#        pass
#    else:
#        print(i,"is prime")

##################
#prgm to  find the sum of prime numbers in range
'''l=int(input("enter lower limit"))
u=int(input("enter upper limit"))
sum=0
for i in range(l,(u+1)):
    flg = 0
    for n in range(2,i):
        if((i%n)==0):
            flg=1
            break
        else:
            pass
    if(flg!=1):
        print(i, "is prime")
        sum+=i
    else:
        pass
print(sum,"is sum of prime")'''
#####################
'''for i in range(1,5): #i for row  wise
    for j in range(1,(i+1)):    #j for column wise
        print(i,end="")
    print("\n")'''
################
'''for i in range(5,0,-1):
    for j in range(1,(i+1)):
        print("*",end="")
    print("\n")'''







#function is set of statements that us used for performing a particular task
#eg: print(),input(),type()

#user defined functions
#syntax
#def functionname(argument 1,argument 2 ...........)
    #function body
    #return stmnt

#we can create function in 3 ways:
#1) function with no argument and no return type
#def add():
#   num1=10
#   num2=20
#   print(num1+num2)
#we can call the function using function name
#add()  #calling the function add

#####################
# function to perform subtract
#def sub():
#    num1=20
#    num2=10
#    print((num1-num2))
#sub()

#####################
# function to perform multiplication
#def mul():
#    num1=20
#    num2=10
#    print((num1*num2))
#mul()

#####################
# function to perform division
#def div():
#    num1=20
#    num2=10
#    print((num1/num2))
#div()

#####################
# function to perform modulo
#def mod():
#    num1=20
#    num2=6
#    print((num1%num2))
#mod()

################
#2) function with argument and no return value
#syntax
#def functionname(arg1,arg2,.............)
# function body

#####################
# function to perform addition
#def add(num1,num2):
#    res=num1+num2
#    print(res)
#add(10,20)

#####################
# function to perform multiplication
#def mul(num1,num2):
#    res=num1*num2
#    print(res)
#mul(10,20)

#####################
# function to perform multiplication
#def div(num1,num2):
#    print((num1/num2))
#div(10,5)

############
#create a fn to chk nmbe is even or odd
#def chknm(num):
#    if(num%2==0):
 #       print(num,"is even")
#    else:
#        print(num,"is odd")
#chknm(13)

#############################
#create a fn to chk numbr is prime or not
#def chkprime(n):
#    flg=0
 #   for x in range(2,n):
#        if(n%x==0):
#            flg=1
#            break
#        else:
#    if(flg>0):
 #       print("not prime")
#   else:
 #       print("prime")
#chkprime(7)


#################
#3) function with argument and return value

#def functionname(arguments.........)
#   function body
#   return value

###############################
# function for addition
#def add(num1,num2):
#    res=num1+num2
#    return res

#val=add(10,20)
#print(val)

###############################
# function for subtraction
#def sub(num1,num2):
#    res=num2-num1
#   return res

#val=sub(10,20)
#print(val)
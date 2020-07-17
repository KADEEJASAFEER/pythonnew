#anonymous function=>nameless

#def add(num1,num2):
#    return (num1+num2)

#remove add since it is nameless
#def (num1,num2):
#    return (num1 + num2)


#lambda function to add
'''''
f=lambda num1,num2:(num1 + num2)
#to call the function
print(f(10,2))
#def sub(num1,num2):
#    return (num2-num1)
#lambda function to subtract
f2=lambda num1,num2:num2-num1
print(f2(5,10))

#lambda function to multiplication
f3=lambda num1,num2:num1*num2
print(f3(5,8))

#lambda function to division
f4=lambda num1,num2:(num2/num1)
print(f4(10,5))

#lambda function to floor division
f5=lambda num1,num2:(num1//num2)
print(f5(10,5))

#lambda function to modulous
f6=lambda num1,num2:(num1%num2)
print(f6(10,7))

sq=lambda num:num**2
print(sq(5))
'''


#map function
#find square of list elements
#lst=[10,20,30,40]
#here we select each input and perfom square of each element
#(lst)=>sq(f(x))=>100,400,900,1600
#here we use map function
#to convert employees name to uppercase


#filter function
# to print even numbers from list
#to list employees above salary 25000

lst=[10,20,30,40,11,28,35,42]
#square of all elements we use map function
#def square(num1):
#    return (num1*num1)
#sq=lambda num1:num1**2
#map anf filter both uses 2 arguments
#map(function,iterables)
#sqlist=list(map(square,lst)) #by using function
sqlist=list(map(lambda num1:num1**2,lst)) #by using lambda
print(sqlist)
#to find cube of list
cubelist=list(map(lambda num1:num1**3,lst))
print(cubelist)

#def numCheck(num1):
#    return (num1%2==0)
#evn=lambda num1:num1%2==0

even=list(filter(lambda num1:num1%2==0,lst))
print(even)

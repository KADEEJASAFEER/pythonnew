#list comprehension

lst=[1,2,3,4]

'''''
sq=list(map(lambda x:x**2,lst))
print(sq)
even=list(filter(lambda x:x%2==0,lst))
print(even) '''

#list comprehension
#square=[(i**2) for i in lst]
#print(square)
#cube=[(i**3) for i in lst]
#print(cube)

###########################
lst=[1,2,3]
lst2=[4,5,6]
#print the numbers in pairs
#(1,4),(1,5),(1,6),(2,4)....(3,6)

'''for i in lst:
    for j in lst2:
        #print((i,j))
        pass
pairs=[(i,j) for i in lst for j in lst2]
print(pairs)'''

#(1**4),(1**5),(1**6).....

'''for i in lst:
    for j in lst2:
        #print(i**j)
        pass
power=[(i**j) for i in lst for j in lst2]
print(power)    '''

###even numbers
#even=[i for i in lst2 if i%2==0] #can do only single operation
even=[i for i in lst2 if i%2==0]
print(even)

'''obj = ["Even" if i%2==0 else "Odd" for i in range(10)]
print(obj)  '''

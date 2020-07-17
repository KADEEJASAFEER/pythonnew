'''def add(num1,num2):
    print(num1+num2)
add(10,20)'''

#variablelength argument

'''def add(**kwargs):
    #print(kwargs)
    tot=0
    for k,v in kwargs.items():
        tot+=v
    print(tot)

add(num1=10,num2=20,num3=30,num4=40)    '''
#$recieved as dictonary
#can pass any nmbr of agrumnets

def person(*args):
    print(args)
person("sajay",25,25000)    #recieved as tuple
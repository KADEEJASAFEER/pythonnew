###############SET###############
#####define
#st={}
#print(type(st)) #class <'dict">
##empty set gives type dictionary
#st=set()   #to define empty set
#print(type(st)) ###  <class 'set'>
###set fn with values
#st={10,20,25,45}
#print(st)
#########store duplicates
#st={10,20,25,45,25,"hello"}
#print(st)
###cant store duplicates
####is input and output preserved
'''st={10,20,25,45,25,"hello"}
print(st)'''
###insertion order is not preserved

#########################
###remove duplicates value from  list
'''lst=[10,10,20,20,30,30]
st=set(lst) #convert list in to set
print(st)   #{10,20,30}
lst=list(st)
print(lst)      #[10,20,30]'''

#####################
###operations on set  =>union,intersection,difference
##1)union
'''st1={10,20,30,40}
st2={30,40,50,60}
unionst=st1.union(st2)
print("union = ",unionst)
##2)intersection
intrst=st1.intersection(st2)
print("intersecton =",intrst)
##3)difference
difrnsst=st1.difference(st2)
print("differennce set =",difrnsst)
difrnc2=st2.difference(st1)
print("difference set2 =",difrnc2)'''

#####################
####nee to print only unique words from a random txt
'''data="this is a this is a random text to check to check"
words=data.split(" ")       #it can be used to split string
print(words)
st=set(words)
print(st)'''
###########################
#s="Rooose"
#v={i for i in s}
#print(len(v))
##########
st={10,20,30}
st.add(40)
st.update([50,60])
print(st)






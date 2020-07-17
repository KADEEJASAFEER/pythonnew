#find word count in file   "data"
f=open("C:/Users/user/PycharmProjects/pythonclass/file_s/data", "r")
dict={}
for line in f:
    #print(line)    #A tuple is a sequence of immutable Python objects.
    #word=line.split(" ")
    #print(word) #['A', 'tuple', 'is', 'a', 'sequence', 'of', 'immutable', 'Python', 'objects.\n']
    words=(line.rstrip("\n").split(" "))    #['A', 'tuple', 'is', 'a', 'sequence', 'of', 'immutable', 'Python', 'objects.']
    print(words)
    for word in words:
        if(word not in dict):
            dict[word]=1
        else:
            dict[word]+=1
for k,v in dict.items():
    print(k,"=>",v)
#####to check word count in text
'''text="hai hello hai hello"
####o/p=>{"hai",2,"hello",2,......}
word=text.split(" ")
print(word)
dict={}
for word in word:               #hai,hello
    if(word not in dict):
        dict[word]=1            #dict=("hai",1,"hello",1)
    else:
        dict[word]+=1           #dict=("hai"=2,"hello",2)
print(dict) '''

################
#first recurring character
txt=input("enter the recurring text: ")
wrd=list(txt)
#print(wrd)
dict={}
flg=0
for i in wrd:
    if(i not in dict):
        dict[i]=1
    else:
        dict[i]+=1
        print("the recursing character is :",i)
        flg=1
        break
if(flg==0):
    print("no recursing character found")

f1=open("C:/Users/user/PycharmProjects/pythonclass/file_s/students.txt","r")
f2=open("C:/Users/user/PycharmProjects/pythonclass/file_s/passed.txt","r")
f3=open("C:/Users/user/PycharmProjects/pythonclass/file_s/failed.txt","w")

st1=set()
st2=set()

def readfromfile(fref):
    st=set()
    for data in fref:
        data=data.rstrip("\n")
        st.add(data)
    return st
    #print(st)
st1=readfromfile(f1)
st2=readfromfile(f2)
fail=st1-st2
#print(fail)
for data in fail:
    f3.write(data)
f3.flush()
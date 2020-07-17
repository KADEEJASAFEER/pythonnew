f1=open("students.txt","r")
f2=open("passed.txt","r")
f3=open("failed.txt","w")


def fileread(a):
    st=set()
    for name in a:
        name=name.rstrip("\n")
        st.add(name)
    #print(st)
    return st
st1=fileread(f1)
st2=fileread(f2)
print(st1)
print(st2)
fail=st1-st2
print(fail)
for st in fail:
    f3.write(st+"\n")

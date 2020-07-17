f=open("C:/Users/user/PycharmProjects/pythonclass/file_study/movies_study.csv")

for line in f:
    m=line.rstrip("\n").split(",")
    #print(m)
    name=m[1]
    #print(name)
    rate=m[3]
    #print(rate)
    rate=float((rate))
    #print(rate)
    if((rate)>=3.5):
        print(name)



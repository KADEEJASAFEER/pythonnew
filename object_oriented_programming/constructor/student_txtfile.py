class studentFile:
    def __init__(self,id,name,course,mark):
        self.id=id
        self.name=name
        self.course=course
        self.mark=mark

    def printValues(self):
        print(self.id,",",self.name,",",self.course,",",self.mark)

f=open("student.txt")
lst=[]

for data in f:
    #print(data)
    student=data.rstrip("\n").split(",")
    id=student[0]
    name=student[1]
    course=student[2]
    mark=int(student[3])
    ob=studentFile(id,name,course,mark)
    ob.printValues()
    lst.append((ob))

for student in lst:
    #print(student.id)
    name=student.name
    #print(name.upper())

for student in lst:
    course=student.course
    if(course=="mca"):
        print("student list of MCA:",student.name)
    elif(course=="bca"):
        print("student list of BCA:",student.name)

for student in lst:
    mark=student.mark
    if(mark>=150):
        print("students with mark>150:",student.name)
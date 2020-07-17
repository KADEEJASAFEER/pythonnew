x=10
def val():
    global x    #if x is global it will print 100
    x=50    #here scope of x is local
    x=x+50
val()
print(x)    #10
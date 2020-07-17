'''import mathfun.arithopration
res=mathfun.arithopration.add(10,20)
print(res)
sub=mathfun.arithopration.sub(20,10)
print(sub)'''
#this method needs to call the heirarchy each time which is a draw back
import mathfun.arithopration as mp
res=mp.add(40,20)
print(res)
#to overcome this we use this:
'''from mathfun.arithopration import add,sub,div
add=add(10,20)
print(add)
##to call all the functions use:
from mathfun.arithopration import *
ml=mul(10,20)
print(ml)'''
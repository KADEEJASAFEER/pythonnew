#Exception is abnormal situation in a prgm
#try,except,finally,raise
#try=>doubtful/abnormal code
#except=>handling code
#finally=>for clean up processing/this code will execute
#raise=>customized exception


'''num1=int(input("enter number"))
num2=int(input("enter number2"))
try:
    res=num1/num2

    print(res)

#user defined msg
#except:
#    print("exception occured")

#bulilt in or predefined  exception msg
except Exception as e:
    print(e.args)

#finally:
 #   print("have database transaction")'''



age=int(input("enter age"))

if(age<18):
    raise Exception("invalid age")
    #print("u cant vote")
else:
    print("u can vote")




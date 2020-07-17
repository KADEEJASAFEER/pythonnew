#pattern matching

import re
'''matcher=re.finditer("ab","ababaabbabababbababab")
count=0
for match in matcher:
    print(match.start())
    #start will return which locations/position where match found
    print(match.group())
    #which pattern is matched
    count+=1
    #to find count of pattern
print(count)'''

#######################
#predefined character sets

#x='[abc]'
#check either a or b or c
#x='[a-z]'
#check for characters from a to z
#x='[0-9]'
#check for numbers btwen 0 to 9
#x='[a-zA-Z]'
#check for uppercase and lowecase alphabets
#x='[a-zA-Z0-9]'
#check for all alphabets and numbers
#x='[^a-z]'
# check for characters except a to z
#x='[^0-9]'
#except 0 to 9
#x='[^a-zA-Z0-9]'
#check for special characters

#############################

#pre-defined characters
#x='\s'  #chk for space
#x='\d' #chk for digits[0-9]
#x='\D'     #chk for [^0-9]
#x='\w'      #chk for [a-zA_Z0-9]

'''matcher=re.finditer(x,"ab_@ 97Z ")
count=0
#it will check any of the character
for match in matcher:
    print(match.start())
    print(match.group())'''

############################
#QUANTIFIERS
#x="a+b"  #chk for combination and single character 'a'
#x="a*"   #chk for position even if match is not found
#x="a?"      #check all characters position induvidually
#x='a{2}'    #chk for combination of 2 nmbr of 'a'
x='a{2,3}'  #chk for minimum 2 nmbr and max 3 nmbr of 'a'
#x='^a'      #chk whether given string is starting with 'a' or not
#x='a$'      #chk with which character/position  enter the string


matcher=re.findall(x,"aabbaaaac")
print(matcher)

'''count=0
#it will check any of the character
for match in matcher:
    print(match.start())
    print(match.group())
    #count += 1
    # to find count of pattern
#print(count)  '''


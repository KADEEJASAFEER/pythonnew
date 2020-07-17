import re

'''txt = "The rain in Spain falls mainly in the plain!"

#Check if the string contains "ai" followed by 0 or more "x" characters:

x = re.findall("ai*", txt)
for a in x:
    print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")'''


import re

string = '2102 1111'

# Three digit number followed by space followed by two digit number
pattern = '(\d{3}) (\d{2})'

# match variable contains a Match object.
match = re.search(pattern, string)
#print(match.group(1,2)
print(match.start())
print(match.end())
print(match.span())
print(match.re)
print(match.string)


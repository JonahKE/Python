l = ['magical unicorns',19,'hello',98.98,'world']
string = ""
number = 0
strcount = 0
numcount = 0
for x in l:
    if isinstance(x, str):
        string += x + " "
        strcount += 1
    elif isinstance(x, (int, long, float, complex)):
        number += x
        numcount += 1
if strcount != 0 and numcount != 0:
    print "The array you entered is of mixed type"
elif strcount != 0 and numcount == 0:
    print "The array you entered is of string type"
elif strcount == 0 and numcount != 0:
    print "The array you entered is of number type"
else:
    print "The array you entered is neither of string nor integer type"
print "Sum: ",  number
print "String:", string
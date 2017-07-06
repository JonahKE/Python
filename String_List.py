# Find and Replace
words = "It's thanksgiving day. It's my birthday,too!"
print words.find("day")
words2 = words.replace("day", "month")
print words2
# Min and Max
x = [2,54,-2,7,12,98]
print max(x)
print min(x)
# First and Last
x = ["hello",2,54,-2,7,12,98,"world"]
print x[0]
print x[len(x)-1]
xnew = [x[0],x[len(x)-1]]
print xnew
# New List
x = [19,2,54,-2,7,12,98,32,10,-3,6]
xsorted = sorted(x)
xnew = xsorted[len(xsorted)/2:]
xnew.insert(0, xsorted[:len(xsorted)/2])
print xnew
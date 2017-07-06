print "x", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
for line in range(1,13):
    print line,
    for number in range(1,13):
        print line*number,
    print " "
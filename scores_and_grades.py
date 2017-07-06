import random
for x in range(10):
    score = random.randint(60,101)
    if score >= 60 and score <=69:
        print "Score: {}; Your grade is D".format(score)
    elif score >= 70 and score <=79:
        print "Score: {}; Your grade is C".format(score)
    elif score >= 80 and score <=89:
        print "Score: {}; Your grade is B".format(score)
    else:
        print "Score: {}; Your grade is A".format(score)
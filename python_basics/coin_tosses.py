import random
tails, heads, attempt = 0, 0, 0
for toss in range(1,5001):
    flip = random.randint(0,1)
    if flip == 0:
        tails += 1
        attempt += 1
        print "Attempt #{}: Throwing a coin... It's a tail! ... Got {} head(s) so far and {} tail(s) so far.".format(attempt,heads,tails)
    else:
        heads += 1
        attempt += 1
        print "Attempt #{}: Throwing a coin... It's a head! ... Got {} head(s) so far and {} tail(s) so far.".format(attempt,heads,tails)
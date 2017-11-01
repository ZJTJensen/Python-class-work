import random



heads = 0
tails = 0
for i in range (1, 5000):
    random_chance = random.randint(1,2)
    if random_chance == 1:
        heads += 1
        print "Attempt #", i,": Throwing  coin... It's a Head! ... Got ", str(heads), "Head(s) so far and ", str(tails), "tail(s) so far" 
    elif random_chance == 2:
        tails +=1 
        print "Attempt #", i,": Throwing  coin... It's a Tail! ... Got ", str(heads), "Head(s) so far and ", str(tails), "tail(s) so far"